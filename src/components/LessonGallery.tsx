/**
 * Affiche une galerie de plusieurs photos/illustrations d'archive libres de
 * droits (domaine public ou licence libre, Wikimedia Commons/Pixabay) associées
 * à la leçon, chacune avec sa mention de crédit obligatoire affichée sous l'image.
 */
export default function LessonGallery({
  galerie,
}: {
  galerie?: { url: string; alt: string; credit: string }[];
}) {
  if (!galerie || galerie.length === 0) return null;
  return (
    <div className="mt-6 grid gap-4 sm:grid-cols-2">
      {galerie.map((photo, i) => (
        <figure
          key={i}
          className="overflow-hidden rounded-2xl border border-ardoise-900/10 bg-white shadow-sm"
        >
          {/* Image d'archive : balise <img> standard, pas de next/image, pour
              éviter toute config de domaine distant. */}
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src={photo.url} alt={photo.alt} className="h-auto w-full object-contain bg-craie" loading="lazy" />
          <figcaption className="px-4 py-2 text-xs text-ardoise-700/60">{photo.credit}</figcaption>
        </figure>
      ))}
    </div>
  );
}
