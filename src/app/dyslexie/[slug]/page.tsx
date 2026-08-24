import AdaptedDetailPage from "@/components/AdaptedDetailPage";
import { adaptedLessonsByProfil } from "@/content/adaptations";

export function generateStaticParams() {
  return adaptedLessonsByProfil("dyslexie").map((l) => ({ slug: l.slug }));
}

export default async function DyslexieLessonPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  return <AdaptedDetailPage profil="dyslexie" slug={slug} />;
}
