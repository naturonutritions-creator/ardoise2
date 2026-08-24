import Link from "next/link";
import { Lock, Sparkles } from "lucide-react";

/**
 * Bandeau affiché à la place du contenu détaillé, des exercices et du quiz
 * d'une leçon lorsque l'utilisateur n'a pas (ou plus) accès au contenu complet :
 * essai gratuit de 7 jours expiré, ou pas d'abonnement actif. L'objectif,
 * le résumé et le premier paragraphe du cours restent visibles en aperçu.
 */
export default function AccessBanner({ isTrialExpired }: { isTrialExpired: boolean }) {
  return (
    <div className="mt-8 rounded-2xl border-2 border-corail-500/50 bg-corail-100 p-6 text-center sm:p-8">
      <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-corail-500/20">
        <Lock className="h-6 w-6 text-corail-600" />
      </div>
      <h3 className="mt-4 font-display text-lg font-semibold text-ardoise-900 sm:text-xl">
        {isTrialExpired
          ? "Ton essai gratuit de 7 jours est terminé"
          : "Cette leçon fait partie de l'abonnement Cap Réussite"}
      </h3>
      <p className="mx-auto mt-2 max-w-md text-sm text-ardoise-700">
        Abonne-toi pour débloquer le cours complet, les exercices et le quiz de cette leçon —
        et accéder à toutes les classes, du CP à la Terminale, pendant toute la durée de ton abonnement.
      </p>
      <Link
        href="/tarifs"
        className="mt-5 inline-flex items-center gap-2 rounded-full bg-corail-600 px-6 py-3 text-sm font-semibold text-white transition hover:bg-corail-500"
      >
        <Sparkles className="h-4 w-4" />
        Voir les abonnements
      </Link>
      {!isTrialExpired && (
        <p className="mt-3 text-xs text-ardoise-700/70">7 jours d&apos;essai gratuit, sans engagement.</p>
      )}
    </div>
  );
}
