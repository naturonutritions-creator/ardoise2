# -*- coding: utf-8 -*-
path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

extra = {
    "la-prehistoire": "Ce sont les archéologues et les préhistoriens qui reconstituent la vie de nos ancêtres, en étudiant les fossiles, les outils et les traces qu'ils ont laissés (foyers, ossements, peintures). En France, la grotte de Lascaux, découverte en 1940, est l'une des plus célèbres : ses peintures vieilles de plus de 17 000 ans représentent surtout des animaux (chevaux, taureaux, cerfs).",
    "emc-vie-collective-cm1": "Les enfants bénéficient de droits spécifiques, reconnus dans le monde entier par la Convention internationale des droits de l'enfant, adoptée en 1989 : le droit d'être protégé, le droit d'aller à l'école, le droit de jouer, ou encore le droit de donner son avis sur les sujets qui le concernent.",
    "emc-respect-autrui-cm1": "En France, la loi punit sévèrement les discriminations : refuser un emploi, un logement ou l'accès à un lieu public à cause de l'origine, du sexe ou du handicap d'une personne est un délit. Une institution, le Défenseur des droits, peut être saisie par toute personne qui s'estime victime d'une discrimination.",
    "emc-valeurs-republique-cm1": "La devise « Liberté, Égalité, Fraternité » remonte à la Révolution française de 1789 ; elle a ensuite été inscrite dans la Constitution et sur le fronton des bâtiments publics à partir de la fin du XIXe siècle. Marianne, coiffée de son bonnet phrygien, est représentée par un buste dans chaque mairie de France.",
    "gaule-celtique-gaulois-cm1": "Les Gaulois croyaient en de nombreux dieux (ils étaient polythéistes) et vénéraient aussi certains lieux naturels comme les forêts et les sources. Parmi les grands oppidums gaulois, on peut citer Bibracte ou Gergovie, où Vercingétorix remporta une victoire contre les légions de César avant sa défaite finale à Alésia.",
    "gaule-romaine-cm1": "Les Romains construisent un vaste réseau de routes pavées à travers toute la Gaule, permettant de relier rapidement les villes entre elles : plusieurs grands axes routiers actuels suivent encore aujourd'hui le tracé de ces anciennes voies romaines. Des villes comme Lugdunum (Lyon) deviennent d'importants centres administratifs et commerciaux de l'Empire.",
    "clovis-merovingiens-cm1": "Selon la légende, Clovis se serait converti au christianisme après avoir remporté une bataille difficile, en promettant de se faire baptiser en cas de victoire. Ce baptême rapproche les Francs des populations gallo-romaines, déjà majoritairement chrétiennes, ce qui facilite l'unification du royaume.",
    "charlemagne-carolingiens-cm1": "Charlemagne établit sa capitale à Aix-la-Chapelle, où il fait construire un palais et une chapelle richement décorée. Sa figure a marqué durablement les esprits : plusieurs siècles après sa mort, des récits comme la Chanson de Roland racontent, en les enjolivant, ses exploits et ceux de ses chevaliers.",
    "capetiens-saint-louis-cm1": "Le Moyen Âge est aussi une période de grands chantiers religieux : de nombreuses cathédrales gothiques, comme Notre-Dame de Paris (dont la construction commence en 1163) ou celle de Chartres, sont édifiées durant cette période, témoignant de l'importance de la religion catholique dans la société médiévale.",
    "grandes-decouvertes-cm1": "Ces expéditions au long cours sont rendues possibles par des progrès techniques : la boussole, qui indique le nord grâce au magnétisme, et l'astrolabe, qui permet de se repérer grâce aux étoiles, aident les marins à s'orienter en haute mer, loin des côtes qu'ils connaissaient jusque-là.",
    "francois-1er-renaissance-cm1": "Dès son arrivée au pouvoir, François Ier remporte une victoire éclatante à la bataille de Marignan en 1515. Il transforme aussi le palais du Louvre, à Paris, ancienne forteresse médiévale, en une résidence royale de style Renaissance, amorçant la transformation qui en fera plus tard un musée.",
    "henri-iv-guerres-religion-cm1": "Avec l'aide de son ministre Sully, Henri IV s'attache aussi à redresser l'économie du royaume, ruinée par des décennies de guerre : il encourage l'agriculture, les grands travaux et le commerce. Il meurt assassiné en 1610 par François Ravaillac, un fanatique opposé à sa politique de tolérance religieuse.",
    "louis-xiv-cm1": "Le règne de Louis XIV est aussi marqué par un immense rayonnement culturel : le roi protège des artistes et écrivains célèbres comme le dramaturge Molière ou le fabuliste Jean de La Fontaine, qui contribuent à faire de la France un modèle culturel admiré dans toute l'Europe.",
    "se-reperer-espace-cm1": "Pour lire une carte ou un plan, il faut aussi connaître quelques repères essentiels : les points cardinaux (nord, sud, est, ouest), la légende qui explique les symboles utilisés, et l'échelle qui indique le rapport entre les distances sur la carte et les distances réelles sur le terrain.",
    "espaces-urbains-ruraux-cm1": "Depuis plusieurs décennies, la population française s'est fortement concentrée dans les villes et leurs périphéries (on parle de périurbanisation), tandis que certaines zones rurales plus isolées ont vu leur population diminuer, ce qui pose des questions d'aménagement du territoire comme l'accès aux services publics ou aux transports.",
    "consommer-en-france-cm1": "Pour réduire l'impact de notre consommation sur l'environnement, il est aussi possible de privilégier des produits locaux et de saison, achetés en circuit court (directement auprès des producteurs), ce qui limite le transport des marchandises et soutient l'agriculture de proximité.",
    "egalite-filles-garcons-ecole-cm1": "Cette égalité n'a pas toujours existé : ce n'est qu'en 1880, avec la loi Camille Sée, que les filles ont pu accéder à un enseignement secondaire public en France, et il a fallu attendre 1975 pour que les établissements scolaires deviennent officiellement mixtes partout dans le pays.",
}

count = 0
for slug, paragraph in extra.items():
    marker_start = f'slug: "{slug}"'
    idx = txt.index(marker_start)
    # find the contenu array end: "],\n    quiz:" boundary right after contenu
    quiz_idx = txt.index("quiz: {", idx)
    # search backward from quiz_idx for the contenu closing "],\n    " immediately preceding
    close_pattern = '"],\n    quiz: {'
    close_idx = txt.rindex(close_pattern, idx, quiz_idx + len('quiz: {'))
    insertion_point = close_idx + 1  # right after the closing quote of last string, before "]"
    # Actually simpler: insert new sentence before the final "]" of contenu array.
    # close_idx points to the position of the closing quote+comma+bracket sequence '"],\n    quiz: {'
    # We want to insert ', "paragraph"' right before the "]"
    esc = paragraph.replace('"', '\\"')
    insertion = f', "{esc}"'
    txt = txt[:close_idx+1] + insertion + txt[close_idx+1:]
    count += 1

with open(path, 'w') as f:
    f.write(txt)
print("CM1 paragraphs added:", count)
