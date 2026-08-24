import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import { NIVEAUX, CYCLES } from "@/content/curriculum";
import { Award, ArrowRight } from "lucide-react";

export const metadata = {
  title: "Diplômes de fin d'année — Cap Réussite",
  description: "Génère et imprime un diplôme de fin d'année, du CP à la Terminale.",
};

export default function DiplomePage() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-16 text-craie">
          <Container>
            <span className="inline-flex items-center gap-2 rounded-full bg-craie/10 px-4 py-1.5 text-sm font-medium text-safran-500">
              <Award className="h-4 w-4" />
              Récompense
            </span>
            <h1 className="mt-4 font-display text-4xl font-semibold">Diplômes de fin d&apos;année</h1>
            <p className="mt-3 max-w-2xl text-craie/80">
              Choisis ta classe pour créer un diplôme personnalisé, à imprimer ou à
              télécharger en PDF, en récompense d&apos;une belle année de travail.
            </p>
          </Container>
        </section>

        <section className="py-16">
          <Container className="space-y-14">
            {CYCLES.map((cycle) => {
              const niveaux = NIVEAUX.filter((n) => n.cycle === cycle.slug);
              return (
                <div key={cycle.slug}>
                  <h2 className="font-display text-2xl font-semibold text-ardoise-900">{cycle.nom}</h2>
                  <div className="mt-4 grid gap-3 sm:grid-cols-3 lg:grid-cols-4">
                    {niveaux.map((niveau) => (
                      <Link
                        key={niveau.slug}
                        href={`/diplome/${niveau.slug}`}
                        className="group rounded-xl border border-ardoise-900/10 bg-white p-5 transition-shadow hover:shadow-md"
                      >
                        <p className="font-display text-lg font-semibold text-ardoise-900">{niveau.nom}</p>
                        <span className="mt-3 inline-flex items-center gap-1 text-sm font-semibold text-corail-600">
                          Créer le diplôme
                          <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
                        </span>
                      </Link>
                    ))}
                  </div>
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
