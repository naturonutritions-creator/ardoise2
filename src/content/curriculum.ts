export type Cycle = "primaire" | "college" | "lycee";

export interface Niveau {
  slug: string;
  nom: string;
  cycle: Cycle;
}

export const CYCLES: { slug: Cycle; nom: string; description: string }[] = [
  {
    slug: "primaire",
    nom: "Primaire",
    description: "Du CP au CM2 — les fondamentaux : lecture, écriture, numération.",
  },
  {
    slug: "college",
    nom: "Collège",
    description: "De la 6e à la 3e — consolidation des acquis et préparation au Brevet.",
  },
  {
    slug: "lycee",
    nom: "Lycée",
    description: "De la 2nde à la Terminale — spécialités, Parcoursup et Baccalauréat.",
  },
];

export const NIVEAUX: Niveau[] = [
  { slug: "cp", nom: "CP", cycle: "primaire" },
  { slug: "ce1", nom: "CE1", cycle: "primaire" },
  { slug: "ce2", nom: "CE2", cycle: "primaire" },
  { slug: "cm1", nom: "CM1", cycle: "primaire" },
  { slug: "cm2", nom: "CM2", cycle: "primaire" },
  { slug: "6e", nom: "6e", cycle: "college" },
  { slug: "5e", nom: "5e", cycle: "college" },
  { slug: "4e", nom: "4e", cycle: "college" },
  { slug: "3e", nom: "3e", cycle: "college" },
  { slug: "2nde", nom: "2nde", cycle: "lycee" },
  { slug: "1re", nom: "1re", cycle: "lycee" },
  { slug: "terminale", nom: "Terminale", cycle: "lycee" },
];

export interface Matiere {
  slug: string;
  nom: string;
  icone: string; // lucide-react icon name
  couleur: "corail" | "menthe" | "safran";
  cycles: Cycle[];
}

export const MATIERES: Matiere[] = [
  { slug: "francais", nom: "Français", icone: "BookOpen", couleur: "corail", cycles: ["primaire", "college", "lycee"] },
  { slug: "mathematiques", nom: "Mathématiques", icone: "Sigma", couleur: "menthe", cycles: ["primaire", "college", "lycee"] },
  { slug: "decouverte-du-monde", nom: "Découverte du monde", icone: "Compass", couleur: "safran", cycles: ["primaire"] },
  { slug: "emc", nom: "EMC", icone: "Scale", couleur: "corail", cycles: ["primaire", "college"] },
  { slug: "histoire-geo", nom: "Histoire-Géographie", icone: "Globe2", couleur: "safran", cycles: ["college", "lycee"] },
  { slug: "svt", nom: "SVT", icone: "Leaf", couleur: "menthe", cycles: ["college", "lycee"] },
  { slug: "physique-chimie", nom: "Physique-Chimie", icone: "FlaskConical", couleur: "safran", cycles: ["college", "lycee"] },
  { slug: "anglais", nom: "Anglais", icone: "Languages", couleur: "corail", cycles: ["primaire", "college", "lycee"] },
  { slug: "italien", nom: "Italien", icone: "Languages", couleur: "menthe", cycles: ["primaire", "college", "lycee"] },
  { slug: "espagnol", nom: "Espagnol", icone: "Languages", couleur: "safran", cycles: ["primaire", "college", "lycee"] },
  { slug: "latin", nom: "Latin", icone: "Landmark", couleur: "corail", cycles: ["college", "lycee"] },
  { slug: "philosophie", nom: "Philosophie", icone: "Brain", couleur: "safran", cycles: ["lycee"] },
  { slug: "programmation", nom: "Programmation", icone: "Code2", couleur: "menthe", cycles: ["college", "lycee"] },
  { slug: "fiches-memo", nom: "Fiches & Exercices", icone: "FileDown", couleur: "menthe", cycles: ["primaire", "college", "lycee"] },
];

export function niveauxDuCycle(cycle: Cycle) {
  return NIVEAUX.filter((n) => n.cycle === cycle);
}

export function matieresDuCycle(cycle: Cycle) {
  return MATIERES.filter((m) => m.cycles.includes(cycle));
}

// Code de langue BCP-47 utilisé par la synthèse vocale (Web Speech API)
// pour que chaque matière soit lue avec la bonne prononciation.
export const LANG_CODES: Record<string, string> = {
  anglais: "en-GB",
  espagnol: "es-ES",
  italien: "it-IT",
  latin: "fr-FR", // pas de voix latine disponible dans les navigateurs : on lit le latin avec une voix française, plus naturelle et compréhensible pour un élève francophone
};

export function langCode(matiere: string): string {
  return LANG_CODES[matiere] ?? "fr-FR";
}
