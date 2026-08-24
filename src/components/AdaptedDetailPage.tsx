import { notFound } from "next/navigation";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import QuizPlayer from "@/components/QuizPlayer";
import ReadAloud from "@/components/ReadAloud";
import SyncedReadAloud from "@/components/SyncedReadAloud";
import { PROFIL_INFO } from "@/components/ProfilBadge";
import { adaptedLessonBySlug, type ProfilAdaptation } from "@/content/adaptations";
import { MATIERES, NIVEAUX } from "@/content/curriculum";
import { Clock, Lightbulb } from "lucide-react";

export default function AdaptedDetailPage({
  profil,
  slug,
}: {
  profil: ProfilAdaptation;
  slug: string;
}) {
  const lesson = adaptedLessonBySlug(slug);
  if (!lesson || lesson.profil !== profil) notFound();

  const info = PROFIL_INFO[profil];
  const matiere = MATIERES.find((m) => m.slug === lesson.matiere);
  const niveau = NIVEAUX.find((n) => n.slug === lesson.niveau);

  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-14 text-craie">
          <Container>
            <div className="flex items-center gap-2 text-sm text-safran-500">
              <span>{info.nom}</span>
              <span className="text-craie/40">·</span>
              <span>{matiere?.nom}</span>
              <span className="text-craie/40">·</span>
              <span>{niveau?.nom}</span>
            </div>
            <h1 className="mt-3 font-display text-3xl font-semibold sm:text-4xl">{lesson.titre}</h1>
            <p className="mt-3 max-w-2xl text-craie/80">{lesson.resume}</p>
            <div className="mt-4 flex flex-wrap items-center gap-3 text-sm text-craie/60">
              <span className="flex items-center gap-2">
                <Clock className="h-4 w-4" />
                {lesson.duree}
              </span>
              <ReadAloud
                text={lesson.etapes.join(". ")}
                label="Écouter toute la leçon"
                className="border-craie/30 bg-craie/10 text-craie hover:border-craie/60"
              />
            </div>
          </Container>
        </section>

        <section className="py-14">
          <Container className="grid gap-10 lg:grid-cols-[2fr_1fr]">
            <div>
              <ol className="space-y-4">
                {lesson.etapes.map((etape, i) => (
                  <li
                    key={i}
                    className="flex gap-4 rounded-2xl border border-ardoise-900/10 bg-white p-5 shadow-sm"
                  >
                    <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-ardoise-900 font-display text-sm font-semibold text-craie">
                      {i + 1}
                    </span>
                    {profil === "dyslexie" ? (
                      <SyncedReadAloud text={etape} className="flex-1" textClassName="text-sm" />
                    ) : (
                      <div className="flex-1">
                        <p className="text-sm leading-relaxed text-ardoise-800">{etape}</p>
                        <ReadAloud
                          text={etape}
                          className="mt-2 !px-3 !py-1.5"
                        />
                      </div>
                    )}
                  </li>
                ))}
              </ol>

              <div className="mt-10">
                <QuizPlayer quiz={lesson.quiz} lessonSlug={lesson.slug} />
              </div>
            </div>

            <aside>
              <div className="rounded-2xl border border-safran-500/30 bg-safran-100 p-6">
                <h3 className="flex items-center gap-2 font-display text-sm font-semibold text-ardoise-900">
                  <Lightbulb className="h-4 w-4 text-safran-500" />
                  Conseils {info.nom}
                </h3>
                <ul className="mt-3 space-y-2">
                  {lesson.conseils.map((conseil, i) => (
                    <li key={i} className="text-sm leading-relaxed text-ardoise-800">
                      • {conseil}
                    </li>
                  ))}
                </ul>
              </div>
            </aside>
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
