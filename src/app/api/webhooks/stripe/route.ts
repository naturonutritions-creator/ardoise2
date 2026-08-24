import { NextResponse } from "next/server";
import { getStripe } from "@/lib/stripe";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";
import type Stripe from "stripe";

export async function POST(request: Request) {
  const stripe = getStripe();
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

  if (!stripe || !webhookSecret) {
    return NextResponse.json({ received: false, message: "Stripe non configuré." }, { status: 200 });
  }

  const signature = request.headers.get("stripe-signature");
  const body = await request.text();

  let event: Stripe.Event;
  try {
    event = stripe.webhooks.constructEvent(body, signature ?? "", webhookSecret);
  } catch (err) {
    return NextResponse.json({ message: `Signature invalide: ${(err as Error).message}` }, { status: 400 });
  }

  switch (event.type) {
    case "checkout.session.completed": {
      const session = event.data.object as Stripe.Checkout.Session;
      const email = session.customer_email;
      const product = session.metadata?.product;
      const plan = session.metadata?.plan;

      if (email) {
        const [user] = await db.select().from(schema.users).where(eq(schema.users.email, email)).limit(1);
        if (user) {
          if (product) {
            // Achat ponctuel : pack de 6 examens blancs (Brevet ou Bac).
            await db.insert(schema.purchases).values({
              userId: user.id,
              product,
              stripeCustomerId: String(session.customer),
              stripeSessionId: String(session.id),
              status: "active",
            });
          } else if (plan) {
            // Abonnement récurrent (mensuel / annuel / famille).
            await db.insert(schema.subscriptions).values({
              userId: user.id,
              stripeCustomerId: String(session.customer),
              stripeSubscriptionId: String(session.subscription),
              plan,
              status: "active",
            });
          }
        }
      }
      break;
    }
    default:
      break;
  }

  return NextResponse.json({ received: true });
}
