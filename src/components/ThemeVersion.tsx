"use client";

import { useState } from "react";
import type { TexteTraduction } from "@/content/traduction";
import ReadAloud from "@/components/ReadAloud";

export default function ThemeVersion({
  texte,
  lang,
}: {
  texte: TexteTraduction;
  lang: string;
}) {
  const [sens, setSens] = useState<"theme" | "version">("theme");
  const [reveal, setReveal] = useState(false);

  const source = sens === "theme" ? texte.texteFR : texte.texteLangue;
  const cible = sens === "theme" ? texte.texteLangue : texte.texteFR;
  const sourceLang = sens === "theme" ? "fr-FR" : lang;
  const cibleLang = sens === "theme" ? lang : "fr-FR";

  return (
    <div>
      <div className="flex flex-wrap gap-2">
        <button
          type="button"
          onClick={() => {
            setSens("theme");
            setReveal(false);
          }}
          className={`rounded-full border px-4 py-2 text-sm font-medium transition-colors ${
            sens === "theme"
              ? "border-corail-600 bg-corail-600 text-white"
              : "border-ardoise-900/15 bg-white text-ardoise-800 hover:border-corail-400"
          }`}
        >
          Thème (français → langue)
        </button>
        <button
          type="button"
          onClick={() => {
            setSens("version");
            setReveal(false);
          }}
          className={`rounded-full border px-4 py-2 text-sm font-medium transition-colors ${
            sens === "version"
              ? "border-corail-600 bg-corail-600 text-white"
              : "border-ardoise-900/15 bg-white text-ardoise-800 hover:border-corail-400"
          }`}
        >
          Version (langue → français)
        </button>
      </div>

      <p className="mt-4 text-sm text-ardoise-700/70">
        {sens === "theme"
          ? "Traduis ce texte français dans la langue étrangère, puis vérifie ta traduction."
          : "Traduis ce texte étranger en français, puis vérifie ta traduction."}
      </p>

      <article className="mt-4 rounded-2xl border border-ardoise-900/10 bg-white p-6 shadow-sm">
        {source.map((p, i) => (
          <div key={i} className="mb-4 flex items-start gap-2 last:mb-0">
            <p className="leading-relaxed text-ardoise-800">{p}</p>
            <ReadAloud
              text={p}
              label="Écouter"
              className="mt-0.5 shrink-0 !px-2 !py-1 text-[11px]"
              lang={sourceLang}
            />
          </div>
        ))}
      </article>

      <button
        type="button"
        onClick={() => setReveal((r) => !r)}
        className="mt-4 rounded-full border border-menthe-500 bg-menthe-100 px-4 py-2 text-sm font-medium text-ardoise-900 hover:bg-menthe-200"
      >
        {reveal ? "Masquer la traduction modèle" : "Voir la traduction modèle"}
      </button>

      {reveal && (
        <article className="mt-4 rounded-2xl border border-menthe-500/30 bg-menthe-100 p-6">
          <h3 className="font-display text-sm font-semibold text-ardoise-900">
            Traduction modèle
          </h3>
          {cible.map((p, i) => (
            <div key={i} className="mt-3 flex items-start gap-2 first:mt-3">
              <p className="leading-relaxed text-ardoise-800">{p}</p>
              <ReadAloud
                text={p}
                label="Écouter"
                className="mt-0.5 shrink-0 !px-2 !py-1 text-[11px]"
                lang={cibleLang}
              />
            </div>
          ))}
        </article>
      )}

      {texte.vocabulaireAide && texte.vocabulaireAide.length > 0 && (
        <div className="mt-6 rounded-2xl border border-ardoise-900/10 bg-white p-6">
          <h3 className="font-display text-sm font-semibold text-ardoise-900">
            Vocabulaire utile
          </h3>
          <ul className="mt-3 grid gap-1.5 sm:grid-cols-2">
            {texte.vocabulaireAide.map((g) => (
              <li key={g.mot} className="text-sm text-ardoise-800">
                <span className="font-semibold">{g.mot}</span> — {g.traduction}
              </li>
            ))}
          </ul>
        </div>
      )}

      {texte.pointsAttention && texte.pointsAttention.length > 0 && (
        <div className="mt-6 rounded-2xl border border-safran-500/30 bg-safran-500/10 p-6">
          <h3 className="font-display text-sm font-semibold text-ardoise-900">
            Points d&apos;attention pour la traduction
          </h3>
          <ul className="mt-3 space-y-1.5">
            {texte.pointsAttention.map((p, i) => (
              <li key={i} className="text-sm text-ardoise-800">
                {p}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
