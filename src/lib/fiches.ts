import type { Lesson } from "@/content/lessons";

const LANGUES = new Set(["anglais", "espagnol", "italien"]);
const CONJ_RE = /conjug|verbe|temps|présent|futur|passé|imparfait/i;

/** URL de la fiche mémo (carte mentale / frise / tableau) — disponible pour toutes les leçons. */
export function ficheMemoUrl(lesson: Pick<Lesson, "matiere" | "niveau" | "slug">): string {
  return `/fiches/memo/${lesson.matiere}/${lesson.niveau}/${lesson.slug}.pdf`;
}

/**
 * Vrai si une fiche d'exercices téléchargeable existe pour cette leçon :
 * français, mathématiques, ou conjugaison dans une langue étrangère.
 */
export function aDesExercices(lesson: Pick<Lesson, "matiere" | "titre">): boolean {
  if (lesson.matiere === "francais" || lesson.matiere === "mathematiques") return true;
  if (LANGUES.has(lesson.matiere) && CONJ_RE.test(lesson.titre)) return true;
  return false;
}

/** URL de la fiche d'exercices téléchargeable (avec corrigé) — ou `null` si non disponible. */
export function ficheExercicesUrl(lesson: Pick<Lesson, "matiere" | "niveau" | "slug" | "titre">): string | null {
  if (!aDesExercices(lesson)) return null;
  return `/fiches/exercices/${lesson.matiere}/${lesson.niveau}/${lesson.slug}.pdf`;
}
