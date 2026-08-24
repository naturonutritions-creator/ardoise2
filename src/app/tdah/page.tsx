import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import { PROFIL_INFO } from "@/components/ProfilBadge";
import { adaptedNiveauxByProfil } from "@/content/adaptations";
import { NIVEAUX, CYCLES } from "@/content/curriculum";
import { ChevronRight } from "lucide-react";

export const metadata = {
  title: "TDAH — Cap Réussite",
  description: "Des leçons adaptées, en petites étapes, pour les élèves avec un TDAH, classées par niveau et par matière.",
};

export default function TdahPage() {
  const info = PROFIL_INFO.tdah;
  const Icon = info.icone;
  const niveauxDisponibles = new Set(adaptedNiveauxByProfil("tdah"));
  const niveaux = NIVEAUX.filter((n) => niveauxDisponibles.has(n.slug));

  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-16 text-craie">
          <Container>
            <span className="inline-flex items-center gap-2 rounded-full bg-craie/10 px-4 py-1.5 text-sm font-medium text-safran-500">
              <Icon className="h-4 w-4" />
              Contenu adapté
            </span>
            <h1 className="mt-4 font-display text-4xl font-semibold">{info.nom}</h1>
            <p className="mt-3 max-w-2xl text-craie/80">
              Choisis un niveau, puis une matière pour retrouver les leçons adaptées.
            </p>
          </Container>
        </section>

        <section className="py-16">
          <Container>
            <p className="mb-8 rounded-xl border border-ardoise-900/10 bg-ardoise-100/50 p-4 text-sm text-ardoise-700">
              {info.description}
            </p>

            {niveaux.length > 0 ? (
              <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                {niveaux.map((niveau) => {
                  const cycle = CYCLES.find((cy) => cy.slug === niveau.cycle);
                  return (
                    <Link
                      key={niveau.slug}
                      href={`/tdah/niveau/${niveau.slug}`}
                      className="flex items-center justify-between rounded-2xl border border-ardoise-900/10 bg-white p-5 shadow-sm transition-shadow hover:shadow-md"
                    >
                      <span>
                        <span className="block font-display text-lg font-semibold text-ardoise-900">
                          {niveau.nom}
                        </span>
                        <span className="block text-xs text-ardoise-700/60">{cycle?.nom}</span>
                      </span>
                      <ChevronRight className="h-4 w-4 text-ardoise-700/40" />
                    </Link>
                  );
                })}
              </div>
            ) : (
              <p className="text-sm text-ardoise-700/60">
                De nouvelles leçons adaptées arrivent bientôt.
              </p>
            )}
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
