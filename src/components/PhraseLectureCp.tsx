"use client";

import { BookOpen } from "lucide-react";
import ReadAloud from "@/components/ReadAloud";

/**
 * Affiche des phrases faciles à lire pour le CP, avec les lettres muettes
 * finales des mots mises en évidence dans une couleur différente (grisée),
 * pour aider l'enfant à comprendre pourquoi on les écrit sans les
 * prononcer. La notation dans le contenu utilise des tildes : "cha~t~"
 * affiche "cha" en noir et "t" en gris.
 */
function renderPhrase(phrase: string) {
  const parts = phrase.split(/~([^~]*)~/g);
  // Après split avec un groupe capturant, les éléments d'indice impair sont
  // les portions marquées (lettres muettes), les indices pairs le reste.
  return parts.map((part, i) =>
    i % 2 === 1 ? (
      <span key={i} className="text-ardoise-400">
        {part}
      </span>
    ) : (
      <span key={i}>{part}</span>
    )
  );
}

export default function PhraseLectureCp({ phrases, lang = "fr-FR" }: { phrases?: string[]; lang?: string }) {
  if (!phrases || phrases.length === 0) return null;

  return (
    <div className="mt-6 rounded-2xl border border-menthe-500/30 bg-menthe-100 p-6">
      <h3 className="flex items-center gap-2 font-display text-sm font-semibold text-ardoise-900">
        <BookOpen className="h-4 w-4 text-menthe-600" />
        Je lis des phrases faciles
      </h3>
      <p className="mt-1 text-xs text-ardoise-700/70">
        Les lettres <span className="text-ardoise-400">grisées</span> ne s&apos;entendent pas : on les écrit,
        mais on ne les prononce pas.
      </p>
      <div className="mt-3 space-y-2">
        {phrases.map((phrase, i) => (
          <div key={i} className="flex items-center justify-between gap-2 rounded-xl bg-white px-4 py-3">
            <p className="text-base leading-relaxed text-ardoise-900">{renderPhrase(phrase)}</p>
            <ReadAloud text={phrase} className="shrink-0" lang={lang} />
          </div>
        ))}
      </div>
    </div>
  );
}
