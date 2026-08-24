# -*- coding: utf-8 -*-
path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

extra = {
    "neolithique": "Le site de Çatalhöyük, en Turquie actuelle, est l'un des plus anciens grands villages néolithiques connus : il comptait plusieurs milliers d'habitants vivant dans des maisons construites côte à côte, il y a environ 9 000 ans. On appelle parfois cette transformation la « révolution néolithique », tant elle a bouleversé durablement le mode de vie humain.",
    "homo-sapiens-migrations-6e": "Les scientifiques utilisent aujourd'hui l'analyse de l'ADN, en plus des fossiles et des outils, pour retracer précisément le trajet de ces migrations à travers le temps. Ces études ont notamment montré que tous les êtres humains actuels descendent d'un petit groupe d'Homo sapiens ayant quitté l'Afrique il y a environ 70 000 ans.",
    "art-prehistorique-6e": "La grotte de Lascaux a été découverte par hasard en 1940 par quatre adolescents à la recherche de leur chien. Devenue trop fragile à cause de l'afflux de visiteurs, elle est aujourd'hui fermée au public, mais une reproduction fidèle, Lascaux IV, permet à chacun de découvrir ces peintures sans les abîmer.",
    "grece-antique-cites-6e": "Le Parthénon, temple dédié à la déesse Athéna, domine encore aujourd'hui l'Acropole d'Athènes : ce monument, construit au 5e siècle avant J.-C., illustre le raffinement de l'architecture grecque et reste un symbole de cette civilisation dans le monde entier.",
    "egypte-pharaons-6e": "Les Égyptiens croyaient en une vie après la mort : c'est pourquoi ils momifiaient les corps des défunts, notamment ceux des pharaons, pour les conserver, et les enterraient avec de nombreux objets destinés à leur être utiles dans l'au-delà, comme le montre le trésor découvert dans la tombe de Toutânkhamon.",
    "rome-monarchie-empire-6e": "L'expression latine « Senatus Populusque Romanus » (le Sénat et le peuple romain), abrégée SPQR, résume l'idée que le pouvoir appartenait en théorie à la fois aux institutions et au peuple romain. Plusieurs mots de notre vocabulaire politique actuel, comme « sénat », « république » ou « consul », viennent directement du latin de cette époque.",
    "jules-cesar-gaule-6e": "La reddition de Vercingétorix devant Jules César, immortalisée par de nombreux tableaux et sculptures, est devenue un symbole très fort dans l'histoire de France : au 19e siècle, Vercingétorix a été présenté comme l'un des premiers héros nationaux, incarnant la résistance face à un envahisseur.",
    "christianisme-empire-romain-6e": "Avant l'édit de Milan, certains chrétiens se réunissaient en secret dans des catacombes, des galeries souterraines servant aussi de lieux de sépulture, pour échapper aux persécutions. Le christianisme s'est ensuite diffusé rapidement grâce aux routes commerciales et aux villes de l'Empire, qui facilitaient la circulation des idées comme des marchandises.",
    "quest-ce-quune-metropole-6e": "Une métropole exerce aussi une influence sur les territoires qui l'entourent, appelés son aire d'influence ou son arrière-pays : elle y attire des travailleurs, des étudiants ou des marchandises, tout en leur fournissant des services (hôpitaux spécialisés, universités, grands équipements) qu'on ne trouve pas dans les villes plus petites.",
    "vivre-metropole-mobilites-6e": "Certaines métropoles ont mis en place des solutions innovantes pour limiter la pollution automobile : Paris avec son service de vélos en libre-service Vélib', Londres avec un péage urbain payant pour les voitures entrant dans le centre-ville, ou encore le développement de zones à faibles émissions réservées aux véhicules les moins polluants.",
    "littoraux-francais-amenagements-6e": "Ces littoraux sont aussi fragiles : l'érosion côtière et la montée du niveau de la mer, liée au changement climatique, menacent certaines zones basses ou certaines falaises, obligeant parfois à repenser l'aménagement du trait de côte pour protéger les populations et les habitations.",
    "vivre-sur-une-ile-6e": "Certaines îles ne sont pas isolées mais regroupées en archipels, un ensemble d'îles proches les unes des autres, comme l'archipel des Antilles dans les Caraïbes ou celui de la Polynésie française dans le Pacifique, ce qui permet parfois une meilleure coopération entre les territoires voisins.",
    "deserts-chauds-froids-6e": "Malgré leurs conditions extrêmes, certains déserts recèlent d'importantes ressources naturelles, comme le pétrole dans certains déserts chauds du Moyen-Orient, ce qui y attire des activités économiques malgré la rareté de l'eau. En Antarctique, aucune population permanente ne vit, mais des scientifiques de nombreux pays y séjournent temporairement dans des bases de recherche.",
    "vivre-montagne-regions-polaires-6e": "Le réchauffement climatique fragilise aujourd'hui de nombreuses stations de sports d'hiver, notamment en moyenne montagne, où l'enneigement devient de plus en plus incertain d'une année sur l'autre, obligeant certaines stations à diversifier leurs activités au-delà du ski.",
    "repartition-population-mondiale-6e": "Depuis 2007, pour la première fois dans l'histoire, plus de la moitié de la population mondiale vit en ville plutôt qu'à la campagne : ce mouvement, appelé urbanisation, se poursuit rapidement, en particulier en Asie et en Afrique, où de nombreuses métropoles connaissent une croissance très rapide.",
    "reperes-planete-continents-oceans-6e": "Deux autres repères importants sont les tropiques : le tropique du Cancer dans l'hémisphère Nord et le tropique du Capricorne dans l'hémisphère Sud. Ils délimitent la zone intertropicale, une bande autour de l'équateur où le climat est chaud toute l'année.",
    "respect-discriminations-6e": "L'histoire montre que les luttes contre les discriminations ont permis de faire progresser les droits : aux États-Unis par exemple, Rosa Parks est devenue en 1955 un symbole de la lutte contre la ségrégation raciale en refusant de céder sa place dans un bus réservé aux personnes blanches.",
    "harcelement-scolaire-6e": "Depuis 2022, le harcèlement scolaire est reconnu en France comme un délit à part entière, puni par la loi : cela signifie que les faits de harcèlement peuvent être sanctionnés pénalement, en plus des sanctions prises par l'établissement scolaire.",
    "symboles-valeurs-republique-6e": "Le visage de Marianne n'est pas figé : depuis les années 1970, le buste installé dans les mairies s'inspire parfois du visage de femmes célèbres, comme Brigitte Bardot ou Catherine Deneuve, incarnant à chaque fois une image renouvelée de la République.",
    "union-europeenne-6e": "L'Union européenne trouve son origine dans la Communauté européenne du charbon et de l'acier (CECA), créée en 1951 par six pays fondateurs (France, Allemagne, Italie, Belgique, Pays-Bas, Luxembourg), qui voulaient rendre la guerre entre eux impossible en mettant en commun des ressources stratégiques.",
    "internet-reseaux-sociaux-securite-6e": "La plupart des réseaux sociaux fixent un âge minimum, souvent 13 ans, pour créer un compte, car ils ne sont pas conçus pour des enfants plus jeunes. Les parents peuvent aussi mettre en place un contrôle parental pour accompagner et protéger leurs enfants dans leurs usages du numérique.",
    "premiers-secours-6e": "L'ensemble de ces actions forme ce qu'on appelle la « chaîne de survie » : alerter rapidement les secours, réaliser les gestes de premiers secours en attendant leur arrivée, utiliser un défibrillateur si nécessaire en cas d'arrêt cardiaque, puis laisser les secours professionnels prendre le relais.",
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
print("6e paragraphs added:", count)
