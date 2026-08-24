import Link from "next/link";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import MatiereIcon from "@/components/MatiereIcon";
import { LESSONS } from "@/content/lessons";
import { MATIERES } from "@/content/curriculum";
import { CheckCircle2, PlayCircle, Sparkles } from "lucide-react";
import { getAccessStatus } from "@/lib/access";

export const metadata = { title: "Tableau de bord — Cap Réussite" };

export default async function TableauDeBordPage() {
  const session = await getServerSession(authOptions);
  const userId = Number((session?.user as { id?: string } | undefined)?.id);
  const access = await getAccessStatus();

  let progressions: { lessonSlug: string; lessonDone: boolean; quizScore: number | null }[] = [];
  try {
    progressions = await db
      .select({
        lessonSlug: schema.progressions.lessonSlug,
        lessonDone: schema.progressions.lessonDone,
        quizScore: schema.progressions.quizScore,
      })
      .from(schema.progressions)
      .where(eq(schema.progressions.userId, userId));
  } catch {
    // Base de données non configurée sur cette démo : le tableau de bord
    // s'affiche quand même, simplement sans historique persisté.
  }

  const doneSlugs = new Set(progressions.filter((p) => p.lessonDone).map((p) => p.lessonSlug));
  const moyenne =
    progressions.length > 0
      ? Math.round(
          progressions.reduce((acc, p) => acc + (p.quizScore ?? 0), 0) / progressions.length
        )
      : null;

  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-14 text-craie">
          <Container>
            <p className="text-sm text-safran-500">Bonjour {session?.user?.name ?? ""} 👋</p>
            <h1 className="mt-1 font-display text-3xl font-semibold">Ton tableau de bord</h1>

            {access.isTrial && access.trialEndsAt && (
              <div className="mt-4 inline-flex items-center gap-2 rounded-full bg-menthe-500/20 px-4 py-1.5 text-sm text-craie">
                <Sparkles className="h-4 w-4 text-menthe-500" />
                Essai gratuit — accès à toutes les classes jusqu&apos;au{" "}
                {access.trialEndsAt.toLocaleDateString("fr-FR", { day: "numeric", month: "long" })}
              </div>
            )}
            {access.isSubscribed && (
              <div className="mt-4 inline-flex items-center gap-2 rounded-full bg-menthe-500/20 px-4 py-1.5 text-sm text-craie">
                <Sparkles className="h-4 w-4 text-menthe-500" />
                Abonnement actif — accès à toutes les classes
              </div>
            )}
            {access.isTrialExpired && (
              <div className="mt-4 inline-flex items-center gap-2 rounded-full bg-corail-500/20 px-4 py-1.5 text-sm text-craie">
                Ton essai gratuit est terminé —{" "}
                <Link href="/tarifs" className="font-semibold underline">
                  voir les abonnements
                </Link>
              </div>
            )}

            <div className="mt-6 flex flex-wrap gap-6">
              <div className="rounded-xl bg-craie/10 px-5 py-3">
                <p className="text-2xl font-display font-semibold">{doneSlugs.size}</p>
                <p className="text-xs text-craie/60">leçons terminées</p>
              </div>
              <div className="rounded-xl bg-craie/10 px-5 py-3">
                <p className="text-2xl font-display font-semibold">{moyenne ?? "—"}{moyenne !== null && "%"}</p>
                <p className="text-xs text-craie/60">score moyen aux quiz</p>
              </div>
            </div>
          </Container>
        </section>

        <section className="py-14">
          <Container>
            <h2 className="font-display text-xl font-semibold text-ardoise-900">Continuer à apprendre</h2>
            <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {LESSONS.map((lesson) => {
                const matiere = MATIERES.find((m) => m.slug === lesson.matiere);
                const done = doneSlugs.has(lesson.slug);
                return (
                  <Link
                    key={lesson.slug}
                    href={`/cours/${lesson.matiere}/${lesson.niveau}/${lesson.slug}`}
                    className="rounded-xl border border-ardoise-900/10 bg-white p-5 transition-shadow hover:shadow-md"
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2 text-xs font-medium text-corail-600">
                        {matiere && <MatiereIcon nom={matiere.icone} className="h-3.5 w-3.5" />}
                        {matiere?.nom} · {lesson.niveau.toUpperCase()}
                      </div>
                      {done ? (
                        <CheckCircle2 className="h-4 w-4 text-menthe-600" />
                      ) : (
                        <PlayCircle className="h-4 w-4 text-ardoise-700/40" />
                      )}
                    </div>
                    <p className="mt-2 font-semibold text-ardoise-900">{lesson.titre}</p>
                    <p className="mt-1 text-xs text-ardoise-700/70">{lesson.duree}</p>
                  </Link>
                );
              })}
            </div>
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
