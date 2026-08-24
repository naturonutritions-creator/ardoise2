import { NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { getStripe, PRODUCTS, type ProductId } from "@/lib/stripe";

export async function POST(request: Request) {
  const { product } = (await request.json()) as { product: ProductId };

  if (!product || !(product in PRODUCTS)) {
    return NextResponse.json({ message: "Produit inconnu." }, { status: 400 });
  }

  const session = await getServerSession(authOptions);
  if (!session?.user?.email) {
    return NextResponse.json(
      { message: "Connecte-toi d'abord pour acheter ce pack." },
      { status: 200 }
    );
  }

  const stripe = getStripe();
  const priceId = process.env[PRODUCTS[product].priceEnvVar];

  if (!stripe || !priceId) {
    return NextResponse.json(
      {
        message:
          "Le paiement n'est pas encore configuré sur cette démo (clés Stripe manquantes). Voir le README pour l'activer en production.",
      },
      { status: 200 }
    );
  }

  const origin = request.headers.get("origin") ?? process.env.NEXT_PUBLIC_SITE_URL ?? "http://localhost:3000";

  const checkoutSession = await stripe.checkout.sessions.create({
    mode: "payment",
    line_items: [{ price: priceId, quantity: 1 }],
    customer_email: session.user.email,
    success_url: `${origin}/examens?paiement=succes`,
    cancel_url: `${origin}/examens?paiement=annule`,
    metadata: { product },
  });

  return NextResponse.json({ url: checkoutSession.url });
}
