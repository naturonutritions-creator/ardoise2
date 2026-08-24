import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";

export const metadata = { title: "À propos — Cap Réussite" };

export default function AProposPage() {
  return (
    <>
      <Header />
      <main className="flex-1 py-16">
        <Container className="max-w-3xl">
          <h1 className="font-display text-4xl font-semibold text-ardoise-900">Notre mission</h1>
          <div className="prose prose-slate mt-6 max-w-none text-ardoise-800">
            <p className="mb-4 leading-relaxed">
              Cap Réussite est née d&apos;un constat simple : les meilleures ressources de soutien
              scolaire sont souvent déconnectées du programme réellement suivi en classe. Nous
              avons voulu construire une plateforme qui colle au plus près des repères annuels
              publiés par l&apos;Éducation nationale, du CP à la Terminale.
            </p>
            <p className="mb-4 leading-relaxed">
              Chaque leçon est pensée pour être courte, claire et actionnable, avec un quiz
              auto-corrigé qui permet à l&apos;élève — et à ses parents — de savoir immédiatement
              où en sont les acquis.
            </p>
            <p className="mb-4 leading-relaxed">
              Cap Réussite fonctionne comme un site et comme une application : installable en un clic
              sur mobile ou ordinateur, elle reste accessible à tout moment, à la maison comme en
              déplacement.
            </p>
          </div>
        </Container>
      </main>
      <Footer />
    </>
  );
}
