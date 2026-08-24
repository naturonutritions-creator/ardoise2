import { notFound } from "next/navigation";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import EvaluationPlayer from "@/components/EvaluationPlayer";
import { EVALUATIONS, evaluationBySlug } from "@/content/evaluations";
import { NIVEAUX } from "@/content/curriculum";

export function generateStaticParams() {
  return EVALUATIONS.map((e) => ({ slug: e.slug }));
}

export default async function EvaluationPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const evaluation = evaluationBySlug(slug);
  if (!evaluation) notFound();

  const niveau = NIVEAUX.find((n) => n.slug === evaluation.niveau);

  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-14 text-craie">
          <Container>
            <p className="text-sm font-medium text-safran-500">
              {niveau?.nom} · Trimestre {evaluation.trimestre}
            </p>
            <h1 className="mt-2 font-display text-3xl font-semibold sm:text-4xl">{evaluation.titre}</h1>
            <p className="mt-3 max-w-2xl text-craie/80">{evaluation.description}</p>
          </Container>
        </section>

        <section className="py-14">
          <Container className="max-w-3xl">
            <EvaluationPlayer evaluation={evaluation} />
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
