# -*- coding: utf-8 -*-
path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

extra = {
    "revolution-francaise-cm2": "Le 14 juillet est resté un symbole si fort qu'il est devenu, en 1880, la date de la fête nationale française, célébrée chaque année par un défilé militaire et des feux d'artifice. Le drapeau tricolore (bleu, blanc, rouge), adopté durant la Révolution, est un autre symbole hérité directement de cette période.",
    "grandes-decouvertes-traite-cm2": "Face à l'esclavage, des révoltes éclatent régulièrement dans les colonies : la plus célèbre est celle de Saint-Domingue, menée notamment par Toussaint Louverture à partir de 1791, qui aboutit à la création d'Haïti en 1804, première République noire indépendante de l'histoire.",
    "renaissance-arts-sciences-cm2": "La Joconde, portrait peint par Léonard de Vinci et aujourd'hui exposée au musée du Louvre, est l'une des œuvres les plus célèbres de la Renaissance : elle illustre parfaitement les nouvelles techniques de l'époque, comme le sfumato, qui adoucit les contours pour un rendu plus réaliste.",
    "louis-xiv-lumieres-cm2": "Les idées des Lumières ne restent pas seulement théoriques : elles influencent directement des événements historiques, comme la déclaration d'indépendance des États-Unis en 1776, qui s'inspire des principes de liberté et de droits naturels défendus par ces philosophes.",
    "revolution-francaise-empire-cm2": "La Révolution transforme aussi la vie quotidienne des Français : elle introduit un nouveau système de mesure, le système métrique (le mètre, le kilogramme), destiné à remplacer la multitude d'unités locales différentes qui existaient jusque-là et à faciliter les échanges dans tout le pays.",
    "france-industrielle-coloniale-republicaine-cm2": "Face aux conditions de travail très dures, notamment pour les enfants, une première loi est votée en 1841 pour limiter le travail des plus jeunes dans les usines ; il faudra cependant attendre plusieurs décennies et de nombreuses luttes ouvrières pour que les conditions de travail s'améliorent réellement.",
    "guerres-mondiales-construction-europeenne-cm2": "Pendant la Seconde Guerre mondiale, la France est occupée par l'Allemagne nazie à partir de 1940. Certains Français choisissent de résister à l'occupant, comme les membres de la Résistance ou les Français libres ralliés au général de Gaulle, au péril de leur vie, tandis que le régime de Vichy collabore avec l'occupant.",
    "se-reperer-monde-cm2": "L'équateur, une ligne imaginaire qui fait le tour de la Terre à égale distance des deux pôles, sépare la planète en deux hémisphères : l'hémisphère Nord et l'hémisphère Sud. Le point culminant de la planète est le mont Everest, en Asie (8 849 m), tandis que le point le plus profond des océans se trouve dans la fosse des Mariannes, dans l'océan Pacifique.",
    "diversite-regions-francaises-cm2": "Parmi les langues régionales encore parlées en France, on peut citer le breton (en Bretagne), l'occitan (dans le sud), l'alsacien (en Alsace) ou le corse (en Corse). Bien que le français soit la seule langue officielle, ces langues font partie du patrimoine culturel des régions concernées.",
    "france-monde-langue-francaise-cm2": "L'Organisation internationale de la Francophonie (OIF), créée en 1970, réunit aujourd'hui une centaine de pays et gouvernements à travers le monde qui partagent l'usage du français. Elle organise notamment tous les deux ans un Sommet de la Francophonie et des Jeux de la Francophonie.",
    "produire-en-france-cm2": "La France est aussi reconnue pour certaines productions de haute technologie, comme l'aéronautique et l'aérospatiale : la région toulousaine, par exemple, est un centre majeur de construction aéronautique européenne, avec la présence d'Airbus.",
    "se-deplacer-villes-france-cm2": "Le réseau de trains à grande vitesse (TGV) français, l'un des plus développés d'Europe, permet de relier Paris à de nombreuses grandes villes en quelques heures seulement (par exemple Paris-Lyon en moins de deux heures), et la plupart des grandes lignes ferroviaires sont organisées en étoile, partant de Paris vers les régions.",
    "europe-symboles-cm2": "L'Union européenne comptait 28 pays membres jusqu'en 2020, année où le Royaume-Uni l'a quittée (un événement appelé le « Brexit ») : elle en compte aujourd'hui 27. Chaque nouveau pays qui souhaite la rejoindre doit respecter un ensemble de critères, notamment démocratiques et économiques.",
    "secourisme-cm2": "Si une victime est inconsciente mais respire normalement, on peut la placer en position latérale de sécurité (PLS), qui l'empêche de s'étouffer en cas de vomissement. Dans de nombreux lieux publics, on trouve aussi des défibrillateurs automatisés, que toute personne peut utiliser en suivant les instructions vocales de l'appareil pour aider en cas d'arrêt cardiaque.",
    "debat-developpement-durable-cm2": "Le développement durable repose traditionnellement sur trois piliers indissociables : le pilier environnemental (protéger la nature et les ressources), le pilier économique (permettre une activité juste et durable) et le pilier social (garantir des conditions de vie dignes pour tous). Un conseil municipal des enfants, présent dans certaines communes, est un exemple concret de lieu où s'exercer au débat citoyen.",
    "droits-devoirs-citoyen-cm2": "On peut devenir citoyen français de différentes façons : par la naissance (si l'un de ses parents est français, ou parfois si l'on naît en France), ou par la naturalisation, une procédure administrative pour les personnes étrangères qui souhaitent devenir françaises. Depuis 2003, cette acquisition peut être marquée par une cérémonie d'accueil dans la citoyenneté française.",
}

count = 0
for slug, paragraph in extra.items():
    marker_start = f'slug: "{slug}"'
    idx = txt.index(marker_start)
    quiz_idx = txt.index("quiz: {", idx)
    close_pattern = '"],\n    quiz: {'
    close_idx = txt.rindex(close_pattern, idx, quiz_idx + len('quiz: {'))
    esc = paragraph.replace('"', '\\"')
    insertion = f', "{esc}"'
    txt = txt[:close_idx+1] + insertion + txt[close_idx+1:]
    count += 1

with open(path, 'w') as f:
    f.write(txt)
print("CM2 paragraphs added:", count)
