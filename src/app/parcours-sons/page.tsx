import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import { lessonBySlug } from "@/content/lessons";
import { ArrowRight, Ear } from "lucide-react";

// Parcours pédagogique des sons du CP, organisé du plus simple (une seule
// lettre, un seul son) au plus complexe (graphies à plusieurs lettres,
// sons nasalisés composés). Cet ordre est indépendant de l'ordre de
// rangement du contenu : il reflète la progression conseillée pour un
// enfant qui découvre la lecture, étape par étape.
const ETAPES: { titre: string; description: string; slugs: string[] }[] = [
  {
    titre: "Étape 1 — Les voyelles",
    description: "Le tout premier palier : reconnaître les cinq voyelles, la base de tous les autres sons.",
    slugs: ["les-voyelles"],
  },
  {
    titre: "Étape 2 — Les consonnes simples",
    description: "Une lettre, un son : les consonnes qui se prononcent toujours de la même façon.",
    slugs: [
      "le-son-b",
      "le-son-p",
      "le-son-t",
      "le-son-d",
      "le-son-m",
      "le-son-n",
      "le-son-l",
      "le-son-r",
      "le-son-f-v",
    ],
  },
  {
    titre: "Étape 3 — Les sons composés de deux lettres",
    description: "Deux lettres qui, ensemble, forment un seul son nouveau.",
    slugs: [
      "le-son-ch",
      "le-son-j",
      "le-son-g-dur-doux",
      "le-son-c-qu-k",
      "le-son-s-ss",
      "le-son-gn",
    ],
  },
  {
    titre: "Étape 4 — Les sons nasalisés",
    description: "Des sons qui « passent par le nez » : les plus délicats à l'oreille, à entraîner en dernier parmi les sons simples.",
    slugs: ["le-son-on", "le-son-an-en", "le-son-in-ain", "le-son-oin", "le-son-ien"],
  },
  {
    titre: "Étape 5 — Les sons vocaliques complexes",
    description: "Les sons les plus riches, avec plusieurs graphies possibles pour un même son : le dernier palier avant de lire des phrases entières.",
    slugs: ["le-son-ou", "le-son-oi", "le-son-eu", "le-son-au-eau", "le-son-ai-ei", "le-son-ill-y", "le-son-e-accent-er-ez"],
  },
  {
    titre: "Étape 6 — Lire des phrases",
    description: "Une fois les sons maîtrisés, on assemble : lire une phrase entière et repérer la ponctuation.",
    slugs: ["lire-une-phrase-cp", "la-phrase-et-la-ponctuation-cp"],
  },
];

export const metadata = {
  title: "Parcours des sons — du plus simple au plus complexe | Cap Réussite",
  description:
    "Le parcours conseillé pour apprendre les sons du CP dans l'ordre, des voyelles simples aux sons composés les plus complexes.",
};

export default function ParcoursSonsPage() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-16 text-craie">
          <Container>
            <p className="text-sm font-medium text-safran-500">CP — Français</p>
            <h1 className="mt-2 font-display text-4xl font-semibold">Le parcours des sons</h1>
            <p className="mt-3 max-w-2xl text-craie/80">
              Pour bien apprendre à lire, on avance étape par étape : des sons les plus simples (une
              lettre, un son) jusqu&apos;aux sons les plus complexes (plusieurs graphies, sons nasalisés).
              Suis le parcours dans l&apos;ordre pour progresser sans te perdre.
            </p>
          </Container>
        </section>

        <section className="py-16">
          <Container className="space-y-12">
            {ETAPES.map((etape, ei) => (
              <div key={etape.titre}>
                <div className="mb-4 flex items-center gap-3">
                  <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-menthe-100 font-display text-sm font-semibold text-menthe-700">
                    {ei + 1}
                  </span>
                  <div>
                    <h2 className="font-display text-xl font-semibold text-ardoise-900">{etape.titre}</h2>
                    <p className="text-sm text-ardoise-700/70">{etape.description}</p>
                  </div>
                </div>
                <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
                  {etape.slugs.map((slug) => {
                    const lesson = lessonBySlug(slug);
                    if (!lesson) return null;
                    return (
                      <Link
                        key={slug}
                        href={`/cours/${lesson.matiere}/${lesson.niveau}/${lesson.slug}`}
                        className="group flex items-center justify-between gap-2 rounded-xl border border-ardoise-900/10 bg-white p-4 shadow-sm transition-colors hover:border-corail-500/40"
                      >
                        <span className="flex items-center gap-2 text-sm font-medium text-ardoise-900">
                          <Ear className="h-4 w-4 shrink-0 text-corail-500" />
                          {lesson.titre}
                        </span>
                        <ArrowRight className="h-4 w-4 shrink-0 text-ardoise-700/40 transition-transform group-hover:translate-x-0.5 group-hover:text-corail-600" />
                      </Link>
                    );
                  })}
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
