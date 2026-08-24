"use client";

import { useState } from "react";
import { CheckCircle2, XCircle, PencilLine } from "lucide-react";
import { clsx } from "clsx";
import type { QuizQuestion } from "@/content/lessons";
import ReadAloud from "@/components/ReadAloud";

/**
 * Mini-exercices d'entraînement, distincts du quiz principal : chaque
 * réponse est corrigée immédiatement (pas de score global, pas de bouton
 * "valider" à la fin), pour permettre à l'enfant de s'entraîner autant de
 * fois qu'il le souhaite avant d'aborder le quiz noté.
 */
function ExerciceItem({
  exercice,
  index,
  avecAudio,
  lang,
}: {
  exercice: QuizQuestion;
  index: number;
  avecAudio: boolean;
  lang: string;
}) {
  const [selected, setSelected] = useState<number | null>(null);
  const isCorrect = selected !== null && selected === exercice.reponse;

  return (
    <div className="rounded-xl border border-ardoise-900/10 bg-white p-4">
      <div className="mb-2 flex flex-wrap items-start justify-between gap-2">
        <p className="text-sm font-medium text-ardoise-900">
          <span className="mr-1.5 inline-flex h-5 w-5 items-center justify-center rounded-full bg-safran-100 text-xs font-semibold text-safran-700">
            {index + 1}
          </span>
          {exercice.enonce}
        </p>
        <ReadAloud text={exercice.enonce} label="Écouter" className="!px-2 !py-1 text-[11px]" lang="fr-FR" />
      </div>
      <div className="grid gap-2 sm:grid-cols-2">
        {exercice.choix.map((choix, ci) => {
          const isChosen = selected === ci;
          const revealed = selected !== null;
          return (
            <div
              key={ci}
              className={clsx(
                "flex items-center gap-1.5 rounded-lg border pr-1.5 text-left text-sm transition-colors",
                revealed && ci === exercice.reponse && "border-menthe-500 bg-menthe-100",
                revealed && isChosen && ci !== exercice.reponse && "border-corail-500 bg-corail-100",
                !revealed && "border-ardoise-900/15 hover:border-ardoise-900/40"
              )}
            >
              <button
                type="button"
                onClick={() => setSelected(ci)}
                className="flex flex-1 items-center justify-between px-3 py-2"
              >
                <span>{choix}</span>
                {revealed && ci === exercice.reponse && <CheckCircle2 className="h-4 w-4 text-menthe-600" />}
                {revealed && isChosen && ci !== exercice.reponse && <XCircle className="h-4 w-4 text-corail-600" />}
              </button>
              {avecAudio && (
                <ReadAloud text={choix} label="" className="!gap-0 shrink-0 !rounded-full !border-0 !bg-transparent !px-1.5 !py-1.5" lang={lang} />
              )}
            </div>
          );
        })}
      </div>
      {selected !== null && (
        <p className={clsx("mt-2 text-xs font-medium", isCorrect ? "text-menthe-600" : "text-corail-600")}>
          {isCorrect ? "Bravo, c'est la bonne réponse !" : exercice.explication}
        </p>
      )}
    </div>
  );
}

export default function ExercicesSupplementaires({
  exercices,
  avecAudio = false,
  lang = "fr-FR",
}: {
  exercices?: QuizQuestion[];
  avecAudio?: boolean;
  lang?: string;
}) {
  if (!exercices || exercices.length === 0) return null;

  return (
    <div className="mt-6">
      <h3 className="flex items-center gap-2 font-display text-sm font-semibold uppercase tracking-wide text-ardoise-700/70">
        <PencilLine className="h-4 w-4" />
        Exercices supplémentaires
      </h3>
      <div className="mt-3 space-y-3">
        {exercices.map((ex, i) => (
          <ExerciceItem key={ex.id} exercice={ex} index={i} avecAudio={avecAudio} lang={lang} />
        ))}
      </div>
    </div>
  );
}
