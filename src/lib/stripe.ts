import Stripe from "stripe";

let stripeInstance: Stripe | null = null;

/**
 * Retourne un client Stripe initialisé, ou `null` si aucune clé n'est
 * configurée (mode démo / build sans variables d'environnement).
 */
export function getStripe(): Stripe | null {
  const key = process.env.STRIPE_SECRET_KEY;
  if (!key) return null;
  if (!stripeInstance) {
    stripeInstance = new Stripe(key);
  }
  return stripeInstance;
}

export const PLANS = {
  mensuel: {
    nom: "Mensuel",
    prix: "14,90 €",
    periode: "/ mois",
    priceEnvVar: "STRIPE_PRICE_MENSUEL",
  },
  annuel: {
    nom: "Annuel",
    prix: "119 €",
    periode: "/ an",
    priceEnvVar: "STRIPE_PRICE_ANNUEL",
  },
  famille: {
    nom: "Famille",
    prix: "24,90 €",
    periode: "/ mois",
    priceEnvVar: "STRIPE_PRICE_FAMILLE",
  },
} as const;

export type PlanId = keyof typeof PLANS;

// Produits à l'unité (paiement ponctuel, pas d'abonnement) : les packs de
// 6 examens blancs (Brevet / Bac), gratuits si l'élève a terminé le cycle
// correspondant sur la plateforme (voir src/lib/acces.ts).
export const PRODUCTS = {
  "brevet-pack": {
    nom: "Pack 6 Brevets blancs",
    prix: "8 €",
    priceEnvVar: "STRIPE_PRICE_BREVET_PACK",
  },
  "bac-pack": {
    nom: "Pack 6 Bacs blancs",
    prix: "8 €",
    priceEnvVar: "STRIPE_PRICE_BAC_PACK",
  },
} as const;

export type ProductId = keyof typeof PRODUCTS;
