import { NextResponse } from "next/server";
import bcrypt from "bcryptjs";
import { z } from "zod";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";

const schemaInscription = z.object({
  name: z.string().min(2, "Le nom doit contenir au moins 2 caractères."),
  email: z.string().email("Adresse email invalide."),
  password: z.string().min(8, "Le mot de passe doit contenir au moins 8 caractères."),
});

export async function POST(request: Request) {
  const json = await request.json();
  const parsed = schemaInscription.safeParse(json);

  if (!parsed.success) {
    return NextResponse.json(
      { message: parsed.error.issues[0]?.message ?? "Formulaire invalide." },
      { status: 400 }
    );
  }

  const { name, email, password } = parsed.data;
  const emailLower = email.toLowerCase();

  try {
    const [existing] = await db
      .select({ id: schema.users.id })
      .from(schema.users)
      .where(eq(schema.users.email, emailLower))
      .limit(1);

    if (existing) {
      return NextResponse.json({ message: "Un compte existe déjà avec cet email." }, { status: 409 });
    }

    const passwordHash = await bcrypt.hash(password, 10);

    await db.insert(schema.users).values({
      name,
      email: emailLower,
      passwordHash,
    });

    return NextResponse.json({ message: "Compte créé avec succès." }, { status: 201 });
  } catch {
    return NextResponse.json(
      {
        message:
          "Impossible de créer le compte : la base de données n'est pas configurée sur cette démo (voir README).",
      },
      { status: 503 }
    );
  }
}
