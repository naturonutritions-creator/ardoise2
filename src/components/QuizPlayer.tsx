"use client";

import { useState } from "react";
import type { Quiz } from "@/content/lessons";
import { CheckCircle2, XCircle, RotateCcw } from "lucide-react";
import { clsx } from "clsx";
import ReadAloud from "@/components/ReadAloud";

export default function QuizPlayer({
  quiz,
  lessonSlug,
  niveau,
}: {
  quiz: Quiz;
  lessonSlug: string;
  niveau?: string;
}) {
  // Pour les plus jeunes lecteurs (CP, CE1), chaque réponse propose aussi
  // un bouton d'écoute, en plus de la question déjà lue à voix haute.
  const answersReadAloud = niveau === "cp" || niveau === "ce1";
  const [answers, setAnswers] = useState<Record<string, number>>({});
  const [submitted, setSubmitted] = useState(false);
  const [saving, setSaving] = useState(false);

  const total = quiz.questions.length;
  const correct = quiz.questions.filter((q) => answers[q.id] === q.reponse).length;
  const score = submitted ? Math.round((correct / total) * 100) : null;

  async function handleSubmit() {
    setSubmitted(true);
    setSaving(true);
    try {
      await fetch(`/api/quiz/${quiz.slug}/submit`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          lessonSlug,
          score: Math.round(
            (quiz.questions.filter((q) => answers[q.id] === q.reponse).length / total) * 100
          ),
        }),
      });
    } catch {
      // Si l'utilisateur n'est pas connecté ou hors-ligne, on n'enregistre pas
      // le score côté serveur mais on affiche quand même le résultat.
    } finally {
      setSaving(false);
    }
  }

  function reset() {
    setAnswers({});
    setSubmitted(false);
  }

  return (
    <div className="rounded-2xl border border-ardoise-900/10 bg-white p-6 shadow-sm">
      <div className="mb-4 flex items-center justify-between">
        <h3 className="font-display text-lg font-semibold text-ardoise-900">{quiz.titre}</h3>
        {submitted && (
          <span
            className={clsx(
              "rounded-full px-3 py-1 text-sm font-semibold",
              score! >= 50 ? "bg-menthe-100 text-menthe-600" : "bg-corail-100 text-corail-600"
            )}
          >
            {correct}/{total} bonnes réponses
          </span>
        )}
      </div>

      <div className="space-y-6">
        {quiz.questions.map((q, qi) => {
          const chosen = answers[q.id];
          return (
            <div key={q.id}>
              <div className="mb-2 flex flex-wrap items-start justify-between gap-2">
                <p className="font-medium text-ardoise-900">
                  {qi + 1}. {q.enonce}
                </p>
                <ReadAloud text={q.enonce} label="Écouter la question" />
              </div>
              <div className="grid gap-2 sm:grid-cols-2">
                {q.choix.map((choix, ci) => {
                  const isChosen = chosen === ci;
                  const isCorrect = submitted && ci === q.reponse;
                  const isWrongChosen = submitted && isChosen && ci !== q.reponse;
                  return (
                    <div
                      key={ci}
                      className={clsx(
                        "flex items-center gap-1.5 rounded-xl border pr-1.5 text-left text-sm transition-colors",
                        !submitted && isChosen && "border-ardoise-900 bg-ardoise-100",
                        !submitted && !isChosen && "border-ardoise-900/15 hover:border-ardoise-900/40",
                        isCorrect && "border-menthe-500 bg-menthe-100",
                        isWrongChosen && "border-corail-500 bg-corail-100"
                      )}
                    >
                      <button
                        type="button"
                        disabled={submitted}
                        onClick={() => setAnswers((a) => ({ ...a, [q.id]: ci }))}
                        className="flex flex-1 items-center justify-between px-4 py-2.5"
                      >
                        <span>{choix}</span>
                        {isCorrect && <CheckCircle2 className="h-4 w-4 text-menthe-600" />}
                        {isWrongChosen && <XCircle className="h-4 w-4 text-corail-600" />}
                      </button>
                      {answersReadAloud && (
                        <ReadAloud
                          text={choix}
                          label=""
                          className="!gap-0 shrink-0 !rounded-full !border-0 !bg-transparent !px-1.5 !py-1.5"
                        />
                      )}
                    </div>
                  );
                })}
              </div>
              {submitted && (
                <p className="mt-2 text-sm text-ardoise-700">
                  <span className="font-semibold">Explication : </span>
                  {q.explication}
                </p>
              )}
            </div>
          );
        })}
      </div>

      <div className="mt-6 flex items-center gap-3">
        {!submitted ? (
          <button
            type="button"
            onClick={handleSubmit}
            disabled={Object.keys(answers).length < total}
            className="rounded-full bg-ardoise-900 px-5 py-2.5 text-sm font-semibold text-craie transition-colors hover:bg-ardoise-800 disabled:cursor-not-allowed disabled:opacity-40"
          >
            Valider mes réponses
          </button>
        ) : (
          <button
            type="button"
            onClick={reset}
            className="flex items-center gap-2 rounded-full border border-ardoise-900/20 px-5 py-2.5 text-sm font-semibold text-ardoise-900 hover:bg-ardoise-100"
          >
            <RotateCcw className="h-4 w-4" />
            Recommencer
          </button>
        )}
        {saving && <span className="text-xs text-ardoise-700/60">Enregistrement…</span>}
      </div>
    </div>
  );
}
