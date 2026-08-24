import { db, schema } from "@/lib/db";
import { eq, and } from "drizzle-orm";
import { LESSONS } from "@/content/lessons";
import type { ProductId } from "@/lib/stripe";

/**
 * Niveaux couverts par chaque cycle d'examens blancs. Un élève qui a terminé
 * (100% des leçons marquées faites) tous les niveaux d'un cycle débloque
 * gratuitement le pack de 6 examens blancs correspondant.
 */
export const NIVEAUX_BREVET = ["6e", "5e", "4e", "3e"];
export const NIVEAUX_BAC = ["2nde", "1re", "terminale"];

export function niveauxDuPack(product: ProductId): string[] {
  return product === "brevet-pack" ? NIVEAUX_BREVET : NIVEAUX_BAC;
}

/**
 * Vrai si l'utilisateur a terminé (lessonDone = true) l'intégralité des
 * leçons de la plateforme pour les niveaux donnés.
 */
export async function aTermineLeCycle(userId: number, niveaux: string[]): Promise<boolean> {
  if (!userId || Number.isNaN(userId)) return false;

  const slugsAttendus = new Set(
    LESSONS.filter((l) => niveaux.includes(l.niveau)).map((l) => l.slug)
  );
  if (slugsAttendus.size === 0) return false;

  try {
    const progressions = await db
      .select({ lessonSlug: schema.progressions.lessonSlug, lessonDone: schema.progressions.lessonDone })
      .from(schema.progressions)
      .where(eq(schema.progressions.userId, userId));

    const doneSlugs = new Set(progressions.filter((p) => p.lessonDone).map((p) => p.lessonSlug));
    for (const slug of slugsAttendus) {
      if (!doneSlugs.has(slug)) return false;
    }
    return true;
  } catch {
    // Base de données non configurée sur cette démo.
    return false;
  }
}

/** Vrai si l'utilisateur a acheté le pack d'examens (achat ponctuel actif). */
export async function aAcheteLePack(userId: number, product: ProductId): Promise<boolean> {
  if (!userId || Number.isNaN(userId)) return false;
  try {
    const [purchase] = await db
      .select()
      .from(schema.purchases)
      .where(
        and(
          eq(schema.purchases.userId, userId),
          eq(schema.purchases.product, product),
          eq(schema.purchases.status, "active")
        )
      )
      .limit(1);
    return !!purchase;
  } catch {
    return false;
  }
}

/**
 * Vrai si l'utilisateur peut accéder au pack d'examens blancs : soit il l'a
 * acheté (8 €), soit il a terminé gratuitement tout le cycle correspondant
 * (6e à 3e pour le Brevet, 2nde à Terminale pour le Bac) sur la plateforme.
 */
export async function peutAccederAuPack(userId: number, product: ProductId): Promise<boolean> {
  const [achete, termine] = await Promise.all([
    aAcheteLePack(userId, product),
    aTermineLeCycle(userId, niveauxDuPack(product)),
  ]);
  return achete || termine;
}
