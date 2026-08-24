import Link from "next/link";
import { notFound } from "next/navigation";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import MatiereIcon from "@/components/MatiereIcon";
import { CYCLES, matieresDuCycle, niveauxDuCycle, type Cycle } from "@/content/curriculum";
import { lessonsByNiveau } from "@/content/lessons";
import { TEXTES_COMPREHENSION } from "@/content/comprehension";
import { TEXTES_TRADUCTION } from "@/content/traduction";
import { BookOpenCheck, Languages, FileDown } from "lucide-react";

export function generateStaticParams() {
  return CYCLES.map((c) => ({ cycle: c.slug }));
}

export default async function CyclePage({ params }: { params: Promise<{ cycle: string }> }) {
  const { cycle: cycleSlug } = await params;
  const cycle = CYCLES.find((c) => c.slug === cycleSlug);
  if (!cycle) notFound();

  const niveaux = niveauxDuCycle(cycle.slug as Cycle);
  const matieres = matieresDuCycle(cycle.slug as Cycle);

  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-16 text-craie">
          <Container>
            <p className="text-sm font-medium text-safran-500">Programme</p>
            <h1 className="mt-2 font-display text-4xl font-semibold">{cycle.nom}</h1>
            <p className="mt-3 max-w-2xl text-craie/80">{cycle.description}</p>
          </Container>
        </section>

        <section className="py-16">
          <Container className="space-y-14">
            {niveaux.map((niveau) => {
              const lessons = lessonsByNiveau(niveau.slug);
              return (
                <div key={niveau.slug} id={niveau.slug} className="scroll-mt-24">
                  <div className="flex flex-wrap items-center justify-between gap-2">
                    <h2 className="font-display text-2xl font-semibold text-ardoise-900">{niveau.nom}</h2>
                    {niveau.slug === "cp" && (
                      <Link
                        href="/parcours-sons"
                        className="rounded-full border border-corail-500/40 bg-corail-100 px-3 py-1.5 text-xs font-semibold text-corail-600 transition-colors hover:bg-corail-200"
                      >
                        Voir le parcours des sons →
                      </Link>
                    )}
                  </div>
                  {lessons.length > 0 ? (
                    <div className="mt-4 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
                      {lessons.map((lesson) => {
                        const matiere = matieres.find((m) => m.slug === lesson.matiere);
                        return (
                          <Link
                            key={lesson.slug}
                            href={`/cours/${lesson.matiere}/${lesson.niveau}/${lesson.slug}`}
                            className="rounded-xl border border-ardoise-900/10 bg-white p-4 transition-shadow hover:shadow-md"
                          >
                            <div className="flex items-center gap-2 text-xs font-medium text-corail-600">
                              {matiere && <MatiereIcon nom={matiere.icone} className="h-3.5 w-3.5" />}
                              {matiere?.nom}
                            </div>
                            <p className="mt-2 font-semibold text-ardoise-900">{lesson.titre}</p>
                            <p className="mt-1 text-xs text-ardoise-700/70">{lesson.duree}</p>
                          </Link>
                        );
                      })}
                    </div>
                  ) : (
                    <p className="mt-3 text-sm text-ardoise-700/60">
                      De nouvelles leçons pour ce niveau arrivent bientôt.
                    </p>
                  )}

                  {lessons.length > 0 && (
                    <div className="mt-4 flex flex-wrap gap-2">
                      <Link
                        href={`/fiches/${niveau.slug}`}
                        className="inline-flex items-center gap-1.5 rounded-full border border-menthe-500/40 bg-menthe-100 px-3 py-1.5 text-xs font-semibold text-ardoise-800 hover:border-menthe-500"
                      >
                        <FileDown className="h-3.5 w-3.5" />
                        Fiches mémo & exercices
                      </Link>
                    </div>
                  )}

                  {(() => {
                    const langues = Array.from(
                      new Set(
                        TEXTES_COMPREHENSION.filter((t) => t.niveau === niveau.slug).map((t) => t.matiere)
                      )
                    );
                    if (langues.length === 0) return null;
                    return (
                      <div className="mt-4 flex flex-wrap gap-2">
                        {langues.map((matiereSlug) => {
                          const m = matieres.find((mm) => mm.slug === matiereSlug);
                          return (
                            <Link
                              key={matiereSlug}
                              href={`/comprehension/${matiereSlug}/${niveau.slug}`}
                              className="inline-flex items-center gap-1.5 rounded-full border border-corail-500/40 bg-corail-100 px-3 py-1.5 text-xs font-semibold text-corail-700 hover:border-corail-500"
                            >
                              <BookOpenCheck className="h-3.5 w-3.5" />
                              Compréhension de texte — {m?.nom ?? matiereSlug}
                            </Link>
                          );
                        })}
                      </div>
                    );
                  })()}

                  {(() => {
                    const languesTrad = Array.from(
                      new Set(
                        TEXTES_TRADUCTION.filter((t) => t.niveau === niveau.slug).map((t) => t.matiere)
                      )
                    );
                    if (languesTrad.length === 0) return null;
                    return (
                      <div className="mt-2 flex flex-wrap gap-2">
                        {languesTrad.map((matiereSlug) => {
                          const m = matieres.find((mm) => mm.slug === matiereSlug);
                          return (
                            <Link
                              key={matiereSlug}
                              href={`/traduction/${matiereSlug}/${niveau.slug}`}
                              className="inline-flex items-center gap-1.5 rounded-full border border-menthe-500/40 bg-menthe-100 px-3 py-1.5 text-xs font-semibold text-ardoise-800 hover:border-menthe-500"
                            >
                              <Languages className="h-3.5 w-3.5" />
                              Textes à traduire — {m?.nom ?? matiereSlug}
                            </Link>
                          );
                        })}
                      </div>
                    );
                  })()}
                </div>
              );
            })}
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
