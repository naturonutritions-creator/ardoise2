/**
 * Affiche un schéma SVG inline fourni par le contenu de la leçon (lesson.illustration).
 * Le SVG est écrit à la main dans le contenu pédagogique (src/content/lessons.ts),
 * il n'y a donc aucune source externe ni upload utilisateur à assainir ici.
 */
export default function LessonIllustration({ svg }: { svg?: string }) {
  if (!svg) return null;
  return (
    <div className="mt-6 overflow-hidden rounded-2xl border border-ardoise-900/10 bg-white p-4 shadow-sm">
      <div
        className="mx-auto w-full max-w-md [&_svg]:mx-auto [&_svg]:h-auto [&_svg]:w-full"
        dangerouslySetInnerHTML={{ __html: svg }}
      />
    </div>
  );
}
