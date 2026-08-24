"use client";

import { useState } from "react";
import { clsx } from "clsx";
import { CheckCircle2, XCircle } from "lucide-react";
import MatiereIcon from "@/components/MatiereIcon";
import ReadAloud from "@/components/ReadAloud";
import { MATIERES } from "@/content/curriculum";
import type { EvaluationTrimestrielle } from "@/content/evaluations";

export default function EvaluationPlayer({ evaluation }: { evaluation: EvaluationTrimestrielle }) {
  // Pour les plus jeunes lecteurs (CP, CE1), chaque réponse propose aussi
  // un bouton d'écoute, en plus de la question déjà lue à voix haute.
  const answersReadAloud = evaluation.niveau === "cp" || evaluation.niveau === "ce1";
  const [answers, setAnswers] = useState<Record<string, number>>({});
  const [submitted, setSubmitted] = useState(false);

  const allQuestions = evaluation.matieres.flatMap((m, mi) =>
    m.questions.map((q, qi) => ({ ...q, key: `${mi}-${qi}` }))
  );
  const total = allQuestions.length;
  const correct = allQuestions.filter((q) => answers[q.key] === q.reponse).length;

  function handleSubmit() {
    setSubmitted(true);
  }

  function reset() {
    setAnswers({});
    setSubmitted(false);
  }

  return (
    <div className="space-y-8">
      {submitted && (
        <div className="rounded-2xl border border-ardoise-900/10 bg-white p-6 text-center shadow-sm">
          <p className="font-display text-2xl font-semibold text-ardoise-900">
            {correct} / {total}
          </p>
          <p className="mt-1 text-sm text-ardoise-700/70">bonnes réponses sur l&apos;ensemble de l&apos;évaluation</p>
          <button
            type="button"
            onClick={reset}
            className="mt-4 rounded-full border border-ardoise-900/20 px-5 py-2 text-sm font-semibold text-ardoise-900 hover:bg-ardoise-100"
          >
            Recommencer
          </button>
        </div>
      )}

      {evaluation.matieres.map((matiereBloc, mi) => {
        const matiereInfo = MATIERES.find((m) => m.slug === matiereBloc.matiere);
        return (
          <div key={matiereBloc.matiere} className="rounded-2xl border border-ardoise-900/10 bg-white p-6 shadow-sm">
            <h3 className="mb-4 flex items-center gap-2 font-display text-lg font-semibold text-ardoise-900">
              {matiereInfo && <MatiereIcon nom={matiereInfo.icone} className="h-5 w-5 text-corail-500" />}
              {matiereInfo?.nom ?? matiereBloc.matiere}
            </h3>
            <div className="space-y-6">
              {matiereBloc.questions.map((q, qi) => {
                const key = `${mi}-${qi}`;
                const chosen = answers[key];
                return (
                  <div key={key}>
                    <div className="mb-2 flex flex-wrap items-start justify-between gap-2">
                      <p className="font-medium text-ardoise-900">
                        {qi + 1}. {q.enonce}
                      </p>
                      <ReadAloud text={q.enonce} label="Écouter" />
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
                              onClick={() => setAnswers((a) => ({ ...a, [key]: ci }))}
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
          </div>
        );
      })}

      {!submitted && (
        <button
          type="button"
          onClick={handleSubmit}
          disabled={Object.keys(answers).length < total}
          className="rounded-full bg-ardoise-900 px-6 py-3 text-sm font-semibold text-craie transition-colors hover:bg-ardoise-800 disabled:cursor-not-allowed disabled:opacity-40"
        >
          Valider l&apos;évaluation
        </button>
      )}
    </div>
  );
}
