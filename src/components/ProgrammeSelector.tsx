"use client";

import { useState } from "react";
import Link from "next/link";
import { clsx } from "clsx";
import { ArrowRight, Lock } from "lucide-react";
import MatiereIcon from "@/components/MatiereIcon";
import { lessonByNiveauMatiere } from "@/content/lessons";
import type { Niveau, Matiere } from "@/content/curriculum";

export default function ProgrammeSelector({
  niveaux,
  matieres,
}: {
  niveaux: Niveau[];
  matieres: Matiere[];
}) {
  const [selectedNiveau, setSelectedNiveau] = useState(niveaux[0]?.slug ?? "");

  return (
    <div>
      {/* Étape 1 : choisir la classe */}
      <p className="text-xs font-semibold uppercase tracking-wide text-ardoise-700/60">
        1. Choisis ta classe
      </p>
      <div className="mt-2 flex flex-wrap gap-2">
        {niveaux.map((n) => (
          <button
            key={n.slug}
            type="button"
            onClick={() => setSelectedNiveau(n.slug)}
            className={clsx(
              "rounded-full border px-4 py-1.5 text-sm font-medium transition-colors",
              selectedNiveau === n.slug
                ? "border-ardoise-900 bg-ardoise-900 text-craie"
                : "border-ardoise-900/15 bg-white text-ardoise-800 hover:border-ardoise-900/40"
            )}
          >
            {n.nom}
          </button>
        ))}
      </div>

      {/* Étape 2 : choisir la matière */}
      <p className="mt-6 text-xs font-semibold uppercase tracking-wide text-ardoise-700/60">
        2. Choisis ta matière
      </p>
      <div className="mt-2 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {matieres.map((m) => {
          const lesson = lessonByNiveauMatiere(selectedNiveau, m.slug);
          if (lesson) {
            return (
              <Link
                key={m.slug}
                href={`/cours/${m.slug}/${selectedNiveau}/${lesson.slug}`}
                className="group flex items-center gap-3 rounded-xl border border-ardoise-900/10 bg-white p-4 transition-all hover:-translate-y-0.5 hover:border-corail-500 hover:shadow-md"
              >
                <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-menthe-100 text-menthe-600">
                  <MatiereIcon nom={m.icone} className="h-4 w-4" />
                </div>
                <div className="min-w-0 flex-1">
                  <p className="text-sm font-medium text-ardoise-900">{m.nom}</p>
                  <p className="truncate text-xs text-ardoise-700/60">{lesson.titre}</p>
                </div>
                <ArrowRight className="h-4 w-4 shrink-0 text-ardoise-700/30 transition-transform group-hover:translate-x-1 group-hover:text-corail-600" />
              </Link>
            );
          }
          return (
            <div
              key={m.slug}
              className="flex items-center gap-3 rounded-xl border border-dashed border-ardoise-900/10 bg-ardoise-100/40 p-4 opacity-60"
            >
              <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-ardoise-100 text-ardoise-700/50">
                <MatiereIcon nom={m.icone} className="h-4 w-4" />
              </div>
              <div className="min-w-0 flex-1">
                <p className="text-sm font-medium text-ardoise-800">{m.nom}</p>
                <p className="text-xs text-ardoise-700/50">Bientôt disponible</p>
              </div>
              <Lock className="h-3.5 w-3.5 shrink-0 text-ardoise-700/30" />
            </div>
          );
        })}
      </div>
    </div>
  );
}
