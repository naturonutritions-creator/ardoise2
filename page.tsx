import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import { Check } from "lucide-react";
import CheckoutButton from "@/components/CheckoutButton";

const PLANS = [
  {
    id: "gratuit" as const,
    nom: "Découverte",
    prix: "0 €",
    periode: "",
    description: "Pour explorer la plateforme.",
    avantages: ["Accès à 1 leçon par matière", "Quiz auto-corrigés", "Sans engagement"],
    cta: "Créer un compte gratuit",
    href: "/inscription",
  },
  {
    id: "mensuel" as const,
    nom: "Mensuel",
    prix: "14,90 €",
    periode: "/ mois",
    description: "L'accès complet, sans engagement.",
    avantages: [
      "Toutes les leçons, tous niveaux",
      "Suivi de progression détaillé",
      "Quiz illimités avec explications",
      "Résiliable à tout moment",
    ],
    cta: "Choisir Mensuel",
    populaire: true,
  },
  {
    id: "annuel" as const,
    nom: "Annuel",
    prix: "119 €",
    periode: "/ an",
    description: "2 mois offerts par rapport au mensuel.",
    avantages: [
      "Toutes les leçons, tous niveaux",
      "Suivi de progression détaillé",
      "Quiz illimités avec explications",
      "Meilleur prix à l'année",
    ],
    cta: "Choisir Annuel",
  },
  {
    id: "famille" as const,
    nom: "Famille",
    prix: "24,90 €",
    periode: "/ mois",
    description: "Jusqu'à 4 enfants sur un seul compte.",
    avantages: ["Tout le plan Mensuel", "Jusqu'à 4 profils enfants", "Tableau de bord parent"],
    cta: "Choisir Famille",
  },
];

export const metadata = {
  title: "Tarifs — Ardoise",
};

export default function TarifsPage() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-16 text-craie">
          <Container>
            <h1 className="font-display text-4xl font-semibold">Des tarifs simples et clairs</h1>
            <p className="mt-3 max-w-2xl text-craie/80">
              Un essai gratuit, puis un abonnement sans engagement. Paiement sécurisé, résiliable
              en un clic.
            </p>
          </Container>
        </section>

        <section className="py-16">
          <Container className="grid gap-6 lg:grid-cols-4">
            {PLANS.map((plan) => (
              <div
                key={plan.id}
                className={`flex flex-col rounded-2xl border p-6 ${
                  "populaire" in plan && plan.populaire
                    ? "border-corail-500 bg-white shadow-lg ring-2 ring-corail-500"
                    : "border-ardoise-900/10 bg-white"
                }`}
              >
                {"populaire" in plan && plan.populaire && (
                  <span className="mb-3 inline-block w-fit rounded-full bg-corail-100 px-3 py-1 text-xs font-semibold text-corail-600">
                    Le plus choisi
                  </span>
                )}
                <h2 className="font-display text-lg font-semibold text-ardoise-900">{plan.nom}</h2>
                <p className="mt-1 text-sm text-ardoise-700/70">{plan.description}</p>
                <p className="mt-4">
                  <span className="font-display text-3xl font-semibold text-ardoise-900">{plan.prix}</span>
                  <span className="text-sm text-ardoise-700/70">{plan.periode}</span>
                </p>
                <ul className="mt-6 flex-1 space-y-2">
                  {plan.avantages.map((a) => (
                    <li key={a} className="flex items-start gap-2 text-sm text-ardoise-800">
                      <Check className="mt-0.5 h-4 w-4 shrink-0 text-menthe-600" />
                      {a}
                    </li>
                  ))}
                </ul>
                <div className="mt-6">
                  {plan.id === "gratuit" ? (
                    <a
                      href={plan.href}
                      className="block w-full rounded-full bg-ardoise-900 px-4 py-2.5 text-center text-sm font-semibold text-craie hover:bg-ardoise-800"
                    >
                      {plan.cta}
                    </a>
                  ) : (
                    <CheckoutButton plan={plan.id} label={plan.cta} />
                  )}
                </div>
              </div>
            ))}
          </Container>
          <Container>
            <p className="mt-10 text-center text-xs text-ardoise-700/60">
              Les paiements sont traités par Stripe. En mode démonstration, les clés de paiement ne
              sont pas configurées : voir le README pour activer les paiements réels.
            </p>
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
