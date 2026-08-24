import { notFound } from "next/navigation";
import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import MatiereIcon from "@/components/MatiereIcon";
import { MATIERES, NIVEAUX } from "@/content/curriculum";
import { TEXTES_TRADUCTION, textesTraduction } from "@/content/traduction";
import { Languages, Clock } from "lucide-react";

export function generateStaticParams() {
  const pairs = new Set(TEXTES_TRADUCTION.map((t) => `${t.matiere}__${t.niveau}`));
  return Array.from(pairs).map((p) => {
    const [matiere, niveau] = p.split("__");
    return { matiere, niveau };
  });
}

export default async function TraductionListPage({
  params,
}: {
  params: Promise<{ matiere: string; niveau: string }>;
}) {
  const { matiere: matiereSlug, niveau: niveauSlug } = await params;
  const matiere = MATIERES.find((m) => m.slug === matiereSlug);
  const niveau = NIVEAUX.find((n) => n.slug === niveauSlug);
  if (!matiere || !niveau) notFound();

  const textes = textesTraduction(matiereSlug, niveauSlug);

  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-14 text-craie">
          <Container>
            <div className="flex items-center gap-2 text-sm text-safran-500">
              <MatiereIcon nom={matiere.icone} className="h-4 w-4" />
              <span>{matiere.nom}</span>
              <span className="text-craie/40">·</span>
              <span>{niveau.nom}</span>
            </div>
            <h1 className="mt-3 font-display text-3xl font-semibold sm:text-4xl">
              Textes à traduire — thème et version
            </h1>
            <p className="mt-3 max-w-2xl text-craie/80">
              Entraîne-toi à traduire des textes courts dans les deux sens : le thème (du français
              vers la langue) et la version (de la langue vers le français). Chaque texte propose
              du vocabulaire et des conseils de traduction.
            </p>
            <Link
              href={`/cours/${matiere.slug}/${niveau.slug}`}
              className="mt-2 inline-block text-sm text-craie/60 hover:text-craie"
            >
              ← Retour aux leçons {matiere.nom} — {niveau.nom}
            </Link>
          </Container>
        </section>

        <section className="py-14">
          <Container>
            {textes.length > 0 ? (
              <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                {textes.map((t) => (
                  <Link
                    key={t.slug}
                    href={`/traduction/${matiere.slug}/${niveau.slug}/${t.slug}`}
                    className="rounded-2xl border border-ardoise-900/10 bg-white p-5 transition-shadow hover:shadow-md"
                  >
                    <div className="flex items-center gap-2 text-xs font-medium text-corail-600">
                      <Languages className="h-3.5 w-3.5" />
                      Niveau {t.niveauCECRL}
                    </div>
                    <p className="mt-2 font-semibold text-ardoise-900">{t.titre}</p>
                    <p className="mt-1 text-xs text-ardoise-700/70">{t.resume}</p>
                    <p className="mt-3 flex items-center gap-1 text-xs text-ardoise-700/50">
                      <Clock className="h-3.5 w-3.5" />
                      {t.duree}
                    </p>
                  </Link>
                ))}
              </div>
            ) : (
              <p className="text-sm text-ardoise-700/60">
                De nouveaux textes à traduire pour ce niveau arrivent bientôt.
              </p>
            )}
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
