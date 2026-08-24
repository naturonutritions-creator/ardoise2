import { notFound } from "next/navigation";
import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import DiplomaCertificate from "@/components/DiplomaCertificate";
import { NIVEAUX } from "@/content/curriculum";

export function generateStaticParams() {
  return NIVEAUX.map((n) => ({ niveau: n.slug }));
}

export default async function DiplomeNiveauPage({
  params,
}: {
  params: Promise<{ niveau: string }>;
}) {
  const { niveau: niveauSlug } = await params;
  const niveau = NIVEAUX.find((n) => n.slug === niveauSlug);
  if (!niveau) notFound();

  return (
    <>
      <div className="print-hide">
        <Header />
      </div>
      <main className="flex-1">
        <section className="print-hide bg-ardoise-900 py-10 text-craie">
          <Container>
            <Link
              href="/diplome"
              className="text-sm text-craie/60 hover:text-craie"
            >
              ← Choisir une autre classe
            </Link>
            <h1 className="mt-3 font-display text-3xl font-semibold sm:text-4xl">
              Diplôme — {niveau.nom}
            </h1>
            <p className="mt-2 max-w-2xl text-craie/80">
              Saisis le prénom et le nom de l&apos;élève, puis imprime ou télécharge le
              diplôme en PDF.
            </p>
          </Container>
        </section>

        <section className="py-10">
          <Container>
            <DiplomaCertificate niveau={niveau} />
          </Container>
        </section>
      </main>
      <div className="print-hide">
        <Footer />
      </div>
    </>
  );
}
