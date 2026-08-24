"use client";

import { Ear } from "lucide-react";
import ReadAloud from "@/components/ReadAloud";

export default function AlphabetAEcouter({
  lettres,
  lang,
}: {
  lettres?: { lettre: string; nomEtranger: string }[];
  lang: string;
}) {
  if (!lettres || lettres.length === 0) return null;

  return (
    <div className="rounded-2xl border border-menthe-500/30 bg-menthe-100 p-6">
      <h3 className="flex items-center gap-2 font-display text-sm font-semibold text-ardoise-900">
        <Ear className="h-4 w-4 text-menthe-600" />
        Écoute l&apos;alphabet
      </h3>
      <p className="mt-1 text-xs text-ardoise-700/70">
        Clique sur une lettre pour l&apos;entendre dans la langue du cours, puis en français.
      </p>
      <div className="mt-3 flex flex-wrap gap-2">
        {lettres.map((l) => (
          <ReadAloud
            key={l.lettre}
            text={l.nomEtranger}
            secondText={l.lettre}
            secondLang="fr-FR"
            label={l.lettre.toUpperCase()}
            className="bg-white"
            lang={lang}
          />
        ))}
      </div>
    </div>
  );
}
