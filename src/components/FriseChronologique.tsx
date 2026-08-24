import type { FriseEvenement } from "@/content/lessons";
import { Star } from "lucide-react";

export default function FriseChronologique({ evenements }: { evenements: FriseEvenement[] }) {
  if (!evenements || evenements.length === 0) return null;

  return (
    <div className="rounded-2xl border border-ardoise-900/10 bg-white p-6 shadow-sm">
      <h2 className="flex items-center gap-2 font-display text-lg font-semibold text-ardoise-900">
        Frise chronologique
      </h2>
      <ol className="relative mt-6 ml-3 border-l-2 border-ardoise-900/10 pl-6">
        {evenements.map((ev, i) => (
          <li key={i} className="relative pb-8 last:pb-0">
            <span
              className={`absolute -left-[calc(1.5rem+7px)] top-1 flex h-4 w-4 items-center justify-center rounded-full ring-4 ring-white ${
                ev.important ? "bg-corail-500" : "bg-menthe-500"
              }`}
            >
              {ev.important && <Star className="h-2.5 w-2.5 text-white" fill="currentColor" />}
            </span>
            <p
              className={`font-display text-sm font-bold ${
                ev.important ? "text-corail-600" : "text-ardoise-800"
              }`}
            >
              {ev.date}
            </p>
            <p className="mt-0.5 font-semibold text-ardoise-900">{ev.titre}</p>
            {ev.description && (
              <p className="mt-1 text-sm leading-relaxed text-ardoise-700/80">{ev.description}</p>
            )}
          </li>
        ))}
      </ol>
    </div>
  );
}
