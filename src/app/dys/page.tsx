import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import { PROFIL_INFO } from "@/components/ProfilBadge";
import { adaptedNiveauxByProfil, type ProfilAdaptation } from "@/content/adaptations";
import { NIVEAUX, CYCLES } from "@/content/curriculum";
import { ChevronRight } from "lucide-react";

export const metadata = {
  title: "Dyslexie & Dyscalculie — Cap Réussite",
  description: "Des leçons adaptées pour les élèves dyslexiques et dyscalculiques, classées par niveau et par matière.",
};

const TABS: { profil: ProfilAdaptation; label: string }[] = [
  { profil: "dyslexie", label: "Dyslexie" },
  { profil: "dyscalculie", label: "Dyscalculie" },
];

export default async function DysPage({
  searchParams,
}: {
  searchParams: Promise<{ profil?: string }>;
}) {
  const { profil: profilParam } = await searchParams;
  const profil: ProfilAdaptation = profilParam === "dyscalculie" ? "dyscalculie" : "dyslexie";
  const info = PROFIL_INFO[profil];
  const Icon = info.icone;
  const niveauxDisponibles = new Set(adaptedNiveauxByProfil(profil));
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
            <h1 className="mt-4 font-display text-4xl font-semibold">Dys</h1>
            <p className="mt-3 max-w-2xl text-craie/80">
              Choisis un onglet, puis un niveau et une matière pour retrouver les leçons adaptées.
            </p>

            <div className="mt-6 inline-flex rounded-full bg-craie/10 p-1">
              {TABS.map((tab) => (
                <Link
                  key={tab.profil}
                  href={`/dys?profil=${tab.profil}`}
                  className={`rounded-full px-5 py-2 text-sm font-semibold transition-colors ${
                    profil === tab.profil
                      ? "bg-craie text-ardoise-900"
                      : "text-craie/70 hover:text-craie"
                  }`}
                >
                  {tab.label}
                </Link>
              ))}
            </div>
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
                      href={`/dys/${profil}/${niveau.slug}`}
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
                De nouvelles leçons adaptées arrivent bientôt pour ce profil.
              </p>
            )}
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
