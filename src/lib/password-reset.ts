import crypto from "crypto";
import { eq, and, isNull, gt } from "drizzle-orm";
import { db, schema } from "@/lib/db";

const TOKEN_TTL_MS = 60 * 60 * 1000; // 1 heure

function hashToken(token: string) {
  return crypto.createHash("sha256").update(token).digest("hex");
}

/** Crée un token de réinitialisation en clair (à mettre dans le lien envoyé par email) et stocke son empreinte SHA-256 en base. */
export async function createPasswordResetToken(userId: number) {
  const token = crypto.randomBytes(32).toString("hex");
  const tokenHash = hashToken(token);
  const expiresAt = new Date(Date.now() + TOKEN_TTL_MS);

  await db.insert(schema.passwordResetTokens).values({ userId, tokenHash, expiresAt });

  return token;
}

/** Vérifie qu'un token en clair est valide (existe, non expiré, non déjà utilisé) et renvoie l'utilisateur associé, sans le consommer. */
export async function findValidResetToken(token: string) {
  const tokenHash = hashToken(token);
  const [row] = await db
    .select()
    .from(schema.passwordResetTokens)
    .where(
      and(
        eq(schema.passwordResetTokens.tokenHash, tokenHash),
        isNull(schema.passwordResetTokens.usedAt),
        gt(schema.passwordResetTokens.expiresAt, new Date())
      )
    )
    .limit(1);
  return row ?? null;
}

/** Marque un token comme utilisé, pour empêcher toute réutilisation du même lien. */
export async function consumeResetToken(tokenId: number) {
  await db
    .update(schema.passwordResetTokens)
    .set({ usedAt: new Date() })
    .where(eq(schema.passwordResetTokens.id, tokenId));
}
