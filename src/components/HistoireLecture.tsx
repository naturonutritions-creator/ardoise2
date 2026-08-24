"use client";

import { BookOpenText } from "lucide-react";
import ReadAloud from "@/components/ReadAloud";

/**
 * Petite histoire à écouter, construite à partir du vocabulaire et des
 * phrases déjà découverts dans la leçon. Remplace l'ancien exercice
 * "écoute l'intonation" (question / affirmation / exclamation), jugé trop
 * difficile pour bien progresser en langue : ici, l'enfant lit et écoute
 * un texte court et cohérent plutôt que de deviner un type de phrase.
 */
export default function HistoireLecture({
  histoire,
  lang = "fr-FR",
}: {
  histoire?: { titre: string; texte: string };
  lang?: string;
}) {
  if (!histoire) return null;

  return (
    <div className="mt-6 rounded-2xl border border-safran-500/30 bg-safran-100 p-6">
      <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
        <h3 className="flex items-center gap-2 font-display text-sm font-semibold text-ardoise-900">
          <BookOpenText className="h-4 w-4 text-safran-600" />
          {histoire.titre}
        </h3>
        <ReadAloud text={histoire.texte} label="Écouter l'histoire" lang={lang} className="bg-white" />
      </div>
      <p className="mt-2 leading-relaxed text-ardoise-800">{histoire.texte}</p>
    </div>
  );
}
