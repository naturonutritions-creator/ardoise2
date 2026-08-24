import { notFound } from "next/navigation";
import Link from "next/link";
import Header from "@/components/Header";
import ContentGuard from "@/components/ContentGuard";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import QuizPlayer from "@/components/QuizPlayer";
import MatiereIcon from "@/components/MatiereIcon";
import { LESSONS, lessonBySlug } from "@/content/lessons";
import { MATIERES, NIVEAUX } from "@/content/curriculum";
import { Clock, Target, ArrowLeft } from "lucide-react";
import ReadAloud from "@/components/ReadAloud";
import SonReel from "@/components/SonReel";
import MotsAEcouter from "@/components/MotsAEcouter";
import AlphabetAEcouter from "@/components/AlphabetAEcouter";
import VocabulaireLecture from "@/components/VocabulaireLecture";
import ResumeLectureBox from "@/components/ResumeLectureBox";
import SonMatch from "@/components/SonMatch";
import EcouteIntonation from "@/components/EcouteIntonation";
import HistoireLecture from "@/components/HistoireLecture";
import ExercicesSupplementaires from "@/components/ExercicesSupplementaires";
import PhraseLectureCp from "@/components/PhraseLectureCp";
import HighlightedText from "@/components/HighlightedText";
import FriseChronologique from "@/components/FriseChronologique";
import LessonIllustration from "@/components/LessonIllustration";
import LessonPhoto from "@/components/LessonPhoto";
import LessonGallery from "@/components/LessonGallery";
import InlineContentImage from "@/components/InlineContentImage";
import AccessBanner from "@/components/AccessBanner";
import { getAccessStatus } from "@/lib/access";
import { langCode } from "@/content/curriculum";

export function generateStaticParams() {
  return LESSONS.map((l) => ({ matiere: l.matiere, niveau: l.niveau, slug: l.slug }));
}

