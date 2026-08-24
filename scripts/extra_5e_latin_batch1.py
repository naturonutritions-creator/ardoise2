import re

path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

def q(id_, enonce, choix, reponse, explication):
    choix_str = ", ".join(f'"{c}"' for c in choix)
    return f'''      {{
        id: "{id_}",
        enonce: "{enonce}",
        choix: [{choix_str}],
        reponse: {reponse},
        explication: "{explication}",
      }}'''

new_questions = {
    'neutres-deuxieme-declinaison-latin-5e': [
        q("q7", "Quelle est la terminaison du nominatif singulier des neutres de la 2e déclinaison ?", ["-us", "-um", "-a", "-is"], 1, "Les neutres de la 2e déclinaison ont un nominatif singulier en -um, comme templum."),
        q("q8", "Quelle est la règle générale valable pour tous les neutres latins ?", ["Le génitif est toujours en -orum", "Le nominatif et l'accusatif sont toujours identiques", "Le datif n'existe pas", "Ils n'ont pas de pluriel"], 1, "Pour tous les neutres, quelle que soit la déclinaison, le nominatif et l'accusatif sont toujours identiques."),
        q("q9", "Quelle est la terminaison du nominatif et de l'accusatif pluriel des neutres ?", ["-i", "-is", "-a", "-orum"], 2, "Le nominatif et l'accusatif pluriel des neutres se terminent toujours par -a, comme templa."),
        q("q10", "Quel est le génitif singulier de templum ?", ["Templum", "Templo", "Templi", "Templorum"], 2, "Le génitif singulier de templum, templi (le temple) est templi."),
    ],
    'adjectifs-premiere-classe-latin-5e': [
        q("q7", "Sur quel modèle se décline le féminin des adjectifs de la 1ère classe ?", ["Dominus", "Templum", "Rosa", "Rex"], 2, "Le féminin des adjectifs de la 1ère classe se décline comme rosa (1ère déclinaison)."),
        q("q8", "Que doit faire un adjectif de la 1ère classe par rapport au nom qu'il qualifie ?", ["Toujours avoir la même terminaison", "S'accorder en genre, nombre et cas", "Se placer juste avant le nom", "Rester invariable"], 1, "L'adjectif doit s'accorder en genre, en nombre et en cas avec le nom qu'il qualifie, même si les terminaisons diffèrent parfois."),
        q("q9", "Pourquoi l'ordre des mots est-il libre en latin ?", ["Car le latin n'a pas de syntaxe", "Car les terminaisons indiquent la fonction grammaticale", "Car le latin n'a pas d'adjectifs", "Car les Romains ne suivaient aucune règle"], 1, "Les terminaisons (déclinaisons) indiquant la fonction grammaticale, l'ordre des mots dans la phrase peut varier librement en latin."),
        q("q10", "Comment accorder « bonus » avec « puella » (une bonne fille) ?", ["Bonus puella", "Bona puella", "Bonum puella", "Boni puella"], 1, "Puella est féminin, donc l'adjectif prend la forme féminine bona : puella bona."),
    ],
    'troisieme-declinaison-latin-5e': [
        q("q7", "Pourquoi le génitif est-il indispensable pour les mots de la 3e déclinaison ?", ["Car le nominatif est très variable", "Car il n'y a pas de nominatif", "Car le génitif est plus court", "Car le latin l'exige par tradition"], 0, "Le nominatif de la 3e déclinaison prend des formes très variables, donc le génitif (qui révèle le radical) est indispensable."),
        q("q9".replace("q9","q9"), "Quel est le radical de rex, regis ?", ["Rex-", "Reg-", "Regi-", "Re-"], 1, "Le radical reg- apparaît au génitif (regis) et dans tous les autres cas sauf le nominatif singulier."),
        q("q9", "Comment un dictionnaire latin présente-t-il un mot de la 3e déclinaison ?", ["Seulement le nominatif", "Le nominatif et le génitif", "Seulement le génitif", "Le nominatif et l'accusatif"], 1, "Le dictionnaire donne toujours le nominatif et le génitif pour les mots de la 3e déclinaison, afin de révéler le radical."),
        q("q10", "Quel est l'accusatif singulier de rex, regis ?", ["Rex", "Regis", "Regem", "Rege"], 2, "L'accusatif singulier de rex, regis (le roi) est regem."),
    ],
    'verbes-ere-ire-latin-5e': [
        q("q7", "Combien de conjugaisons existe-t-il en latin ?", ["Deux", "Trois", "Quatre", "Cinq"], 2, "Le latin compte quatre conjugaisons, distinguées par la terminaison de l'infinitif : -are, -ere, -ere, -ire."),
        q("q8", "À quelle conjugaison appartient monere ?", ["1ère (-are)", "2e (-ere)", "3e (-ere)", "4e (-ire)"], 1, "Monere appartient à la 2e conjugaison, dont l'infinitif se termine par -ēre."),
        q("q9", "Quelle est la 3e personne du pluriel de audire au présent ?", ["Audiunt", "Audient", "Audiant", "Audeunt"], 0, "La 3e personne du pluriel de audire au présent est audiunt, terminaison en -unt comme la 3e conjugaison."),
        q("q10", "Quelle est la 1ère personne du singulier de monere au présent ?", ["Moneo", "Manes", "Monet", "Monemus"], 0, "La 1ère personne du singulier de monere au présent est moneo (j'avertis)."),
    ],
    'imparfait-indicatif-latin-5e': [
        q("q7", "Quel suffixe caractérise l'imparfait latin ?", ["-ba-", "-bi-", "-eb-", "-av-"], 0, "Le suffixe -ba- est caractéristique de l'imparfait, placé entre le radical et les terminaisons personnelles."),
        q("q8", "Quelle est la 1ère personne du singulier d'amare à l'imparfait ?", ["Amo", "Amabam", "Amavi", "Amabo"], 1, "La 1ère personne du singulier d'amare à l'imparfait est amabam (j'aimais)."),
        q("q9", "Quelle valeur exprime généralement l'imparfait latin ?", ["Une action ponctuelle achevée", "Une action durative ou répétée", "Un futur proche", "Un ordre"], 1, "L'imparfait exprime une action durative, répétée, ou décrit un décor, contrairement au parfait qui marque une action achevée."),
        q("q10", "Comment traduit-on « Puer in horto ludebat » ?", ["L'enfant joue dans le jardin", "L'enfant a joué dans le jardin", "L'enfant jouait dans le jardin", "L'enfant jouera dans le jardin"], 2, "Ludebat est un imparfait, qui se traduit par « jouait » : « L'enfant jouait dans le jardin »."),
    ],
    'parfait-indicatif-latin-5e': [
        q("q7", "Que peut exprimer le radical du parfait par rapport au radical du présent ?", ["Il est toujours identique", "Il peut être différent", "Il n'existe pas", "Il est toujours plus court"], 1, "Le parfait utilise souvent un radical différent de celui du présent, à apprendre par cœur pour chaque verbe."),
        q("q8", "Quelle est la terminaison de la 3e personne du pluriel au parfait ?", ["-unt", "-erunt", "-ebant", "-ent"], 1, "La terminaison de la 3e personne du pluriel au parfait est -erunt, comme dans amaverunt."),
        q("q9", "Combien de formes principales donne le dictionnaire pour un verbe latin ?", ["Deux", "Trois", "Quatre", "Cinq"], 2, "Le dictionnaire donne quatre formes principales : l'infinitif présent, le présent, le parfait et le supin."),
        q("q10", "Quelle est la 1ère personne du singulier d'amare au parfait ?", ["Amo", "Amabam", "Amavi", "Amabo"], 2, "La 1ère personne du singulier d'amare au parfait est amavi (j'ai aimé), formée sur le radical amav-."),
    ],
    'composes-sum-latin-5e': [
        q("q7", "Que signifie adsum, adesse ?", ["Pouvoir", "Être présent, assister à", "Être absent", "Poser"], 1, "Adsum, adesse signifie « être présent, assister à », formé du préfixe ad- et de sum."),
        q("q8", "Comment se conjugue adsum au présent ?", ["Comme un verbe irrégulier différent de sum", "Comme sum, avec le préfixe ad-", "Il ne se conjugue pas", "Seulement au pluriel"], 1, "Adsum se conjugue exactement comme sum, en ajoutant simplement le préfixe ad- : adsum, ades, adest, adsumus, adestis, adsunt."),
        q("q9", "Quelle est la 3e personne du pluriel de possum au présent ?", ["Possunt", "Potestis", "Possumus", "Potest"], 0, "La 3e personne du pluriel de possum au présent est possunt (ils peuvent)."),
        q("q10", "Avec quel type de mot s'utilise souvent possum ?", ["Un adjectif", "Un infinitif", "Un génitif", "Un adverbe seul"], 1, "Possum s'utilise souvent avec un infinitif, comme dans « Possum videre » (je peux voir)."),
    ],
    'armee-romaine-legion-latin-5e': [
        q("q7", "Qui commande une centurie ?", ["Un légat", "Un centurion", "Un consul", "Un tribun"], 1, "Une centurie est commandée par un centurion (centurio)."),
        q("q8", "Quel bouclier porte le légionnaire romain ?", ["Le gladius", "Le pilum", "Le scutum", "La lorica"], 2, "Le scutum est le grand bouclier rectangulaire du légionnaire romain."),
        q("q9", "D'où vient le mot français « milice » ?", ["De miles (soldat)", "De legio (légion)", "De centurio", "De decimus"], 0, "Le mot « milice » vient du latin miles, qui signifie « soldat »."),
        q("q10", "D'où vient l'expression « décimer » ?", ["Du châtiment consistant à exécuter un soldat sur dix", "Du nombre de légions", "Du nom d'un général romain", "De la durée du service militaire"], 0, "« Décimer » vient du châtiment romain consistant à exécuter un soldat sur dix (decimus) dans une unité jugée coupable de lâcheté."),
    ],
    'jeux-cirque-gladiateurs-latin-5e': [
        q("q7", "Où se déroulaient les combats de gladiateurs ?", ["Dans l'amphithéâtre", "Dans le Circus Maximus", "Sur le Forum", "Dans les thermes"], 0, "Les combats de gladiateurs (munera) se déroulaient dans l'amphithéâtre, comme le Colisée."),
        q("q8", "Quel équipement caractérise le retiarius ?", ["Un grand bouclier et une épée courte", "Un filet et un trident", "Une épée courbe", "Une lance et une armure lourde"], 1, "Le retiarius combattait avec un filet et un trident."),
        q("q9", "Où se déroulaient les courses de chars ?", ["Dans l'amphithéâtre", "Au Circus Maximus", "Sur le Forum", "Dans les thermes"], 1, "Les courses de chars (ludi circenses) se déroulaient au Circus Maximus, un immense hippodrome."),
        q("q10", "Environ combien de spectateurs pouvait accueillir le Circus Maximus ?", ["15 000", "50 000", "150 000", "500 000"], 2, "Le Circus Maximus pouvait accueillir environ 150 000 spectateurs."),
    ],
}

for slug, qs in new_questions.items():
    idx = txt.index(f'slug: "{slug}"')
    window = txt[idx:idx+9000]
    close_marker = "\n    ],\n  },\n  },"
    close_idx_rel = window.index(close_marker)
    abs_close_idx = idx + close_idx_rel
    insertion = ",\n" + ",\n".join(qs)
    txt = txt[:abs_close_idx] + insertion + txt[abs_close_idx:]

with open(path, 'w') as f:
    f.write(txt)

print("done")
