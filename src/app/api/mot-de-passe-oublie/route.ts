import { NextResponse } from "next/server";
import { z } from "zod";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";
import { createPasswordResetToken } from "@/lib/password-reset";
import { sendEmail } from "@/lib/mailer";

const schemaDemande = z.object({
  email: z.string().email("Adresse email invalide."),
});

// Message générique renvoyé dans tous les cas, pour ne jamais révéler si un email existe en base.
const REPONSE_GENERIQUE = {
  message: "Si un compte existe avec cet email, un lien de réinitialisation vient d'être envoyé.",
};

export async function POST(request: Request) {
  const json = await request.json();
  const parsed = schemaDemande.safeParse(json);

  if (!parsed.success) {
    return NextResponse.json(
      { message: parsed.error.issues[0]?.message ?? "Formulaire invalide." },
      { status: 400 }
    );
  }

  const emailLower = parsed.data.email.toLowerCase();

  try {
    const [user] = await db
      .select({ id: schema.users.id, name: schema.users.name })
      .from(schema.users)
      .where(eq(schema.users.email, emailLower))
      .limit(1);

    if (user) {
      const token = await createPasswordResetToken(user.id);
      const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || "http://localhost:3000";
      const lien = `${siteUrl}/reinitialiser-mot-de-passe/${token}`;

      await sendEmail(
        emailLower,
        "Réinitialise ton mot de passe — Cap Réussite",
        `<p>Bonjour ${user.name},</p>
         <p>Tu as demandé à réinitialiser ton mot de passe sur Cap Réussite.</p>
         <p><a href="${lien}">Clique ici pour choisir un nouveau mot de passe</a> (valable 1 heure).</p>
         <p>Si tu n'es pas à l'origine de cette demande, tu peux ignorer cet email.</p>`,
        `Bonjour ${user.name},\n\nTu as demandé à réinitialiser ton mot de passe sur Cap Réussite.\nClique sur ce lien pour choisir un nouveau mot de passe (valable 1 heure) :\n${lien}\n\nSi tu n'es pas à l'origine de cette demande, tu peux ignorer cet email.`
      );
    }

    // Toujours la même réponse, que l'email existe ou non.
    return NextResponse.json(REPONSE_GENERIQUE, { status: 200 });
  } catch {
    return NextResponse.json(
      {
        message:
          "Impossible de traiter la demande : la base de données n'est pas configurée sur cette démo (voir README).",
      },
      { status: 503 }
    );
  }
}
