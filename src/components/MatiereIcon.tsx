import { BookOpen, Sigma, Globe2, FlaskConical, Languages, Brain, Landmark, Leaf, Compass, Scale, FileDown, Code2, type LucideIcon } from "lucide-react";

const ICONS: Record<string, LucideIcon> = {
  BookOpen,
  Sigma,
  Globe2,
  FlaskConical,
  Languages,
  Brain,
  Landmark,
  Leaf,
  Compass,
  Scale,
  FileDown,
  Code2,
};

export default function MatiereIcon({ nom, className }: { nom: string; className?: string }) {
  const Icon = ICONS[nom] ?? BookOpen;
  return <Icon className={className} />;
}
