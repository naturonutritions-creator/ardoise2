"use client";

import { useState } from "react";
import { ChevronDown, Clock, Award } from "lucide-react";
import { clsx } from "clsx";
import type { ExamEpreuve } from "@/content/exams";

export default function ExamEpreuveCard({ epreuve }: { epreuve: ExamEpreuve }) {
  const [showCorrige, setShowCorrige] = useState(false);

  return (
    <div className="rounded-2xl border border-ardoise-900/10 bg-white p-6 shadow-sm">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <h3 className="font-display text-lg font-semibold text-ardoise-900">{epreuve.matiere}</h3>
        <div className="flex items-center gap-4 text-sm text-ardoise-700/70">
          <span className="flex items-center gap-1">
            <Clock className="h-4 w-4" /> {epreuve.duree}
          </span>
          <span className="flex items-center gap-1">
            <Award className="h-4 w-4" /> {epreuve.bareme}
          </span>
        </div>
      </div>

      <div className="mt-4 space-y-3">
        {epreuve.sujet.map((p, i) => (
          <p key={i} className="text-sm leading-relaxed text-ardoise-800">
            {p}
          </p>
        ))}
      </div>

      <button
        type="button"
        onClick={() => setShowCorrige((v) => !v)}
        className="mt-5 flex items-center gap-2 rounded-full border border-ardoise-900/20 px-4 py-2 text-sm font-semibold text-ardoise-900 hover:bg-ardoise-100"
      >
        <ChevronDown className={clsx("h-4 w-4 transition-transform", showCorrige && "rotate-180")} />
        {showCorrige ? "Masquer le corrigé" : "Afficher le corrigé"}
      </button>

      {showCorrige && (
        <div className="mt-4 space-y-3 rounded-xl bg-menthe-100 p-4">
          {epreuve.corrige.map((p, i) => (
            <p key={i} className="text-sm leading-relaxed text-ardoise-800">
              {p}
            </p>
          ))}
        </div>
      )}
    </div>
  );
}
