import { NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { getStripe, PLANS, type PlanId } from "@/lib/stripe";

export async function POST(request: Request) {
  const { plan } = (await request.json()) as { plan: PlanId };

  if (!plan || !(plan in PLANS)) {
    return NextResponse.json({ message: "Offre inconnue." }, { status: 400 });
  }

  const stripe = getStripe();
  const priceId = process.env[PLANS[plan].priceEnvVar];

  if (!stripe || !priceId) {
    return NextResponse.json(
      {
        message:
          "Le paiement n'est pas encore configuré sur cette démo (clés Stripe manquantes). Voir le README pour l'activer en production.",
      },
      { status: 200 }
    );
  }

  const session = await getServerSession(authOptions);
  const origin = request.headers.get("origin") ?? process.env.NEXT_PUBLIC_SITE_URL ?? "http://localhost:3000";

  const checkoutSession = await stripe.checkout.sessions.create({
    mode: "subscription",
    line_items: [{ price: priceId, quantity: 1 }],
    customer_email: session?.user?.email ?? undefined,
    success_url: `${origin}/tableau-de-bord?paiement=succes`,
    cancel_url: `${origin}/tarifs?paiement=annule`,
    metadata: { plan },
  });

  return NextResponse.json({ url: checkoutSession.url });
}
