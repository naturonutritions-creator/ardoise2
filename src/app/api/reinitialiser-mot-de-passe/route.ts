import { NextResponse } from "next/server";
import bcrypt from "bcryptjs";
import { z } from "zod";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";
import { findValidResetToken, consumeResetToken } from "@/lib/password-reset";

const schemaReset = z.object({
  token: z.string().min(1, "Lien invalide."),
  password: z.string().min(8, "Le mot de passe doit contenir au moins 8 caractères."),
});

export async function POST(request: Request) {
  const json = await request.json();
  const parsed = schemaReset.safeParse(json);

  if (!parsed.success) {
    return NextResponse.json(
      { message: parsed.error.issues[0]?.message ?? "Formulaire invalide." },
      { status: 400 }
    );
  }

  const { token, password } = parsed.data;

  try {
    const resetToken = await findValidResetToken(token);

    if (!resetToken) {
      return NextResponse.json(
        { message: "Ce lien de réinitialisation est invalide ou a expiré. Refais une demande." },
        { status: 400 }
      );
    }

    const passwordHash = await bcrypt.hash(password, 10);

    await db
      .update(schema.users)
      .set({ passwordHash })
      .where(eq(schema.users.id, resetToken.userId));

    await consumeResetToken(resetToken.id);

    return NextResponse.json({ message: "Mot de passe mis à jour avec succès." }, { status: 200 });
  } catch {
    return NextResponse.json(
      {
        message:
          "Impossible de réinitialiser le mot de passe : la base de données n'est pas configurée sur cette démo (voir README).",
      },
      { status: 503 }
    );
  }
}
