import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";

export const metadata = { title: "Politique de confidentialité — Cap Réussite" };

export default function Page() {
  return (
    <>
      <Header />
      <main className="flex-1 py-16">
        <Container className="max-w-3xl">
          <h1 className="font-display text-3xl font-semibold text-ardoise-900">Politique de confidentialité</h1>
          <p className="mt-4 text-sm text-ardoise-700">
            Ce contenu est un modèle à personnaliser avant la mise en production. Remplace ce
            texte par les informations légales réelles de ta société (éditeur, hébergeur, données
            personnelles, conditions de vente) avant de publier le site.
          </p>
        </Container>
      </main>
      <Footer />
    </>
  );
}
