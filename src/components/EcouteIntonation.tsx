"use client";

import { useState } from "react";
import { Ear, Check, X } from "lucide-react";
import { clsx } from "clsx";
import type { IntonationExercice } from "@/content/lessons";
import { cleanForSpeech } from "@/lib/speech";

function speak(text: string, lang: string) {
  if (typeof window === "undefined" || !("speechSynthesis" in window)) return;
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(cleanForSpeech(text));
  utterance.lang = lang;
  utterance.rate = 0.8;
  utterance.pitch = 1;
  window.speechSynthesis.speak(utterance);
}

const TYPES: { value: IntonationExercice["type"]; label: string }[] = [
  { value: "affirmation", label: "Affirmation ." },
  { value: "question", label: "Question ?" },
  { value: "exclamation", label: "Exclamation !" },
];

function explication(type: IntonationExercice["type"]) {
  if (type === "question") return "une question (la voix monte à la fin de la phrase)";
  if (type === "exclamation") return "une exclamation (la voix est marquée, insistante)";
  return "une affirmation (la voix descend à la fin de la phrase)";
}

function ExerciceItem({
  exercice,
  index,
  lang,
}: {
  exercice: IntonationExercice;
  index: number;
  lang: string;
}) {
  const [choice, setChoice] = useState<IntonationExercice["type"] | null>(null);
  const isCorrect = choice === exercice.type;

  return (
    <div className="rounded-xl border border-ardoise-900/10 bg-white p-4">
      <div className="flex flex-wrap items-center gap-2">
        <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-safran-100 text-xs font-semibold text-safran-700">
          {index + 1}
        </span>
        <button
          type="button"
          onClick={() => speak(exercice.phrase, lang)}
          className="inline-flex items-center gap-1.5 rounded-full border border-ardoise-900/20 bg-craie px-3 py-1.5 text-xs font-semibold text-ardoise-800 transition-colors hover:border-ardoise-900/40"
        >
          <Ear className="h-3.5 w-3.5" />
          Écouter la phrase
        </button>
        <span className="text-xs text-ardoise-700/60">Quelle intonation entends-tu ?</span>
      </div>

      <div className="mt-3 flex flex-wrap gap-2">
        {TYPES.map((t) => {
          const isSelected = choice === t.value;
          const revealed = choice !== null;
          return (
            <button
              key={t.value}
              type="button"
              onClick={() => setChoice(t.value)}
              className={clsx(
                "rounded-lg border px-3 py-2 text-sm font-medium transition-colors",
                revealed && isSelected && t.value === exercice.type && "border-menthe-500 bg-menthe-100 text-menthe-700",
                revealed && isSelected && t.value !== exercice.type && "border-corail-500 bg-corail-100 text-corail-600",
                !isSelected && "border-ardoise-900/15 bg-white text-ardoise-800 hover:border-ardoise-900/40"
              )}
            >
              {t.label}
              {revealed && isSelected && (t.value === exercice.type ? (
                <Check className="ml-1 inline h-3.5 w-3.5" />
              ) : (
                <X className="ml-1 inline h-3.5 w-3.5" />
              ))}
            </button>
          );
        })}
      </div>

      {choice !== null && (
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <p className={clsx("text-xs font-medium", isCorrect ? "text-menthe-600" : "text-corail-600")}>
            {isCorrect
              ? `Bravo ! C'était bien ${explication(exercice.type)}.`
              : `Pas tout à fait — réécoute : c'était ${explication(exercice.type)}.`}
          </p>
          <button
            type="button"
            onClick={() => setChoice(null)}
            className="inline-flex items-center gap-1 text-xs font-medium text-ardoise-700/60 hover:text-ardoise-900"
          >
            Réessayer
          </button>
        </div>
      )}
    </div>
  );
}

/**
 * Exercice d'écoute active pour les langues vivantes : l'enfant écoute une
 * phrase lue par la synthèse vocale (avec la bonne intonation) et doit
 * deviner s'il s'agit d'une question, d'une affirmation ou d'une
 * exclamation, pour entraîner son oreille à la prosodie de la langue.
 */
export default function EcouteIntonation({
  exercices,
  lang,
}: {
  exercices?: IntonationExercice[];
  lang: string;
}) {
  if (!exercices || exercices.length === 0) return null;

  return (
    <div className="mt-6">
      <h3 className="font-display text-sm font-semibold uppercase tracking-wide text-ardoise-700/70">
        Écoute : reconnais la bonne intonation
      </h3>
      <p className="mt-1 text-xs text-ardoise-700/60">
        Écoute chaque phrase et devine si c&apos;est une question, une affirmation ou une exclamation.
      </p>
      <div className="mt-3 space-y-3">
        {exercices.map((ex, i) => (
          <ExerciceItem key={`${ex.phrase}-${i}`} exercice={ex} index={i} lang={lang} />
        ))}
      </div>
    </div>
  );
}
