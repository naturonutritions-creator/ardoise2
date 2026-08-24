"use client";

import { useState } from "react";
import { NotebookPen, CheckCircle2 } from "lucide-react";

export default function ResumeLectureBox({ show }: { show?: boolean }) {
  const [texte, setTexte] = useState("");
  const [envoye, setEnvoye] = useState(false);

  if (!show) return null;

  return (
    <div className="mt-8 rounded-2xl border-2 border-dashed border-menthe-500/50 bg-menthe-100 p-6">
      <h3 className="flex items-center gap-2 font-display text-sm font-semibold text-ardoise-900">
        <NotebookPen className="h-4 w-4 text-menthe-600" />
        À toi d&apos;écrire : ton résumé de lecture
      </h3>
      <p className="mt-1 text-xs text-ardoise-700/70">
        En quelques phrases, résume ce que tu as retenu de cette œuvre : l&apos;histoire, les personnages, ce que tu en as pensé.
      </p>
      <textarea
        value={texte}
        onChange={(e) => {
          setTexte(e.target.value);
          setEnvoye(false);
        }}
        rows={5}
        placeholder="Écris ton résumé ici..."
        className="mt-3 w-full rounded-xl border border-ardoise-900/15 bg-white p-3 text-sm text-ardoise-800 outline-none focus:border-menthe-500"
      />
      <div className="mt-3 flex items-center gap-3">
        <button
          type="button"
          onClick={() => texte.trim().length > 0 && setEnvoye(true)}
          className="rounded-full bg-menthe-600 px-4 py-1.5 text-xs font-semibold text-craie transition-colors hover:bg-menthe-500"
        >
          Envoyer mon résumé
        </button>
        {envoye && (
          <span className="flex items-center gap-1 text-xs font-medium text-menthe-600">
            <CheckCircle2 className="h-4 w-4" />
            Bravo, bien joué !
          </span>
        )}
      </div>
    </div>
  );
}
