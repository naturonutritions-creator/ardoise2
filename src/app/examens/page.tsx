import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import { EXAMS } from "@/content/exams";
import { PRODUCTS } from "@/lib/stripe";
import { GraduationCap, Clock, ArrowRight } from "lucide-react";

export const metadata = {
  title: "Examens blancs — Cap Réussite",
  description: "Entraîne-toi dans les conditions du Brevet et du Baccalauréat avec des épreuves types corrigées.",
};

export default function ExamensPage() {
  const brevets = EXAMS.filter((e) => e.pack === "brevet").sort((a, b) => a.numero - b.numero);
  const bacs = EXAMS.filter((e) => e.pack === "bac").sort((a, b) => a.numero - b.numero);

  const groupes = [
    {
      titre: "Brevet blanc — 6 sujets",
      sousTitre: "Niveau 3e",
      prix: PRODUCTS["brevet-pack"].prix,
      gratuit: "Gratuit si tu as terminé tout le programme de la 6e à la 3e sur la plateforme.",
      exams: brevets,
    },
    {
      titre: "Bac blanc — 6 sujets",
      sousTitre: "Niveau Terminale",
      prix: PRODUCTS["bac-pack"].prix,
      gratuit: "Gratuit si tu as terminé tout le programme de la 2nde à la Terminale sur la plateforme.",
      exams: bacs,
    },
  ];

  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-16 text-craie">
          <Container>
            <h1 className="font-display text-4xl font-semibold">Examens blancs</h1>
            <p className="mt-3 max-w-2xl text-craie/80">
              Des épreuves d&apos;entraînement type, avec sujets et corrigés, pour se mettre en
              conditions avant le Brevet et le Baccalauréat.
            </p>
          </Container>
        </section>

        {groupes.map((groupe) => (
          <section key={groupe.titre} className="py-14">
            <Container>
              <div className="mb-6 flex flex-wrap items-end justify-between gap-3">
                <div>
                  <h2 className="font-display text-2xl font-semibold text-ardoise-900">{groupe.titre}</h2>
                  <p className="text-sm text-ardoise-700/70">{groupe.sousTitre}</p>
                </div>
                <div className="rounded-xl bg-safran-100 px-4 py-2 text-right">
                  <p className="font-display text-lg font-semibold text-ardoise-900">{groupe.prix}</p>
                  <p className="max-w-xs text-xs text-ardoise-700/70">{groupe.gratuit}</p>
                </div>
              </div>
              <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
                {groupe.exams.map((exam) => (
                  <Link
                    key={exam.slug}
                    href={`/examens/${exam.slug}`}
                    className="group rounded-2xl border border-ardoise-900/10 bg-white p-6 shadow-sm transition-all hover:-translate-y-1 hover:shadow-md"
                  >
                    <div className="flex h-11 w-11 items-center justify-center rounded-lg bg-corail-100 text-corail-600">
                      <GraduationCap className="h-5 w-5" />
                    </div>
                    <h3 className="mt-4 font-display text-lg font-semibold text-ardoise-900">{exam.titre}</h3>
                    <p className="mt-2 text-sm text-ardoise-800">{exam.description}</p>
                    <div className="mt-4 flex items-center gap-1 text-xs text-ardoise-700/60">
                      <Clock className="h-3.5 w-3.5" /> {exam.dureeTotale}
                    </div>
                    <span className="mt-5 inline-flex items-center gap-1 text-sm font-semibold text-corail-600">
                      Voir les épreuves
                      <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
                    </span>
                  </Link>
                ))}
              </div>
            </Container>
          </section>
        ))}

        <Container>
          <p className="mb-14 text-sm text-ardoise-700/60">
            Ces épreuves sont des modèles d&apos;entraînement inspirés des formats officiels, à
            titre d&apos;exercice. Elles ne remplacent pas les annales officielles ni les
            modalités exactes communiquées par l&apos;Éducation nationale pour l&apos;année en
            cours.
          </p>
        </Container>
      </main>
      <Footer />
    </>
  );
}
