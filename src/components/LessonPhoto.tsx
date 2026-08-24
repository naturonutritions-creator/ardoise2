/**
 * Affiche une photo/portrait d'archive libre de droits (domaine public ou licence
 * libre, hébergée sur Wikimedia Commons) associée à la leçon, avec sa mention de
 * crédit obligatoire affichée sous l'image.
 */
export default function LessonPhoto({
  photo,
}: {
  photo?: { url: string; alt: string; credit: string };
}) {
  if (!photo) return null;
  return (
    <figure className="mt-6 overflow-hidden rounded-2xl border border-ardoise-900/10 bg-white shadow-sm">
      {/* Image d'archive externe (Wikimedia Commons) : balise <img> standard,
          pas de next/image, pour éviter toute config de domaine distant. */}
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src={photo.url} alt={photo.alt} className="h-auto w-full object-contain bg-craie" loading="lazy" />
      <figcaption className="px-4 py-2 text-xs text-ardoise-700/60">{photo.credit}</figcaption>
    </figure>
  );
}
