import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import { CYCLES, matieresDuCycle, niveauxDuCycle } from "@/content/curriculum";
import ProgrammeSelector from "@/components/ProgrammeSelector";
import { ArrowRight } from "lucide-react";

export const metadata = {
  title: "Programme — Cap Réussite",
  description: "Le programme complet du CP à la Terminale, matière par matière.",
};

export default function ProgrammePage() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-16 text-craie">
          <Container>
            <h1 className="font-display text-4xl font-semibold">Le programme, cycle par cycle</h1>
            <p className="mt-3 max-w-2xl text-craie/80">
              Chaque cycle scolaire dispose de son propre parcours de matières et de niveaux,
              construit à partir des repères annuels de l&apos;Éducation nationale.
            </p>
          </Container>
        </section>

        <section className="py-16">
          <Container className="space-y-16">
            {CYCLES.map((cycle) => (
              <div key={cycle.slug}>
                <div className="flex flex-wrap items-end justify-between gap-4">
                  <div>
                    <h2 className="font-display text-2xl font-semibold text-ardoise-900">{cycle.nom}</h2>
                    <p className="mt-1 text-sm text-ardoise-700">{cycle.description}</p>
                  </div>
                  <Link
                    href={`/programme/${cycle.slug}`}
                    className="flex items-center gap-1 text-sm font-semibold text-corail-600"
                  >
                    Voir le détail <ArrowRight className="h-4 w-4" />
                  </Link>
                </div>

                <div className="mt-6">
                  <ProgrammeSelector
                    niveaux={niveauxDuCycle(cycle.slug)}
                    matieres={matieresDuCycle(cycle.slug)}
                  />
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
