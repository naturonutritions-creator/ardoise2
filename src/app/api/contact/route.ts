import { NextResponse } from "next/server";
import { z } from "zod";

const schemaContact = z.object({
  name: z.string().min(2),
  email: z.string().email(),
  message: z.string().min(10),
});

export async function POST(request: Request) {
  const json = await request.json();
  const parsed = schemaContact.safeParse(json);

  if (!parsed.success) {
    return NextResponse.json({ message: "Formulaire invalide." }, { status: 400 });
  }

  // En production : envoyer un email (Resend, Postmark…) ou créer un ticket.
  // Ici, on se contente de confirmer la réception pour la démo.
  console.log("Nouveau message de contact :", parsed.data);

  return NextResponse.json({ message: "Message envoyé, merci !" }, { status: 200 });
}
