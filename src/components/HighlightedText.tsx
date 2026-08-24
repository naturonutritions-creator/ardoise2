import React from "react";

// Repère les dates et périodes historiques dans un texte pour les mettre en
// surbrillance : années sur 4 chiffres (1789), années à 3-4 chiffres introduites
// par un mot déclencheur (« en 622 », « vers 800 », « l'an 800 »), et les siècles
// ou millénaires exprimés en chiffres romains (« XVIe siècle », « Ve millénaire »).
const YEAR_4 = "(?:1[0-9]{3}|20[0-9]{2})";
const TRIGGER_YEAR =
  "(?:[Ee]n|[Vv]ers|[Dd]ès|[Dd]epuis|[Jj]usqu['’]en|[Àà] partir de|[Ll]['’]an)\\s+\\d{3,4}";
const CENTURY =
  "(?:XXI|XX|XIX|XVIII|XVII|XVI|XV|XIV|XIII|XII|XI|X|IX|VIII|VII|VI|V|IV|III|II|I)e\\s+(?:siècles?|millénaires?)";

const DATE_PATTERN = `\\b(?:${TRIGGER_YEAR}|${YEAR_4}|${CENTURY})\\b`;

export default function HighlightedText({ text }: { text: string }) {
  const parts: React.ReactNode[] = [];
  let lastIndex = 0;
  let match: RegExpExecArray | null;
  let key = 0;

  const dateRegex = new RegExp(DATE_PATTERN, "g");
  while ((match = dateRegex.exec(text)) !== null) {
    if (match.index > lastIndex) {
      parts.push(text.slice(lastIndex, match.index));
    }
    parts.push(
      <mark
        key={key++}
        className="rounded bg-safran-100 px-1 py-0.5 font-semibold text-ardoise-900"
      >
        {match[0]}
      </mark>
    );
    lastIndex = match.index + match[0].length;
  }
  if (lastIndex < text.length) {
    parts.push(text.slice(lastIndex));
  }

  return <>{parts}</>;
}
