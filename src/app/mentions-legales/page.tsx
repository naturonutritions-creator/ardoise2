import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";

export const metadata = { title: "Mentions légales — Cap Réussite" };

export default function Page() {
  return (
    <>
      <Header />
      <main className="flex-1 py-16">
        <Container className="max-w-3xl">
          <h1 className="font-display text-3xl font-semibold text-ardoise-900">Mentions légales</h1>
          <p className="mt-4 text-sm text-ardoise-700">
            Ce contenu est un modèle à personnaliser avant la mise en production. Remplace ce
            texte par les informations légales réelles de ta société (éditeur, hébergeur, données
            personnelles, conditions de vente) avant de publier le site.
          </p>

          <h2 className="mt-10 font-display text-xl font-semibold text-ardoise-900">
            Propriété intellectuelle
          </h2>
          <p className="mt-3 text-sm text-ardoise-700">
            L&apos;ensemble des contenus présents sur le site Cap Réussite (reussifr) — textes des
            leçons, exercices, quiz, évaluations, illustrations, structure du programme, code
            source et charte graphique — est protégé par le droit de la propriété intellectuelle
            et constitue la propriété exclusive de l&apos;éditeur du site, sauf mention contraire.
          </p>
          <p className="mt-3 text-sm text-ardoise-700">
            Toute reproduction, représentation, extraction, réutilisation, ou aspiration
            automatisée (par un robot, un script, un outil d&apos;archivage de site ou tout autre
            procédé technique) de tout ou partie de ce contenu, sur quelque support que ce soit,
            sans autorisation écrite préalable de l&apos;éditeur, est strictement interdite et est
            susceptible de constituer une contrefaçon sanctionnée par les articles L.335-2 et
            suivants du Code de la propriété intellectuelle.
          </p>
          <p className="mt-3 text-sm text-ardoise-700">
            Cette interdiction s&apos;applique en particulier à toute utilisation des contenus du
            site pour l&apos;entraînement de modèles d&apos;intelligence artificielle, à toute
            republication sur un autre site internet, et à tout outil d&apos;aspiration de site
            (site copier). Des dispositifs techniques de détection et de blocage sont mis en
            œuvre pour prévenir ces usages.
          </p>
        </Container>
      </main>
      <Footer />
    </>
  );
}
