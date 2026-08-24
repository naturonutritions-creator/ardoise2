/**
 * Affiche une photo d'archive libre de droits insérée à un endroit précis du
 * contenu de la leçon (après un paragraphe donné, ou en intro), avec sa
 * mention de crédit obligatoire affichée sous l'image.
 */
export default function InlineContentImage({
  image,
}: {
  image?: { url: string; alt: string; credit: string; centre?: boolean };
}) {
  if (!image) return null;
  return (
    <figure
      className={`my-4 overflow-hidden rounded-2xl border border-ardoise-900/10 bg-white shadow-sm ${
        image.centre ? "mx-auto max-w-sm" : ""
      }`}
    >
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src={image.url} alt={image.alt} className="h-auto w-full object-contain bg-craie" loading="lazy" />
      <figcaption className="px-4 py-2 text-xs text-ardoise-700/60">{image.credit}</figcaption>
    </figure>
  );
}