export default async function CoursPage({
  params,
}: {
  params: Promise<{ matiere: string; niveau: string; slug: string }>;
}) {
  const { matiere: matiereSlug, niveau: niveauSlug, slug } = await params;
  const lesson = lessonBySlug(slug);

  if (!lesson || lesson.matiere !== matiereSlug || lesson.niveau !== niveauSlug) {
    notFound();
  }

  const matiere = MATIERES.find((m) => m.slug === lesson.matiere);
  const niveau = NIVEAUX.find((n) => n.slug === lesson.niveau);
  const lang = langCode(lesson.matiere);
  const access = await getAccessStatus();

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
                  href={`/niveau/${niveau.slug}`}
                  className="inline-flex items-center gap-1 hover:text-craie hover:underline"
                  title={`Retour au programme ${niveau.nom}`}
                >
                  <ArrowLeft className="h-3.5 w-3.5" />
                  {niveau.nom}
                </Link>
              )}
            </div>
            <h1 className="mt-3 font-display text-3xl font-semibold sm:text-4xl">{lesson.titre}</h1>
            <p className="mt-3 max-w-2xl text-craie/80">{lesson.resume}</p>
            <div className="mt-4 flex flex-wrap items-center gap-3 text-sm text-craie/60">
              <span className="flex items-center gap-2">
                <Clock className="h-4 w-4" />
                {lesson.duree}
              </span>
              <ReadAloud
                text={[lesson.resume, ...lesson.objectifs, ...lesson.contenu].join(". ")}
                label="Écouter toute la leçon"
                className="border-craie/30 bg-craie/10 text-craie hover:border-craie/60"
                lang={lang}
                mixedLang
                audioUrl={lesson.audioLecon}
              />
            </div>
          </Container>
        </section>

        <section className="py-14">
          <Container className="grid gap-10 lg:grid-cols-[2fr_1fr]">
            <div>
              <div className="rounded-2xl border border-ardoise-900/10 bg-white p-6 shadow-sm">
                <h2 className="flex items-center gap-2 font-display text-lg font-semibold text-ardoise-900">
                  <Target className="h-5 w-5 text-corail-500" />
                  Objectifs de la leçon
                </h2>
                <ul className="mt-3 list-inside list-disc space-y-1 text-sm text-ardoise-800">
                  {lesson.objectifs.map((o) => (
                    <li key={o}>{o}</li>
                  ))}
                </ul>
              </div>

              <LessonIllustration svg={lesson.illustration} />
              <LessonPhoto photo={lesson.photo} />
              <LessonGallery galerie={lesson.galerie} />

              {lesson.audioSon && (
                <div className="mt-6">
                  <SonReel audio={lesson.audioSon} />
                </div>
              )}

              {lesson.motsAEcouter && lesson.motsAEcouter.length > 0 && (
                <div className="mt-6">
                  <MotsAEcouter mots={lesson.motsAEcouter} lang={lang} />
                </div>
              )}

              {lesson.alphabet && lesson.alphabet.length > 0 && (
                <div className="mt-6">
                  <AlphabetAEcouter lettres={lesson.alphabet} lang={lang} />
                </div>
              )}

              <VocabulaireLecture mots={lesson.vocabulaire} />

              <SonMatch exercices={lesson.sonsAIdentifier} />

              <PhraseLectureCp phrases={lesson.phrasesLectureCp} lang={lang} />

              {lesson.histoire ? (
                <HistoireLecture histoire={lesson.histoire} lang={lang} />
              ) : (
                <EcouteIntonation exercices={lesson.ecouteIntonation} lang={lang} />
              )}

              <article className="prose prose-slate mt-8 max-w-none">
                {lesson.contenuImages
                  ?.filter((img) => img.apresParagraphe === -1)
                  .map((img, k) => <InlineContentImage key={`intro-${k}`} image={img} />)}
                {(access.hasAccess ? lesson.contenu : lesson.contenu.slice(0, 1)).map((paragraphe, i) => {
                  const langueSeule = lesson.contenuLangueSeule?.includes(i) ?? false;
                  return (
                  <div key={i}>
                    <div className="mb-4 flex items-start gap-2">
                      <p className="leading-relaxed text-ardoise-800">
                        <HighlightedText text={paragraphe} />
                      </p>
                      <ReadAloud
                        text={paragraphe}
                        label="Écouter"
                        className="mt-0.5 shrink-0 !px-2 !py-1 text-[11px]"
                        lang={lang}
                        mixedLang={!langueSeule}
                        audioUrl={lesson.audioParagraphes?.[i]}
                      />
                    </div>
                    {lesson.contenuImages
                      ?.filter((img) => img.apresParagraphe === i)
                      .map((img, k) => <InlineContentImage key={`p${i}-${k}`} image={img} />)}
                  </div>
                  );
                })}
              </article>

              {!access.hasAccess && <AccessBanner isTrialExpired={access.isTrialExpired} />}

              {access.hasAccess && (
                <>
                  {lesson.friseChronologique && lesson.friseChronologique.length > 0 && (
                    <div className="mt-8">
                      <FriseChronologique evenements={lesson.friseChronologique} />
                    </div>
                  )}

                  {lesson.exercicesSupplementaires && lesson.exercicesSupplementaires.length > 0 && (
                    <ExercicesSupplementaires
                      exercices={lesson.exercicesSupplementaires}
                      avecAudio={lesson.niveau === "cp" || lesson.niveau === "ce1"}
                      lang={lang}
                    />
                  )}

                  <div className="mt-10">
                    <QuizPlayer quiz={lesson.quiz} lessonSlug={lesson.slug} niveau={lesson.niveau} />
                  </div>

                  <ResumeLectureBox show={lesson.resumeLecture} />
                </>
              )}
            </div>

            <aside>
              <div className="rounded-2xl border border-ardoise-900/10 bg-white p-6">
                <h3 className="font-display text-sm font-semibold uppercase tracking-wide text-ardoise-700/70">
                  Autres leçons — {matiere?.nom} {niveau?.nom}
                </h3>
                <ul className="mt-3 space-y-2">
                  {LESSONS.filter((l) => l.niveau === niveauSlug && l.matiere === matiereSlug && l.slug !== slug).map((l) => (
                    <li key={l.slug}>
                      <Link
                        href={`/cours/${l.matiere}/${l.niveau}/${l.slug}`}
                        className="text-sm font-medium text-ardoise-800 hover:text-corail-600"
                      >
                        {l.titre}
                      </Link>
                    </li>
                  ))}
                  {LESSONS.filter((l) => l.niveau === niveauSlug && l.matiere === matiereSlug && l.slug !== slug).length === 0 && (
                    <li className="text-sm text-ardoise-700/50">Aucune autre leçon pour l&apos;instant.</li>
                  )}
                </ul>
              </div>
            </aside>
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
