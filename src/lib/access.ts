import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";

/** Durée de l'essai gratuit offert à l'inscription, en jours. */
export const TRIAL_DAYS = 7;

export type AccessStatus = {
  /** Vrai si l'utilisateur peut accéder au contenu complet des leçons (essai en cours ou abonnement actif). */
  hasAccess: boolean;
  /** Vrai si l'accès est accordé au titre de l'essai gratuit (et non d'un abonnement payant). */
  isTrial: boolean;
  /** Vrai si l'utilisateur a un abonnement actif (Stripe). */
  isSubscribed: boolean;
  /** Vrai si l'utilisateur est connecté mais que son essai est terminé et qu'il n'a pas d'abonnement actif. */
  isTrialExpired: boolean;
  /** Date de fin de l'essai gratuit pour cet utilisateur (7 jours après l'inscription), ou null si non connecté. */
  trialEndsAt: Date | null;
};

const NO_ACCESS: AccessStatus = {
  hasAccess: false,
  isTrial: false,
  isSubscribed: false,
  isTrialExpired: false,
  trialEndsAt: null,
};

/**
 * Détermine si l'utilisateur actuellement connecté a accès à l'ensemble du
 * contenu pédagogique (toutes les classes, du CP à la Terminale) :
 *
 * - Un compte tout juste créé bénéficie d'un essai gratuit de 7 jours avec
 *   accès complet, sans carte bancaire ni abonnement.
 * - Passé ce délai, l'accès complet nécessite un abonnement actif (Stripe) —
 *   quel que soit le niveau de l'enfant inscrit, un abonnement actif donne
 *   accès à toutes les classes pendant toute sa durée.
 * - Un visiteur non connecté n'a jamais accès au contenu complet : il doit
 *   d'abord créer un compte pour démarrer son essai gratuit.
 *
 * En l'absence de base de données configurée (environnement de démonstration),
 * l'accès reste ouvert pour ne pas bloquer la navigation de démo.
 */
export async function getAccessStatus(): Promise<AccessStatus> {
  const session = await getServerSession(authOptions);
  const rawId = (session?.user as { id?: string } | undefined)?.id;
  const userId = rawId ? Number(rawId) : null;

  if (!userId || Number.isNaN(userId)) {
    return NO_ACCESS;
  }

  try {
    const [user] = await db
      .select({ createdAt: schema.users.createdAt })
      .from(schema.users)
      .where(eq(schema.users.id, userId))
      .limit(1);

    if (!user) return NO_ACCESS;

    const trialEndsAt = new Date(user.createdAt);
    trialEndsAt.setDate(trialEndsAt.getDate() + TRIAL_DAYS);
    const isTrial = new Date() < trialEndsAt;

    const [subscription] = await db
      .select({
        status: schema.subscriptions.status,
        currentPeriodEnd: schema.subscriptions.currentPeriodEnd,
      })
      .from(schema.subscriptions)
      .where(eq(schema.subscriptions.userId, userId))
      .limit(1);

    const isSubscribed =
      !!subscription &&
      (subscription.status === "active" || subscription.status === "trialing") &&
      (!subscription.currentPeriodEnd || new Date(subscription.currentPeriodEnd) > new Date());

    const hasAccess = isTrial || isSubscribed;

    return {
      hasAccess,
      isTrial: isTrial && !isSubscribed,
      isSubscribed,
      isTrialExpired: !isTrial && !isSubscribed,
      trialEndsAt,
    };
  } catch {
    // Base de données non configurée sur cette démo : on ne bloque pas la navigation.
    return { hasAccess: true, isTrial: false, isSubscribed: false, isTrialExpired: false, trialEndsAt: null };
  }
}
