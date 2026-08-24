import { notFound } from "next/navigation";
import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import MatiereIcon from "@/components/MatiereIcon";
import { NIVEAUX, matieresDuCycle } from "@/content/curriculum";
import { lessonsByNiveau } from "@/content/lessons";
import { ArrowLeft, ChevronRight } from "lucide-react";

export function generateStaticParams() {
  return NIVEAUX.map((n) => ({ niveau: n.slug }));
}

export default async function NiveauPage({ params }: { params: Promise<{ niveau: string }> }) {
  const { niveau: niveauSlug } = await params;
  const niveau = NIVEAUX.find((n) => n.slug === niveauSlug);
  if (!niveau) notFound();

  const lessonsDuNiveau = lessonsByNiveau(niveau.slug);
  const matieres = matieresDuCycle(niveau.cycle).filter((m) =>
    m.slug === "fiches-memo" ? lessonsDuNiveau.length > 0 : lessonsDuNiveau.some((l) => l.matiere === m.slug)
  );

  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-16 text-craie">
          <Container>
            <Link
              href={`/programme/${niveau.cycle}#${niveau.slug}`}
              className="inline-flex items-center gap-1 text-sm text-safran-500 hover:text-craie hover:underline"
            >
              <ArrowLeft className="h-3.5 w-3.5" />
              Programme
            </Link>
            <h1 className="mt-3 font-display text-4xl font-semibold">{niveau.nom}</h1>
            <p className="mt-3 max-w-2xl text-craie/80">
              Choisis une matière pour retrouver tous ses chapitres.
            </p>
          </Container>
        </section>

        <section className="py-16">
          <Container>
            {matieres.length > 0 ? (
              <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                {matieres.map((matiere) => {
                  const estFiches = matiere.slug === "fiches-memo";
                  const nbChapitres = lessonsDuNiveau.filter((l) => l.matiere === matiere.slug).length;
                  return (
                    <Link
                      key={matiere.slug}
                      href={estFiches ? `/fiches/${niveau.slug}` : `/cours/${matiere.slug}/${niveau.slug}`}
                      className="flex items-center justify-between rounded-2xl border border-ardoise-900/10 bg-white p-5 shadow-sm transition-shadow hover:shadow-md"
                    >
                      <span className="flex items-center gap-3">
                        <span className="flex h-10 w-10 items-center justify-center rounded-xl bg-corail-100 text-corail-600">
                          <MatiereIcon nom={matiere.icone} className="h-5 w-5" />
                        </span>
                        <span>
                          <span className="block font-display font-semibold text-ardoise-900">{matiere.nom}</span>
                          <span className="block text-xs text-ardoise-700/60">
                            {estFiches
                              ? "Mémos, cartes mentales & exercices PDF"
                              : `${nbChapitres} chapitre${nbChapitres > 1 ? "s" : ""}`}
                          </span>
                        </span>
                      </span>
                      <ChevronRight className="h-4 w-4 text-ardoise-700/40" />
                    </Link>
                  );
                })}
              </div>
            ) : (
              <p className="text-sm text-ardoise-700/60">
                De nouvelles leçons pour ce niveau arrivent bientôt.
              </p>
            )}
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
