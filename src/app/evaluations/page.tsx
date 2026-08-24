import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import { EVALUATIONS } from "@/content/evaluations";
import { NIVEAUX } from "@/content/curriculum";
import { ClipboardCheck, ArrowRight } from "lucide-react";

export const metadata = {
  title: "Évaluations trimestrielles — Cap Réussite",
  description: "Des bilans trimestriels pour suivre les progrès du CP au CM2.",
};

const NIVEAUX_PRIMAIRE = ["cp", "ce1", "ce2", "cm1", "cm2"];

export default function EvaluationsPage() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-16 text-craie">
          <Container>
            <span className="inline-flex items-center gap-2 rounded-full bg-craie/10 px-4 py-1.5 text-sm font-medium text-safran-500">
              <ClipboardCheck className="h-4 w-4" />
              Primaire
            </span>
            <h1 className="mt-4 font-display text-4xl font-semibold">Évaluations trimestrielles</h1>
            <p className="mt-3 max-w-2xl text-craie/80">
              Un bilan par trimestre, du CP au CM2, mêlant français, mathématiques et
              questionner le monde, pour suivre la progression sur l&apos;année.
            </p>
          </Container>
        </section>

        <section className="py-16">
          <Container className="space-y-14">
            {NIVEAUX_PRIMAIRE.map((niveauSlug) => {
              const niveau = NIVEAUX.find((n) => n.slug === niveauSlug);
              const evals = EVALUATIONS.filter((e) => e.niveau === niveauSlug).sort(
                (a, b) => a.trimestre - b.trimestre
              );
              return (
                <div key={niveauSlug}>
                  <h2 className="font-display text-2xl font-semibold text-ardoise-900">{niveau?.nom}</h2>
                  <div className="mt-4 grid gap-3 sm:grid-cols-3">
                    {evals.map((evaluation) => (
                      <Link
                        key={evaluation.slug}
                        href={`/evaluations/${evaluation.slug}`}
                        className="group rounded-xl border border-ardoise-900/10 bg-white p-5 transition-shadow hover:shadow-md"
                      >
                        <p className="text-xs font-semibold uppercase tracking-wide text-corail-600">
                          Trimestre {evaluation.trimestre}
                        </p>
                        <p className="mt-2 text-sm text-ardoise-700">{evaluation.description}</p>
                        <span className="mt-4 inline-flex items-center gap-1 text-sm font-semibold text-ardoise-900">
                          Commencer
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
