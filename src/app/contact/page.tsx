import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Container from "@/components/Container";
import ContactForm from "@/components/ContactForm";

export const metadata = { title: "Contact — Cap Réussite" };

export default function ContactPage() {
  return (
    <>
      <Header />
      <main className="flex-1 py-16">
        <Container className="max-w-xl">
          <h1 className="font-display text-4xl font-semibold text-ardoise-900">Contact</h1>
          <p className="mt-3 text-ardoise-700">
            Une question, une suggestion ? Écris-nous, on te répond sous 48h.
          </p>
          <div className="mt-8">
            <ContactForm />
          </div>
        </Container>
      </main>
      <Footer />
    </>
  );
}
