"use client";

import { useState } from "react";
import { Volume2, Check, X, RotateCcw } from "lucide-react";
import { clsx } from "clsx";
import type { SonExercice } from "@/content/lessons";
import { cleanForSpeech } from "@/lib/speech";

function speak(text: string) {
  if (typeof window === "undefined" || !("speechSynthesis" in window)) return;
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(cleanForSpeech(text));
  utterance.lang = "fr-FR";
  utterance.rate = 0.8;
  utterance.pitch = 1;
  window.speechSynthesis.speak(utterance);
}

function ExerciceItem({ exercice, index }: { exercice: SonExercice; index: number }) {
  const [selected, setSelected] = useState<number | null>(null);
  const isCorrect = selected !== null && selected === exercice.reponse;

  function handleChoice(i: number) {
    speak(exercice.propositions[i]);
    setSelected(i);
  }

  return (
    <div className="rounded-xl border border-ardoise-900/10 bg-white p-4">
      <div className="flex flex-wrap items-center gap-2">
        <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-menthe-100 text-xs font-semibold text-menthe-700">
          {index + 1}
        </span>
        <button
          type="button"
          onClick={() => speak(exercice.motReference)}
          className="inline-flex items-center gap-1.5 rounded-full border border-ardoise-900/20 bg-craie px-3 py-1.5 text-xs font-semibold text-ardoise-800 transition-colors hover:border-ardoise-900/40"
        >
          <Volume2 className="h-3.5 w-3.5" />
          Écouter « {exercice.motReference} »
        </button>
        <span className="text-xs text-ardoise-700/60">Clique sur le mot qui a le même son</span>
      </div>

      <div className="mt-3 flex flex-wrap gap-2">
        {exercice.propositions.map((mot, i) => {
          const isSelected = selected === i;
          const revealed = selected !== null;
          return (
            <button
              key={mot}
              type="button"
              onClick={() => handleChoice(i)}
              className={clsx(
                "rounded-lg border px-3 py-2 text-sm font-medium transition-colors",
                revealed && isSelected && i === exercice.reponse && "border-menthe-500 bg-menthe-100 text-menthe-700",
                revealed && isSelected && i !== exercice.reponse && "border-corail-500 bg-corail-100 text-corail-600",
                !isSelected && "border-ardoise-900/15 bg-white text-ardoise-800 hover:border-ardoise-900/40"
              )}
            >
              {mot}
              {revealed && isSelected && (i === exercice.reponse ? (
                <Check className="ml-1 inline h-3.5 w-3.5" />
              ) : (
                <X className="ml-1 inline h-3.5 w-3.5" />
              ))}
            </button>
          );
        })}
      </div>

      {selected !== null && (
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <p className={clsx("text-xs font-medium", isCorrect ? "text-menthe-600" : "text-corail-600")}>
            {isCorrect
              ? `Bravo ! « ${exercice.propositions[selected]} » a bien le même son que « ${exercice.motReference} ».`
              : `Pas tout à fait. Le bon mot était « ${exercice.propositions[exercice.reponse]} ». Réessaie !`}
          </p>
          <button
            type="button"
            onClick={() => setSelected(null)}
            className="inline-flex items-center gap-1 text-xs font-medium text-ardoise-700/60 hover:text-ardoise-900"
          >
            <RotateCcw className="h-3 w-3" />
            Réessayer
          </button>
        </div>
      )}
    </div>
  );
}

/**
 * Exercice d'écoute active : l'enfant écoute un mot de référence puis clique
 * sur celui, parmi plusieurs proposés, qui contient le même son. L'enfant
 * "entre" ainsi sa réponse en cliquant, sans clavier — adapté au CE1.
 */
export default function SonMatch({ exercices }: { exercices?: SonExercice[] }) {
  if (!exercices || exercices.length === 0) return null;

  return (
    <div className="mt-6">
      <h3 className="font-display text-sm font-semibold uppercase tracking-wide text-ardoise-700/70">
        Entraîne ton oreille : trouve le bon son
      </h3>
      <div className="mt-3 space-y-3">
        {exercices.map((ex, i) => (
          <ExerciceItem key={`${ex.motReference}-${i}`} exercice={ex} index={i} />
        ))}
      </div>
    </div>
  );
}
