import { notFound } from "next/navigation";
import { getServerSession } from "next-auth";
import Link from "next/link";
import { authOptions } from "@/lib/auth";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import ExamEpreuveCard from "@/components/ExamEpreuveCard";
import CheckoutProductButton from "@/components/CheckoutProductButton";
import { EXAMS, examBySlug } from "@/content/exams";
import { peutAccederAuPack, niveauxDuPack } from "@/lib/acces";
import { PRODUCTS, type ProductId } from "@/lib/stripe";
import { Clock, Lock } from "lucide-react";

export function generateStaticParams() {
  return EXAMS.map((e) => ({ slug: e.slug }));
}

export default async function ExamPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const exam = examBySlug(slug);
  if (!exam) notFound();

  const product: ProductId = exam.pack === "brevet" ? "brevet-pack" : "bac-pack";
  const session = await getServerSession(authOptions);
  const userId = Number((session?.user as { id?: string } | undefined)?.id);
  const connecte = !!session?.user;
  const debloque = connecte ? await peutAccederAuPack(userId, product) : false;
  const niveaux = niveauxDuPack(product).join(", ");

  return (
    <>
      <Header />
      <main className="flex-1">
        <section className="bg-ardoise-900 py-14 text-craie">
          <Container>
            <p className="text-sm font-medium text-safran-500">
              Examen blanc · Niveau {exam.niveau} · {exam.numero}/6
            </p>
            <h1 className="mt-2 font-display text-4xl font-semibold">{exam.titre}</h1>
            <p className="mt-3 max-w-2xl text-craie/80">{exam.description}</p>
            <div className="mt-4 flex items-center gap-2 text-sm text-craie/60">
              <Clock className="h-4 w-4" />
              {exam.dureeTotale}
            </div>
          </Container>
        </section>

        <section className="py-14">
          <Container className="space-y-6">
            {debloque ? (
              exam.epreuves.map((epreuve, i) => <ExamEpreuveCard key={i} epreuve={epreuve} />)
            ) : (
              <div className="rounded-2xl border border-ardoise-900/10 bg-white p-8 text-center shadow-sm">
                <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-corail-100 text-corail-600">
                  <Lock className="h-5 w-5" />
                </div>
                <h2 className="mt-4 font-display text-xl font-semibold text-ardoise-900">
                  Ce pack de 6 examens blancs est réservé
                </h2>
                <p className="mx-auto mt-2 max-w-lg text-sm text-ardoise-700/70">
                  Débloque les 6 sujets « {exam.pack === "brevet" ? "Brevet blanc" : "Bac blanc"} » (sujets
                  et corrigés complets) pour {PRODUCTS[product].prix}, ou gratuitement si tu as terminé
                  tout le programme {niveaux} sur la plateforme.
                </p>
                {!connecte ? (
                  <Link
                    href="/connexion"
                    className="mt-5 inline-flex items-center justify-center rounded-full bg-corail-500 px-5 py-2.5 text-sm font-semibold text-white hover:bg-corail-600"
                  >
                    Se connecter pour débloquer
                  </Link>
                ) : (
                  <div className="mt-5 flex justify-center">
                    <CheckoutProductButton
                      product={product}
                      label={`Débloquer les 6 sujets — ${PRODUCTS[product].prix}`}
                    />
                  </div>
                )}
              </div>
            )}
          </Container>
        </section>
      </main>
      <Footer />
    </>
  );
}
