import { notFound } from "next/navigation";
import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import { PROFIL_INFO } from "@/components/ProfilBadge";
import {
  adaptedLessonsByProfilNiveauMatiere,
  adaptedMatieresByProfilNiveau,
  adaptedNiveauxByProfil,
  type ProfilAdaptation,
} from "@/content/adaptations";
import { MATIERES, NIVEAUX } from "@/content/curriculum";
import { ArrowLeft, Clock } from "lucide-react";

const PROFILS: ProfilAdaptation[] = ["dyslexie", "dyscalculie"];

export function generateStaticParams() {
  const params: { profil: string; niveau: string; matiere: string }[] = [];
  for (const profil of PROFILS) {
    for (const niveau of adaptedNiveauxByProfil(profil)) {
      for (const matiere of adaptedMatieresByProfilNiveau(profil, niveau)) {
        params.push({ profil, niveau, matiere });
      }
    }
  }
  return params;
}

export default async function DysMatierePage({
  params,
}: {
  params: Promise<{ profil: string; niveau: string; matiere: string }>;
}) {
  const { profil: profilParam, niveau: niveauSlug, matiere: matiereSlug } = await params;
  if (!PROFILS.includes(profilParam as ProfilAdaptation)) notFound();
  const profil = profilParam as ProfilAdaptation;
  const niveau = NIVEAUX.find((n) => n.slug === niveauSlug);
  const matiere = MATIERES.find((m) => m.slug === matiereSlug);
  if (!niveau || !matiere) notFound();

  const info = PROFIL_INFO[profil];
  const lessons = adaptedLessonsByProfilNiveauMatiere(profil, niveau.slug, matiere.slug);

  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-16 text-craie">
          <Container>
            <Link
              href={`/dys/${profil}/${niveau.slug}`}
              className="inline-flex items-center gap-1 text-sm text-safran-500 hover:text-craie hover:underline"
            >
              <ArrowLeft className="h-3.5 w-3.5" />
              {niveau.nom}
            </Link>
            <h1 className="mt-3 font-display text-4xl font-semibold">
              {matiere.nom} — {niveau.nom}
            </h1>
            <p className="mt-3 max-w-2xl text-craie/80">
              Version {info.nom.toLowerCase()} des chapitres de {matiere.nom.toLowerCase()}.
            </p>
          </Container>
        </section>

        <section className="py-16">
          <Container>
            {lessons.length > 0 ? (
              <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                {lessons.map((lesson) => (
                  <Link
                    key={lesson.slug}
                    href={`/${profil}/${lesson.slug}`}
                    className="rounded-2xl border border-ardoise-900/10 bg-white p-5 shadow-sm transition-shadow hover:shadow-md"
                  >
                    <p className="font-display font-semibold text-ardoise-900">{lesson.titre}</p>
                    <p className="mt-2 line-clamp-2 text-sm text-ardoise-700/70">{lesson.resume}</p>
                    <p className="mt-3 flex items-center gap-1.5 text-xs text-ardoise-700/60">
                      <Clock className="h-3.5 w-3.5" />
                      {lesson.duree}
                    </p>
                  </Link>
                ))}
              </div>
            ) : (
              <p className="text-sm text-ardoise-700/60">Aucun chapitre disponible pour le moment.</p>
            )}
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
