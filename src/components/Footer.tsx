import Link from "next/link";
import Logo from "./Logo";
import Container from "./Container";

export default function Footer() {
  return (
    <footer className="mt-24 border-t border-ardoise-900/10 bg-ardoise-900 text-craie">
      <Container className="grid gap-10 py-14 md:grid-cols-4">
        <div>
          <div className="flex items-center gap-2">
            <Logo className="h-7 w-7" />
            <span className="font-display text-lg font-semibold">Cap Réussite</span>
          </div>
          <p className="mt-3 text-sm text-craie/70">
            Le soutien scolaire aligné sur le programme officiel de l&apos;Éducation nationale,
            du CP à la Terminale.
          </p>
        </div>

        <div>
          <h3 className="font-display text-sm font-semibold uppercase tracking-wide text-craie/60">
            Programme
          </h3>
          <ul className="mt-3 space-y-2 text-sm">
            <li><Link href="/programme/primaire" className="hover:text-corail-500">Primaire</Link></li>
            <li><Link href="/programme/college" className="hover:text-corail-500">Collège</Link></li>
            <li><Link href="/programme/lycee" className="hover:text-corail-500">Lycée</Link></li>
            <li><Link href="/examens" className="hover:text-corail-500">Examens blancs</Link></li>
            <li><Link href="/evaluations" className="hover:text-corail-500">Évaluations trimestrielles</Link></li>
            <li><Link href="/tdah" className="hover:text-corail-500">TDAH</Link></li>
            <li><Link href="/dys" className="hover:text-corail-500">Dys (dyslexie / dyscalculie)</Link></li>
          </ul>
        </div>

        <div>
          <h3 className="font-display text-sm font-semibold uppercase tracking-wide text-craie/60">
            Cap Réussite
          </h3>
          <ul className="mt-3 space-y-2 text-sm">
            <li><Link href="/a-propos" className="hover:text-corail-500">À propos</Link></li>
            <li><Link href="/tarifs" className="hover:text-corail-500">Tarifs</Link></li>
            <li><Link href="/contact" className="hover:text-corail-500">Contact</Link></li>
          </ul>
        </div>

        <div>
          <h3 className="font-display text-sm font-semibold uppercase tracking-wide text-craie/60">
            Légal
          </h3>
          <ul className="mt-3 space-y-2 text-sm">
            <li><Link href="/mentions-legales" className="hover:text-corail-500">Mentions légales</Link></li>
            <li><Link href="/confidentialite" className="hover:text-corail-500">Confidentialité</Link></li>
            <li><Link href="/cgv" className="hover:text-corail-500">CGV</Link></li>
          </ul>
        </div>
      </Container>
      <div className="border-t border-craie/10 py-6 text-center text-xs text-craie/50">
        © {new Date().getFullYear()} Cap Réussite. Tous droits réservés. Toute reproduction ou
        extraction automatisée du contenu est interdite.
      </div>
    </footer>
  );
}
