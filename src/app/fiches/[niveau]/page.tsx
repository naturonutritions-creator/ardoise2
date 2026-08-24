import { notFound } from "next/navigation";
import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import MatiereIcon from "@/components/MatiereIcon";
import { NIVEAUX, MATIERES } from "@/content/curriculum";
import { lessonsByNiveau } from "@/content/lessons";
import { ficheMemoUrl, ficheExercicesUrl } from "@/lib/fiches";
import { ArrowLeft, FileDown, ClipboardList, GraduationCap } from "lucide-react";

export function generateStaticParams() {
  return NIVEAUX.map((n) => ({ niveau: n.slug }));
}

export default async function FichesNiveauPage({ params }: { params: Promise<{ niveau: string }> }) {
  const { niveau: niveauSlug } = await params;
  const niveau = NIVEAUX.find((n) => n.slug === niveauSlug);
  if (!niveau) notFound();

  const lecons = lessonsByNiveau(niveau.slug);
  const parMatiere = new Map<string, typeof lecons>();
  for (const l of lecons) {
    if (!parMatiere.has(l.matiere)) parMatiere.set(l.matiere, []);
    parMatiere.get(l.matiere)!.push(l);
  }

  const groupes = Array.from(parMatiere.entries())
    .map(([matiereSlug, items]) => ({
      matiere: MATIERES.find((m) => m.slug === matiereSlug),
      matiereSlug,
      items,
    }))
    .sort((a, b) => (a.matiere?.nom ?? a.matiereSlug).localeCompare(b.matiere?.nom ?? b.matiereSlug));

  const isBrevetOuBac = niveau.slug === "3e" || niveau.slug === "terminale";

  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-14 text-craie">
          <Container>
            <Link
              href={`/niveau/${niveau.slug}`}
              className="inline-flex items-center gap-1 text-sm text-safran-500 hover:text-craie hover:underline"
            >
              <ArrowLeft className="h-3.5 w-3.5" />
              {niveau.nom}
            </Link>
            <h1 className="mt-3 font-display text-3xl font-semibold sm:text-4xl">
              Fiches & Exercices — {niveau.nom}
            </h1>
            <p className="mt-3 max-w-2xl text-craie/80">
              Pour chaque chapitre : une fiche mémo téléchargeable (carte mentale, frise ou tableau
              récapitulatif), et pour le français, les mathématiques et la conjugaison en langues, une
              feuille d&apos;exercices avec corrigé.
            </p>
          </Container>
        </section>

        {isBrevetOuBac && (
          <section className="border-b border-ardoise-900/10 bg-safran-100 py-6">
            <Container className="flex flex-wrap items-center justify-between gap-3">
              <p className="flex items-center gap-2 text-sm font-medium text-ardoise-900">
                <GraduationCap className="h-4 w-4" />
                {niveau.slug === "3e"
                  ? "6 sujets de Brevet blanc corrigés t'attendent aussi."
                  : "6 sujets de Bac blanc corrigés t'attendent aussi."}
              </p>
              <Link
                href="/examens"
                className="inline-flex items-center rounded-full bg-corail-500 px-4 py-2 text-xs font-semibold text-white hover:bg-corail-600"
              >
                Voir les examens blancs
              </Link>
            </Container>
          </section>
        )}

        <section className="py-14">
          <Container className="space-y-10">
            {groupes.length === 0 && (
              <p className="text-sm text-ardoise-700/60">Aucune fiche disponible pour ce niveau pour le moment.</p>
            )}
            {groupes.map((groupe) => (
              <div key={groupe.matiereSlug}>
                <h2 className="flex items-center gap-2 font-display text-xl font-semibold text-ardoise-900">
                  {groupe.matiere && <MatiereIcon nom={groupe.matiere.icone} className="h-5 w-5 text-corail-500" />}
                  {groupe.matiere?.nom ?? groupe.matiereSlug}
                </h2>
                <div className="mt-4 grid gap-3 sm:grid-cols-2">
                  {groupe.items.map((lesson) => {
                    const exoUrl = ficheExercicesUrl(lesson);
                    return (
                      <div
                        key={lesson.slug}
                        className="rounded-xl border border-ardoise-900/10 bg-white p-4 shadow-sm"
                      >
                        <p className="font-semibold text-ardoise-900">{lesson.titre}</p>
                        <div className="mt-3 flex flex-wrap gap-2">
                          <a
                            href={ficheMemoUrl(lesson)}
                            download
                            className="inline-flex items-center gap-1.5 rounded-full border border-ardoise-900/20 px-3 py-1.5 text-xs font-semibold text-ardoise-800 hover:border-corail-500 hover:text-corail-600"
                          >
                            <FileDown className="h-3.5 w-3.5" />
                            Fiche mémo (PDF)
                          </a>
                          {exoUrl && (
                            <a
                              href={exoUrl}
                              download
                              className="inline-flex items-center gap-1.5 rounded-full border border-ardoise-900/20 px-3 py-1.5 text-xs font-semibold text-ardoise-800 hover:border-menthe-600 hover:text-menthe-600"
                            >
                              <ClipboardList className="h-3.5 w-3.5" />
                              Exercices + corrigé (PDF)
                            </a>
                          )}
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            ))}
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
