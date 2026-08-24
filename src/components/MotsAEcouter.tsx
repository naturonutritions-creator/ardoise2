"use client";

import { Ear } from "lucide-react";
import ReadAloud from "@/components/ReadAloud";

export default function MotsAEcouter({ mots, lang = "fr-FR" }: { mots: string[]; lang?: string }) {
  return (
    <div className="rounded-2xl border border-menthe-500/30 bg-menthe-100 p-6">
      <h3 className="flex items-center gap-2 font-display text-sm font-semibold text-ardoise-900">
        <Ear className="h-4 w-4 text-menthe-600" />
        Écoute les mots
      </h3>
      <p className="mt-1 text-xs text-ardoise-700/70">
        Clique sur un mot pour l&apos;entendre et bien entraîner ton oreille.
      </p>
      <div className="mt-3 flex flex-wrap gap-2">
        {mots.map((mot) => (
          <ReadAloud key={mot} text={mot} label={mot} className="bg-white" lang={lang} />
        ))}
      </div>
    </div>
  );
}
