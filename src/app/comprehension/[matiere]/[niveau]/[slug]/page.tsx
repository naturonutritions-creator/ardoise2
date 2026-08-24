import { notFound } from "next/navigation";
import Link from "next/link";
import Header from "@/components/Header";
import ContentGuard from "@/components/ContentGuard";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import QuizPlayer from "@/components/QuizPlayer";
import MatiereIcon from "@/components/MatiereIcon";
import ReadAloud from "@/components/ReadAloud";
import { MATIERES, NIVEAUX, langCode } from "@/content/curriculum";
import { TEXTES_COMPREHENSION, texteComprehensionBySlug } from "@/content/comprehension";
import { Clock, BookOpenCheck, ArrowLeft } from "lucide-react";

export function generateStaticParams() {
  return TEXTES_COMPREHENSION.map((t) => ({ matiere: t.matiere, niveau: t.niveau, slug: t.slug }));
}

export default async function ComprehensionPage({
  params,
}: {
  params: Promise<{ matiere: string; niveau: string; slug: string }>;
}) {
  const { matiere: matiereSlug, niveau: niveauSlug, slug } = await params;
  const texte = texteComprehensionBySlug(slug);

  if (!texte || texte.matiere !== matiereSlug || texte.niveau !== niveauSlug) {
    notFound();
  }

  const matiere = MATIERES.find((m) => m.slug === texte.matiere);
  const niveau = NIVEAUX.find((n) => n.slug === texte.niveau);
  const lang = langCode(texte.matiere);
  const autres = TEXTES_COMPREHENSION.filter(
    (t) => t.niveau === niveauSlug && t.matiere === matiereSlug && t.slug !== slug
  );

  return (
    <>
      <Header />
      <ContentGuard />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-14 text-craie">
          <Container>
            <div className="flex items-center gap-2 text-sm text-safran-500">
              {matiere && <MatiereIcon nom={matiere.icone} className="h-4 w-4" />}
              <span>{matiere?.nom}</span>
              <span className="text-craie/40">·</span>
              {niveau && (
                <Link
                  href={`/programme/${niveau.cycle}#${niveau.slug}`}
                  className="inline-flex items-center gap-1 hover:text-craie hover:underline"
                  title={`Retour au programme ${niveau.nom}`}
                >
                  <ArrowLeft className="h-3.5 w-3.5" />
                  {niveau.nom}
                </Link>
              )}
              <span className="text-craie/40">·</span>
              <span className="inline-flex items-center gap-1">
                <BookOpenCheck className="h-3.5 w-3.5" />
                Niveau {texte.niveauCECRL}
              </span>
            </div>
            <h1 className="mt-3 font-display text-3xl font-semibold sm:text-4xl">{texte.titre}</h1>
            <p className="mt-3 max-w-2xl text-craie/80">{texte.resume}</p>
            <div className="mt-4 flex flex-wrap items-center gap-3 text-sm text-craie/60">
              <span className="flex items-center gap-2">
                <Clock className="h-4 w-4" />
                {texte.duree}
              </span>
              <ReadAloud
                text={texte.texte.join(" ")}
                label="Écouter tout le texte"
                className="border-craie/30 bg-craie/10 text-craie hover:border-craie/60"
                lang={lang}
              />
            </div>
          </Container>
        </section>

        <section className="py-14">
          <Container className="grid gap-10 lg:grid-cols-[2fr_1fr]">
            <div>
              <article className="rounded-2xl border border-ardoise-900/10 bg-white p-6 shadow-sm">
                {texte.texte.map((paragraphe, i) => (
                  <div key={i} className="mb-4 flex items-start gap-2 last:mb-0">
                    <p className="leading-relaxed text-ardoise-800">{paragraphe}</p>
                    <ReadAloud
                      text={paragraphe}
                      label="Écouter"
                      className="mt-0.5 shrink-0 !px-2 !py-1 text-[11px]"
                      lang={lang}
                    />
                  </div>
                ))}
              </article>

              {texte.glossaire && texte.glossaire.length > 0 && (
                <div className="mt-6 rounded-2xl border border-menthe-500/30 bg-menthe-100 p-6">
                  <h3 className="font-display text-sm font-semibold text-ardoise-900">
                    Vocabulaire utile
                  </h3>
                  <ul className="mt-3 grid gap-1.5 sm:grid-cols-2">
                    {texte.glossaire.map((g) => (
                      <li key={g.mot} className="text-sm text-ardoise-800">
                        <span className="font-semibold">{g.mot}</span> — {g.traduction}
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              <div className="mt-10">
                <QuizPlayer quiz={texte.quiz} lessonSlug={texte.slug} niveau={texte.niveau} />
              </div>
            </div>

            <aside>
              <div className="rounded-2xl border border-ardoise-900/10 bg-white p-6">
                <h3 className="font-display text-sm font-semibold uppercase tracking-wide text-ardoise-700/70">
                  Autres textes — {matiere?.nom} {niveau?.nom}
                </h3>
                <ul className="mt-3 space-y-2">
                  {autres.map((t) => (
                    <li key={t.slug}>
                      <Link
                        href={`/comprehension/${t.matiere}/${t.niveau}/${t.slug}`}
                        className="text-sm font-medium text-ardoise-800 hover:text-corail-600"
                      >
                        {t.titre}
                      </Link>
                    </li>
                  ))}
                  {autres.length === 0 && (
                    <li className="text-sm text-ardoise-700/50">Aucun autre texte pour l&apos;instant.</li>
                  )}
                </ul>
                <Link
                  href={`/cours/${matiereSlug}/${niveauSlug}`}
                  className="mt-4 inline-block text-sm font-medium text-corail-600 hover:text-corail-700"
                >
                  ← Retour aux leçons
                </Link>
              </div>
            </aside>
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
