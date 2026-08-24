import AdaptedDetailPage from "@/components/AdaptedDetailPage";
import { adaptedLessonsByProfil } from "@/content/adaptations";

export function generateStaticParams() {
  return adaptedLessonsByProfil("tdah").map((l) => ({ slug: l.slug }));
}

export default async function TdahLessonPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  return <AdaptedDetailPage profil="tdah" slug={slug} />;
}
