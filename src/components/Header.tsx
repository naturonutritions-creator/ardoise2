import Link from "next/link";
import Logo from "./Logo";
import Container from "./Container";

const NAV = [
  { href: "/programme", label: "Programme" },
  { href: "/examens", label: "Examens blancs" },
  { href: "/evaluations", label: "Évaluations" },
  { href: "/diplome", label: "Diplômes" },
  { href: "/tdah", label: "TDAH" },
  { href: "/dys", label: "Dys" },
  { href: "/tarifs", label: "Tarifs" },
  { href: "/a-propos", label: "À propos" },
  { href: "/contact", label: "Contact" },
];

export default function Header() {
  return (
    <header className="sticky top-0 z-40 bg-craie/90 shadow-sm backdrop-blur">
      <div className="h-1 w-full bg-gradient-to-r from-ardoise-900 via-menthe-500 to-corail-500" />
      <Container className="flex h-16 items-center justify-between">
        <Link href="/" className="flex items-center gap-2.5">
          <Logo className="h-10 w-10" />
          <span className="font-display text-xl font-semibold text-ardoise-900">Cap Réussite</span>
        </Link>

        <nav className="hidden items-center gap-8 pr-6 md:flex">
          {NAV.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="text-sm font-medium text-ardoise-800 transition-colors hover:text-menthe-600"
            >
              {item.label}
            </Link>
          ))}
        </nav>

        <div className="flex items-center gap-3">
          <Link
            href="/connexion"
            className="hidden text-sm font-medium text-ardoise-800 hover:text-menthe-600 sm:block"
          >
            Connexion
          </Link>
          <Link
            href="/inscription"
            className="rounded-full bg-ardoise-900 px-4 py-2 text-sm font-semibold text-craie shadow-sm transition-colors hover:bg-ardoise-800"
          >
            Essai gratuit
          </Link>
        </div>
      </Container>
    </header>
  );
}
