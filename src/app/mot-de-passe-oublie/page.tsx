import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import { MotDePasseOublieForm } from "@/components/AuthForm";

export const metadata = { title: "Mot de passe oublié — Cap Réussite" };

export default function MotDePasseOubliePage() {
  return (
    <>
      <Header />
      <main className="flex flex-1 items-center justify-center py-16">
        <Container className="max-w-md">
          <div className="rounded-2xl border border-ardoise-900/10 bg-white p-8 shadow-sm">
            <h1 className="font-display text-2xl font-semibold text-ardoise-900">Mot de passe oublié</h1>
            <p className="mt-1 text-sm text-ardoise-700/70">On va t&apos;aider à le récupérer.</p>
            <div className="mt-6">
              <MotDePasseOublieForm />
            </div>
          </div>
        </Container>
      </main>
      <Footer />
    </>
  );
}
