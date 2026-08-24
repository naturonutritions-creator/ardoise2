"use client";

import { useState } from "react";
import Logo from "@/components/Logo";
import { Printer } from "lucide-react";
import type { Niveau } from "@/content/curriculum";

function anneeScolaire(): string {
  const now = new Date();
  const year = now.getFullYear();
  const month = now.getMonth() + 1; // 1-12
  // L'année scolaire commence en septembre
  const debut = month >= 9 ? year : year - 1;
  return `${debut}-${debut + 1}`;
}

export default function DiplomaCertificate({ niveau }: { niveau: Niveau }) {
  const [nom, setNom] = useState("");
  const annee = anneeScolaire();

  return (
    <div>
      <div className="print-hide mb-8 flex flex-col gap-3 rounded-2xl border border-ardoise-900/10 bg-white p-6 sm:flex-row sm:items-end sm:justify-between">
        <div className="flex-1">
          <label htmlFor="nom-eleve" className="text-sm font-semibold text-ardoise-900">
            Prénom et nom de l&apos;élève
          </label>
          <input
            id="nom-eleve"
            type="text"
            value={nom}
            onChange={(e) => setNom(e.target.value)}
            placeholder="Ex : Léa Martin"
            className="mt-2 w-full rounded-lg border border-ardoise-900/20 px-4 py-2.5 text-ardoise-900 outline-none focus:border-corail-500"
          />
        </div>
        <button
          type="button"
          onClick={() => window.print()}
          className="inline-flex items-center justify-center gap-2 rounded-full bg-corail-500 px-5 py-2.5 text-sm font-semibold text-white shadow-sm transition-colors hover:bg-corail-600"
        >
          <Printer className="h-4 w-4" />
          Imprimer / Télécharger en PDF
        </button>
      </div>

      <div className="print-diploma relative overflow-hidden rounded-2xl border-4 border-double border-safran-500 bg-craie p-10 shadow-lg sm:p-16">
        <div className="chalk-texture pointer-events-none absolute inset-0 opacity-40" />
        <div className="relative flex flex-col items-center text-center">
          <Logo className="h-14 w-14" />
          <p className="mt-4 font-display text-sm font-semibold uppercase tracking-[0.3em] text-corail-600">
            Cap Réussite — reussifr
          </p>
          <h1 className="mt-6 font-display text-4xl font-semibold text-ardoise-900 sm:text-5xl">
            Diplôme de fin d&apos;année
          </h1>
          <p className="mt-2 text-sm uppercase tracking-widest text-ardoise-700/60">
            Année scolaire {annee}
          </p>

          <p className="mt-10 text-lg text-ardoise-700">Ce diplôme est fièrement décerné à</p>
          <p className="mt-3 min-h-[3rem] border-b-2 border-ardoise-900/20 px-8 pb-2 font-display text-3xl font-semibold text-corail-600 sm:text-4xl">
            {nom.trim() || "……………………………………"}
          </p>

          <p className="mt-10 max-w-xl text-ardoise-700">
            pour avoir travaillé avec sérieux et persévérance tout au long de son année de{" "}
            <span className="font-semibold text-ardoise-900">{niveau.nom}</span>, et validé
            avec succès les leçons et exercices de son programme scolaire.
          </p>

          <p className="mt-8 font-display text-lg italic text-ardoise-800">
            Bravo, et bonne continuation pour la suite !
          </p>

          <div className="mt-12 flex w-full max-w-md items-center justify-between text-sm text-ardoise-700/70">
            <div className="text-left">
              <p className="border-t border-ardoise-900/20 pt-2">Signature</p>
            </div>
            <div className="text-right">
              <p className="border-t border-ardoise-900/20 pt-2">Cap Réussite — reussifr.com</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
