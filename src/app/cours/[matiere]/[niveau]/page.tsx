import { notFound } from "next/navigation";
import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import MatiereIcon from "@/components/MatiereIcon";
import { MATIERES, NIVEAUX } from "@/content/curriculum";
import { LESSONS } from "@/content/lessons";
import { TEXTES_COMPREHENSION } from "@/content/comprehension";
import { TEXTES_TRADUCTION } from "@/content/traduction";
import { ArrowLeft, Clock, BookOpenCheck, Languages } from "lucide-react";

export function generateStaticParams() {
  const combos = new Set<string>();
  return LESSONS.filter((l) => {
    const key = `${l.matiere}/${l.niveau}`;
    if (combos.has(key)) return false;
    combos.add(key);
    return true;
  }).map((l) => ({ matiere: l.matiere, niveau: l.niveau }));
}

export default async function MatiereNiveauPage({
  params,
}: {
  params: Promise<{ matiere: string; niveau: string }>;
}) {
  const { matiere: matiereSlug, niveau: niveauSlug } = await params;
  const matiere = MATIERES.find((m) => m.slug === matiereSlug);
  const niveau = NIVEAUX.find((n) => n.slug === niveauSlug);
  if (!matiere || !niveau) notFound();

  const chapitres = LESSONS.filter((l) => l.matiere === matiereSlug && l.niveau === niveauSlug);
  const aComprehension = TEXTES_COMPREHENSION.some(
    (t) => t.matiere === matiereSlug && t.niveau === niveauSlug
  );
  const aTraduction = TEXTES_TRADUCTION.some(
    (t) => t.matiere === matiereSlug && t.niveau === niveauSlug
  );

  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-16 text-craie">
          <Container>
            <Link
              href={`/niveau/${niveau.slug}`}
              className="inline-flex items-center gap-1 text-sm text-safran-500 hover:text-craie hover:underline"
            >
              <ArrowLeft className="h-3.5 w-3.5" />
              {niveau.nom}
            </Link>
            <div className="mt-3 flex items-center gap-2">
              <MatiereIcon nom={matiere.icone} className="h-6 w-6 text-safran-500" />
              <h1 className="font-display text-4xl font-semibold">{matiere.nom}</h1>
            </div>
            <p className="mt-3 max-w-2xl text-craie/80">
              Tous les chapitres de {matiere.nom.toLowerCase()} pour le niveau {niveau.nom}.
            </p>
          </Container>
        </section>

        <section className="py-16">
          <Container>
            {(aComprehension || aTraduction) && (
              <div className="mb-6 flex flex-wrap gap-2">
                {aComprehension && (
                  <Link
                    href={`/comprehension/${matiereSlug}/${niveauSlug}`}
                    className="inline-flex items-center gap-1.5 rounded-full border border-corail-500/40 bg-corail-100 px-3 py-1.5 text-xs font-semibold text-corail-700 hover:border-corail-500"
                  >
                    <BookOpenCheck className="h-3.5 w-3.5" />
                    Compréhension de texte
                  </Link>
                )}
                {aTraduction && (
                  <Link
                    href={`/traduction/${matiereSlug}/${niveauSlug}`}
                    className="inline-flex items-center gap-1.5 rounded-full border border-menthe-500/40 bg-menthe-100 px-3 py-1.5 text-xs font-semibold text-ardoise-800 hover:border-menthe-500"
                  >
                    <Languages className="h-3.5 w-3.5" />
                    Textes à traduire
                  </Link>
                )}
              </div>
            )}

            {chapitres.length > 0 ? (
              <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                {chapitres.map((lesson) => (
                  <Link
                    key={lesson.slug}
                    href={`/cours/${lesson.matiere}/${lesson.niveau}/${lesson.slug}`}
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
              <p className="text-sm text-ardoise-700/60">
                De nouveaux chapitres arrivent bientôt pour {matiere.nom.toLowerCase()} — {niveau.nom}.
              </p>
            )}
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
