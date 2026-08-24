import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import { ReinitialiserMotDePasseForm } from "@/components/AuthForm";

export const metadata = { title: "Réinitialiser le mot de passe — Cap Réussite" };

export default async function ReinitialiserMotDePassePage({
  params,
}: {
  params: Promise<{ token: string }>;
}) {
  const { token } = await params;

  return (
    <>
      <Header />
      <main className="flex flex-1 items-center justify-center py-16">
        <Container className="max-w-md">
          <div className="rounded-2xl border border-ardoise-900/10 bg-white p-8 shadow-sm">
            <h1 className="font-display text-2xl font-semibold text-ardoise-900">Nouveau mot de passe</h1>
            <p className="mt-1 text-sm text-ardoise-700/70">Choisis un nouveau mot de passe pour ton compte.</p>
            <div className="mt-6">
              <ReinitialiserMotDePasseForm token={token} />
            </div>
          </div>
        </Container>
      </main>
      <Footer />
    </>
  );
}
