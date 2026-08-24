import AdaptedDetailPage from "@/components/AdaptedDetailPage";
import { adaptedLessonsByProfil } from "@/content/adaptations";

export function generateStaticParams() {
  return adaptedLessonsByProfil("dyscalculie").map((l) => ({ slug: l.slug }));
}

export default async function DyscalculieLessonPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  return <AdaptedDetailPage profil="dyscalculie" slug={slug} />;
}
