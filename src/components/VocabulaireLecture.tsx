import { BookMarked } from "lucide-react";

export default function VocabulaireLecture({
  mots,
}: {
  mots?: { mot: string; definition: string }[];
}) {
  if (!mots || mots.length === 0) return null;

  return (
    <div className="mt-6 rounded-2xl border border-safran-500/30 bg-safran-100 p-6">
      <h3 className="flex items-center gap-2 font-display text-sm font-semibold text-ardoise-900">
        <BookMarked className="h-4 w-4 text-safran-500" />
        Vocabulaire à connaître
      </h3>
      <dl className="mt-3 space-y-2">
        {mots.map((m) => (
          <div key={m.mot} className="text-sm">
            <dt className="inline font-semibold text-ardoise-900">{m.mot}</dt>
            <dd className="inline text-ardoise-800"> — {m.definition}</dd>
          </div>
        ))}
      </dl>
    </div>
  );
}
