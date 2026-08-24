import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import MatiereIcon from "@/components/MatiereIcon";
import { CYCLES, MATIERES } from "@/content/curriculum";
import { ArrowRight, CheckCircle2, Sparkles } from "lucide-react";

export default function Home() {
  return (
    <>
      <Header />
      <main className="flex-1">
        {/* Hero */}
        <section className="relative overflow-hidden bg-ardoise-900 text-craie">
          <div className="chalk-texture absolute inset-0 opacity-40" />
          <Container className="relative py-24 md:py-32">
            <div className="max-w-2xl">
              <span className="inline-flex items-center gap-2 rounded-full bg-craie/10 px-4 py-1.5 text-sm font-medium text-safran-500">
                <Sparkles className="h-4 w-4" />
                Aligné sur le programme officiel de l&apos;Éducation nationale
              </span>
              <h1 className="mt-6 font-display text-4xl font-semibold leading-tight sm:text-5xl">
                Le soutien scolaire qui suit vraiment{" "}
                <span className="text-corail-500">le programme français</span>.
              </h1>
              <p className="mt-6 text-lg text-craie/80">
                Cours, exercices et quiz du CP à la Terminale, construits sur les repères
                officiels d&apos;Éduscol. Une ardoise numérique pour progresser, à son rythme,
                dans toutes les matières.
              </p>
              <div className="mt-8 flex flex-wrap items-center gap-4">
                <Link
                  href="/inscription"
                  className="flex items-center gap-2 rounded-full bg-corail-500 px-6 py-3 text-sm font-semibold text-white shadow-sm transition-colors hover:bg-corail-600"
                >
                  Commencer gratuitement
                  <ArrowRight className="h-4 w-4" />
                </Link>
                <Link
                  href="/programme"
                  className="rounded-full border border-craie/30 px-6 py-3 text-sm font-semibold text-craie transition-colors hover:bg-craie/10"
                >
                  Explorer le programme
                </Link>
              </div>
              <div className="mt-10 flex flex-wrap gap-x-8 gap-y-2 text-sm text-craie/70">
                <span className="flex items-center gap-2"><CheckCircle2 className="h-4 w-4 text-menthe-500" /> Primaire, Collège, Lycée</span>
                <span className="flex items-center gap-2"><CheckCircle2 className="h-4 w-4 text-menthe-500" /> Quiz auto-corrigés</span>
                <span className="flex items-center gap-2"><CheckCircle2 className="h-4 w-4 text-menthe-500" /> Suivi de progression</span>
                <span className="flex items-center gap-2"><CheckCircle2 className="h-4 w-4 text-menthe-500" /> Installable comme une app</span>
              </div>
            </div>
          </Container>
        </section>

        {/* Cycles */}
        <section className="py-20">
          <Container>
            <h2 className="font-display text-3xl font-semibold text-ardoise-900">
              Un accompagnement pour chaque étape de la scolarité
            </h2>
            <div className="mt-10 grid gap-6 md:grid-cols-3">
              {CYCLES.map((cycle) => (
                <Link
                  key={cycle.slug}
                  href={`/programme/${cycle.slug}`}
                  className="group rounded-2xl border border-ardoise-900/10 bg-white p-8 shadow-sm transition-all hover:-translate-y-1 hover:shadow-md"
                >
                  <h3 className="font-display text-xl font-semibold text-ardoise-900">
                    {cycle.nom}
                  </h3>
                  <p className="mt-3 text-sm text-ardoise-700">{cycle.description}</p>
                  <span className="mt-4 inline-flex items-center gap-1 text-sm font-semibold text-corail-600">
                    Découvrir
                    <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
                  </span>
                </Link>
              ))}
            </div>
          </Container>
        </section>

        {/* Matières */}
        <section className="bg-ardoise-100/50 py-20">
          <Container>
            <h2 className="font-display text-3xl font-semibold text-ardoise-900">
              Toutes les matières essentielles
            </h2>
            <div className="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {MATIERES.map((matiere) => (
                <div
                  key={matiere.slug}
                  className="flex items-center gap-4 rounded-xl border border-ardoise-900/10 bg-white p-5"
                >
                  <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-lg bg-corail-100 text-corail-600">
                    <MatiereIcon nom={matiere.icone} className="h-5 w-5" />
                  </div>
                  <div>
                    <p className="font-semibold text-ardoise-900">{matiere.nom}</p>
                    <p className="text-xs text-ardoise-700/70">
                      {matiere.cycles.map((c) => c[0].toUpperCase() + c.slice(1)).join(" · ")}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </Container>
        </section>

        {/* Examens blancs */}
        <section className="py-20">
          <Container>
            <div className="grid items-center gap-10 rounded-3xl bg-ardoise-900 p-10 text-craie md:grid-cols-2 md:p-14">
              <div>
                <span className="inline-flex items-center gap-2 rounded-full bg-craie/10 px-4 py-1.5 text-sm font-medium text-safran-500">
                  Nouveau
                </span>
                <h2 className="mt-4 font-display text-3xl font-semibold">
                  Entraîne-toi avec nos examens blancs
                </h2>
                <p className="mt-3 text-craie/80">
                  Un Brevet blanc pour les élèves de 3e et un Bac blanc pour les Terminale,
                  avec sujets et corrigés détaillés, pour se préparer sereinement le jour J.
                </p>
                <Link
                  href="/examens"
                  className="mt-6 inline-flex items-center gap-2 rounded-full bg-corail-500 px-6 py-3 text-sm font-semibold text-white shadow-sm transition-colors hover:bg-corail-600"
                >
                  Voir les examens blancs
                  <ArrowRight className="h-4 w-4" />
                </Link>
              </div>
              <div className="grid gap-4 sm:grid-cols-2">
                <div className="rounded-2xl bg-craie/10 p-6">
                  <p className="font-display text-lg font-semibold">Brevet blanc</p>
                  <p className="mt-1 text-sm text-craie/70">Français, Maths, Histoire-Géo-EMC</p>
                </div>
                <div className="rounded-2xl bg-craie/10 p-6">
                  <p className="font-display text-lg font-semibold">Bac blanc</p>
                  <p className="mt-1 text-sm text-craie/70">Philosophie, Maths, Histoire-Géo</p>
                </div>
              </div>
            </div>
          </Container>
        </section>

        {/* Comment ça marche */}
        <section className="py-20">
          <Container>
            <h2 className="font-display text-3xl font-semibold text-ardoise-900">
              Comment ça marche
            </h2>
            <div className="mt-10 grid gap-8 md:grid-cols-3">
              {[
                { n: "1", t: "On choisit le niveau", d: "Du CP à la Terminale, on sélectionne la classe et la matière à travailler." },
                { n: "2", t: "On suit la leçon", d: "Un cours clair et structuré, aligné sur les repères officiels du programme." },
                { n: "3", t: "On valide avec le quiz", d: "Un quiz auto-corrigé avec explications pour ancrer les notions durablement." },
              ].map((step) => (
                <div key={step.n}>
                  <div className="flex h-10 w-10 items-center justify-center rounded-full bg-ardoise-900 font-display text-lg font-semibold text-craie">
                    {step.n}
                  </div>
                  <h3 className="mt-4 font-display text-lg font-semibold text-ardoise-900">{step.t}</h3>
                  <p className="mt-2 text-sm text-ardoise-700">{step.d}</p>
                </div>
              ))}
            </div>
          </Container>
        </section>

        {/* CTA */}
        <section className="py-20">
          <Container>
            <div className="rounded-3xl bg-corail-500 px-8 py-14 text-center text-white sm:px-16">
              <h2 className="font-display text-3xl font-semibold">
                Prêt·e à progresser dès aujourd&apos;hui ?
              </h2>
              <p className="mx-auto mt-3 max-w-xl text-white/90">
                Crée un compte gratuit et accède à ta première leçon en moins d&apos;une minute.
              </p>
              <Link
                href="/inscription"
                className="mt-8 inline-flex items-center gap-2 rounded-full bg-white px-6 py-3 text-sm font-semibold text-corail-600 shadow-sm transition-colors hover:bg-craie"
              >
                Créer mon compte
                <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
