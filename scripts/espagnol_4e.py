# -*- coding: utf-8 -*-
PATH = "src/content/lessons.ts"

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def lesson_block(d):
    obj = ", ".join('"' + esc(o) + '"' for o in d["objectifs"])
    cont = ", ".join('"' + esc(c) + '"' for c in d["contenu"])
    q_items = []
    for q in d["quiz"]:
        choix = ", ".join('"' + esc(c) + '"' for c in q["choix"])
        expl = esc(q["explication"])
        enonce = esc(q["enonce"])
        q_items.append(
            f'      {{\n        id: "{q["id"]}",\n        enonce: "{enonce}",\n'
            f'        choix: [{choix}],\n        reponse: {q["reponse"]},\n'
            f'        explication: "{expl}",\n      }}'
        )
    quiz_block = (
        f'quiz: {{\n    slug: "quiz-{d["slug"]}",\n    titre: "Quiz — {esc(d["titre"])}",\n'
        f'    questions: [\n' + ",\n".join(q_items) + "\n    ],\n  },"
    )
    return (
        f'  {{\n    slug: "{d["slug"]}",\n    titre: "{esc(d["titre"])}",\n'
        f'    matiere: "{d["matiere"]}",\n    niveau: "{d["niveau"]}",\n'
        f'    duree: "{d["duree"]}",\n    resume: "{esc(d["resume"])}",\n'
        f'    objectifs: [{obj}],\n    contenu: [{cont}],\n    {quiz_block}\n  }},'
    )

def insert_after(txt, anchor_slug, new_dicts):
    start = txt.index(f'  {{\n    slug: "{anchor_slug}",')
    nxt = txt.index('\n  {\n    slug:', start + 10)
    insertion = "\n" + "\n".join(lesson_block(d) for d in new_dicts)
    return txt[:nxt] + insertion + txt[nxt:]

L = []

L.append({
    "slug": "deber-tener-que-obligacion-espagnol-4e", "titre": "Deber, tener que y el condicional de consejo",
    "matiere": "espagnol", "niveau": "4e", "duree": "20 min",
    "resume": "Saber expresar la obligacion y el consejo en espanol con deber, tener que y el condicional.",
    "objectifs": ["Conjugar y usar el verbo tener que", "Usar deber + infinitivo para una obligacion", "Usar el condicional para dar un consejo (deberias)"],
    "contenu": [
        "Tener que + infinitivo expresa una obligacion fuerte, muy usada en espanol : Tengo que terminar mis deberes. Tengo, tienes, tiene, tenemos, teneis, tienen que + infinitivo. Es la forma mas frecuente para expresar una obligacion en el habla cotidiana.",
        "Deber + infinitivo tambien expresa una obligacion, a menudo un poco mas formal o moral : Debes respetar las reglas. Se conjuga como un verbo regular en -er : debo, debes, debe, debemos, debeis, deben.",
        "Para dar un consejo mas suave que una obligacion, se usa el condicional de deber : deberias (tu), deberia (el/ella), deberiais (vosotros). Ejemplo : Deberias estudiar mas. Esta forma corresponde al « tu devrais » frances o al should ingles.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Como se dice « je dois » (obligacion frecuente) en espanol ?", "choix": ["Tengo que", "Debo", "Deberia", "Tenia que"], "reponse": 0, "explication": "Tengo que es la forma mas frecuente para expresar una obligacion en espanol cotidiano."},
        {"id": "q2", "enonce": "Que preposicion sigue siempre a tener en esta estructura ?", "choix": ["Que", "De", "Para", "Con"], "reponse": 0, "explication": "Tener que + infinitivo es la estructura correcta para expresar obligacion."},
        {"id": "q3", "enonce": "Como se conjuga deber en la primera persona del singular ?", "choix": ["Debo", "Deo", "Debio", "Debia"], "reponse": 0, "explication": "Debo es la primera persona singular del verbo deber, presente de indicativo."},
        {"id": "q4", "enonce": "Que expresa deber + infinitivo ?", "choix": ["Una obligacion, a menudo formal o moral", "Un deseo", "Una posibilidad", "Un pasado"], "reponse": 0, "explication": "Deber + infinitivo expresa una obligacion, a menudo mas formal o moral que tener que."},
        {"id": "q5", "enonce": "Como se dice « tu devrais » (consejo) en espanol ?", "choix": ["Deberias", "Debes", "Deberiais", "Debias"], "reponse": 0, "explication": "Deberias es el condicional de deber, usado para dar un consejo."},
        {"id": "q6", "enonce": "Que tiempo verbal se usa para dar un consejo mas suave que una obligacion ?", "choix": ["El presente de indicativo", "El condicional", "El imperativo", "El futuro"], "reponse": 1, "explication": "El condicional (deberias, deberia) expresa un consejo mas suave que una obligacion directa."},
        {"id": "q7", "enonce": "Completa : « ___ estudiar mas si quieres aprobar. » (consejo)", "choix": ["Deberias", "Tienes que", "Debes", "Tenias que"], "reponse": 0, "explication": "Deberias (condicional) es adecuado para dar un consejo personalizado."},
        {"id": "q8", "enonce": "Cual es el infinitivo de « tengo »?", "choix": ["Tener", "Tenir", "Tenar", "Tenor"], "reponse": 0, "explication": "Tengo es la primera persona singular del verbo tener."},
        {"id": "q9", "enonce": "Tener que es una estructura formal o muy usada en el habla cotidiana ?", "choix": ["Muy usada en el habla cotidiana", "Solo en textos formales", "Nunca se usa", "Solo en el pasado"], "reponse": 0, "explication": "Tener que es la estructura mas frecuente y usada en el habla cotidiana para expresar obligacion."},
        {"id": "q10", "enonce": "Completa : « Debes respetar las reglas » expresa :", "choix": ["Una obligacion", "Una pregunta", "Un deseo", "Un pasado"], "reponse": 0, "explication": "Deber + infinitivo expresa aqui una obligacion clara."},
    ],
})

L.append({
    "slug": "futuro-simple-espagnol-4e", "titre": "El futuro simple",
    "matiere": "espagnol", "niveau": "4e", "duree": "20 min",
    "resume": "Saber formar y usar el futuro simple para hablar de proyectos y predicciones.",
    "objectifs": ["Formar el futuro simple de los verbos regulares", "Conocer los principales futuros irregulares", "Usar el futuro para expresar un proyecto o una prediccion"],
    "contenu": [
        "El futuro simple se forma anadiendo las terminaciones -e, -as, -a, -emos, -eis, -an directamente al infinitivo del verbo, sin cambios, para los verbos regulares : hablar → hablare, hablaras, hablara, hablaremos, hablareis, hablaran.",
        "Muchos verbos comunes tienen un futuro irregular, con una raiz modificada pero las mismas terminaciones : tener → tendre, poner → pondre, salir → saldre, hacer → hare, decir → dire, poder → podre, querer → querre, saber → sabre.",
        "El futuro simple se usa para hablar de un proyecto futuro (Manana ire al mercado), para hacer una prediccion (Manana llovera), o para expresar una suposicion sobre el presente (Seran las doce, no tengo reloj).",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Como se forma el futuro simple de los verbos regulares ?", "choix": ["Se anaden las terminaciones directamente al infinitivo", "Se quita la terminacion del infinitivo", "Se usa siempre el verbo haber", "No existe futuro simple en espanol"], "reponse": 0, "explication": "Para los verbos regulares, las terminaciones del futuro se anaden directamente al infinitivo."},
        {"id": "q2", "enonce": "Cual es el futuro de « hablar » en la primera persona ?", "choix": ["Hablare", "Hablo", "Hablaba", "Hable"], "reponse": 0, "explication": "Hablare es la primera persona singular del futuro de hablar."},
        {"id": "q3", "enonce": "Cual es el futuro del verbo tener en la primera persona ?", "choix": ["Tendre", "Tenere", "Tengo", "Tenia"], "reponse": 0, "explication": "El futuro de tener es irregular : tendre."},
        {"id": "q4", "enonce": "Cual es el futuro del verbo hacer en la primera persona ?", "choix": ["Hare", "Hacere", "Hago", "Hacia"], "reponse": 0, "explication": "El futuro de hacer es irregular : hare."},
        {"id": "q5", "enonce": "Cual es el futuro del verbo poder en la primera persona ?", "choix": ["Podre", "Podere", "Puedo", "Podia"], "reponse": 0, "explication": "El futuro de poder es irregular : podre."},
        {"id": "q6", "enonce": "Cual es el futuro del verbo salir en la primera persona ?", "choix": ["Saldre", "Salire", "Salgo", "Salia"], "reponse": 0, "explication": "El futuro de salir es irregular : saldre."},
        {"id": "q7", "enonce": "Para que se usa el futuro simple ?", "choix": ["Para un proyecto futuro o una prediccion", "Solo para el pasado", "Solo para una accion habitual", "Solo para una orden"], "reponse": 0, "explication": "El futuro simple se usa para expresar un proyecto futuro o hacer una prediccion."},
        {"id": "q8", "enonce": "Completa : « Manana ___ (llover). »", "choix": ["llovera", "llovio", "llueve", "llovia"], "reponse": 0, "explication": "Llover es regular en el futuro : llovera."},
        {"id": "q9", "enonce": "El futuro puede expresar una suposicion sobre el presente ?", "choix": ["No, nunca", "Si, por ejemplo « seran las doce »", "Solo en el pasado", "Solo con el imperativo"], "reponse": 1, "explication": "El futuro puede expresar una suposicion sobre el presente, como « seran las doce »."},
        {"id": "q10", "enonce": "Cual es la terminacion del futuro en la tercera persona plural ?", "choix": ["-an", "-emos", "-eis", "-aban"], "reponse": 0, "explication": "La tercera persona plural del futuro tiene la terminacion -an."},
    ],
})

L.append({
    "slug": "voz-pasiva-espagnol-4e", "titre": "La voz pasiva : introduccion",
    "matiere": "espagnol", "niveau": "4e", "duree": "20 min",
    "resume": "Comprender el principio de la voz pasiva y saber formarla con ser + participio.",
    "objectifs": ["Distinguir la voz activa y la voz pasiva", "Formar la voz pasiva con ser + participio pasado", "Conocer la pasiva refleja con se como alternativa"],
    "contenu": [
        "En la voz activa, el sujeto realiza la accion : El cocinero prepara la cena. En la voz pasiva, el sujeto recibe la accion, y el interes se centra en la accion misma : La cena es preparada (por el cocinero).",
        "La voz pasiva se construye con el verbo ser conjugado en el tiempo deseado, seguido del participio pasado del verbo, que concuerda en genero y numero con el sujeto : La carta es escrita. Las cartas son escritas. El agente, si se menciona, se introduce con por : La carta es escrita por Marco.",
        "En espanol, es muy frecuente usar la pasiva refleja con se en lugar de la voz pasiva con ser, sobre todo cuando el agente no importa : Se vende esta casa. Se hablan varios idiomas aqui. Esta forma es mas natural y mas usada que la pasiva con ser en el habla cotidiana.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "En la voz activa, que hace el sujeto ?", "choix": ["Realiza la accion", "Recibe la accion", "No hace nada", "Siempre es plural"], "reponse": 0, "explication": "En la voz activa, el sujeto realiza la accion."},
        {"id": "q2", "enonce": "Como se forma la voz pasiva con ser ?", "choix": ["Ser + participio pasado", "Haber + infinitivo", "Estar + gerundio", "Ir + participio"], "reponse": 0, "explication": "La voz pasiva se construye con ser seguido del participio pasado."},
        {"id": "q3", "enonce": "Con que concuerda el participio pasado en la voz pasiva ?", "choix": ["Con el sujeto, en genero y numero", "Nunca concuerda", "Con el agente", "Con el verbo haber"], "reponse": 0, "explication": "El participio pasado concuerda con el sujeto en genero y numero en la voz pasiva."},
        {"id": "q4", "enonce": "Que preposicion introduce el agente en la voz pasiva ?", "choix": ["Por", "De", "A", "Con"], "reponse": 0, "explication": "El agente se introduce con la preposicion por : escrita por Marco."},
        {"id": "q5", "enonce": "Transforma a la voz pasiva : « El cocinero prepara la cena. »", "choix": ["La cena es preparada por el cocinero.", "El cocinero es preparado por la cena.", "La cena prepara al cocinero.", "El cocinero preparara la cena."], "reponse": 0, "explication": "« La cena es preparada por el cocinero » es la forma pasiva correcta."},
        {"id": "q6", "enonce": "Que es la pasiva refleja ?", "choix": ["Una construccion con se, muy usada en espanol", "Una forma del futuro", "Un tiempo verbal compuesto", "Una forma del imperativo"], "reponse": 0, "explication": "La pasiva refleja con se es una construccion muy usada en espanol para expresar una accion sin insistir en el agente."},
        {"id": "q7", "enonce": "Cual de estas frases es un ejemplo de pasiva refleja ?", "choix": ["Se vende esta casa.", "La casa es vendida por el agente.", "El agente vende la casa.", "La casa vendera al agente."], "reponse": 0, "explication": "« Se vende esta casa » es un ejemplo tipico de pasiva refleja con se."},
        {"id": "q8", "enonce": "Completa : « Las cartas ___ escritas. » (plural femenino)", "choix": ["son", "es", "eres", "somos"], "reponse": 0, "explication": "Con un sujeto plural, se usa son seguido del participio concordado : escritas."},
        {"id": "q9", "enonce": "El agente debe mencionarse siempre en la voz pasiva ?", "choix": ["Si, siempre obligatorio", "No, puede omitirse", "Solo en presente", "Solo en pasado"], "reponse": 1, "explication": "El agente puede omitirse si no es importante o es desconocido."},
        {"id": "q10", "enonce": "Que forma es mas frecuente en el espanol cotidiano, la pasiva con ser o la pasiva refleja con se ?", "choix": ["La pasiva refleja con se", "La pasiva con ser", "Ambas son igual de raras", "Ninguna se usa"], "reponse": 0, "explication": "La pasiva refleja con se es mas natural y mas usada que la pasiva con ser en el habla cotidiana."},
    ],
})

L.append({
    "slug": "estilo-indirecto-espagnol-4e", "titre": "El estilo indirecto",
    "matiere": "espagnol", "niveau": "4e", "duree": "20 min",
    "resume": "Saber transmitir las palabras de alguien usando el estilo indirecto en espanol.",
    "objectifs": ["Comprender el principio del estilo indirecto", "Transformar una frase del estilo directo al indirecto", "Conocer los principales cambios de tiempo verbal"],
    "contenu": [
        "El estilo directo transmite las palabras exactas de alguien entre comillas : Maria dice: « Estoy cansada. » El estilo indirecto transmite esas mismas palabras sin comillas, introducidas por un verbo como decir seguido de que : Maria dice que esta cansada.",
        "Cuando el verbo introductor esta en presente (dice que), el tiempo de la frase transmitida generalmente no cambia. Pero cuando el verbo introductor esta en pasado (dijo que), el tiempo suele retroceder : el presente se convierte en imperfecto, el preterito perfecto compuesto en pluscuamperfecto, el futuro en condicional.",
        "Los pronombres y los indicadores de tiempo o lugar tambien cambian a menudo : yo se convierte en el/ella, aqui se convierte en alli, manana se convierte en al dia siguiente. Ejemplo : Marco dijo: « Vendre manana » se convierte en Marco dijo que vendria al dia siguiente.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Que es el estilo directo ?", "choix": ["Transmitir las palabras exactas entre comillas", "Transmitir palabras sin comillas", "Una forma del futuro", "Un tipo de pregunta"], "reponse": 0, "explication": "El estilo directo transmite las palabras exactas de alguien entre comillas."},
        {"id": "q2", "enonce": "Que es el estilo indirecto ?", "choix": ["Transmitir palabras entre comillas", "Transmitir palabras sin comillas, introducidas por que", "Una orden directa", "Una pregunta directa"], "reponse": 1, "explication": "El estilo indirecto transmite palabras sin comillas, introducidas por un verbo seguido de que."},
        {"id": "q3", "enonce": "Si el verbo introductor esta en presente, el tiempo de la frase transmitida cambia generalmente ?", "choix": ["Si, siempre", "No, generalmente no cambia", "Siempre al futuro", "Siempre al pasado"], "reponse": 1, "explication": "Si el verbo introductor esta en presente, el tiempo de la frase transmitida generalmente no cambia."},
        {"id": "q4", "enonce": "Que se convierte el presente cuando el verbo introductor esta en pasado ?", "choix": ["El imperfecto", "El futuro", "El condicional", "No cambia"], "reponse": 0, "explication": "Cuando el verbo introductor esta en pasado, el presente se convierte generalmente en imperfecto."},
        {"id": "q5", "enonce": "Que se convierte el futuro simple en estilo indirecto con un verbo introductor en pasado ?", "choix": ["El condicional", "El presente", "El imperfecto", "No cambia"], "reponse": 0, "explication": "El futuro se convierte generalmente en condicional cuando el verbo introductor esta en pasado."},
        {"id": "q6", "enonce": "Transforma : Maria dice: « Estoy cansada. » →", "choix": ["Maria dice que esta cansada.", "Maria dice que estaba cansada.", "Maria dira que esta cansada.", "Maria dijo estoy cansada."], "reponse": 0, "explication": "Con un verbo introductor en presente, el tiempo no cambia : Maria dice que esta cansada."},
        {"id": "q7", "enonce": "Que se convierte « manana » en estilo indirecto pasado ?", "choix": ["Al dia siguiente", "Ayer", "Hoy", "Sigue siendo manana"], "reponse": 0, "explication": "Manana se convierte generalmente en « al dia siguiente » en estilo indirecto pasado."},
        {"id": "q8", "enonce": "Que se convierte « aqui » en estilo indirecto ?", "choix": ["Alli", "Aqui (sin cambio)", "Ahora", "Entonces"], "reponse": 0, "explication": "Aqui se convierte generalmente en alli en estilo indirecto."},
        {"id": "q9", "enonce": "Transforma : Marco dijo: « Vendre manana. » →", "choix": ["Marco dijo que vendria al dia siguiente.", "Marco dijo que viene manana.", "Marco dice que vendra manana.", "Marco dijo que ha venido manana."], "reponse": 0, "explication": "El futuro se convierte en condicional, y manana en al dia siguiente."},
        {"id": "q10", "enonce": "Que conjuncion introduce generalmente el estilo indirecto en espanol ?", "choix": ["Que", "Si", "Porque", "Cuando"], "reponse": 0, "explication": "La conjuncion que introduce generalmente el estilo indirecto despues de un verbo como decir."},
    ],
})

L.append({
    "slug": "primera-condicional-espagnol-4e", "titre": "La primera condicional (si + presente, futuro)",
    "matiere": "espagnol", "niveau": "4e", "duree": "20 min",
    "resume": "Saber expresar una condicion realizable con la estructura si + presente + futuro.",
    "objectifs": ["Comprender el uso de la primera condicional", "Formar una frase con si + presente + futuro", "Distinguir una condicion real de una condicion irreal"],
    "contenu": [
        "La primera condicional expresa una condicion realizable y su consecuencia probable en el futuro : Si llueve manana, nos quedaremos en casa. Se compone de dos partes : la proposicion con si en presente de indicativo, y la proposicion principal en futuro simple.",
        "El orden de las dos proposiciones puede invertirse sin cambiar el sentido : Si estudias, aprobaras el examen. equivale a Aprobaras el examen si estudias. Cuando la proposicion con si se coloca primero, se separa de la principal con una coma.",
        "La primera condicional se usa para situaciones realmente posibles, a diferencia de la segunda condicional (si + imperfecto de subjuntivo, condicional) que expresa una situacion hipotetica o poco probable : Si ganara la loteria, viajaria por el mundo.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Para que sirve la primera condicional ?", "choix": ["Expresar una condicion realizable y su consecuencia", "Expresar un hecho pasado", "Expresar un habito", "Expresar una orden"], "reponse": 0, "explication": "La primera condicional expresa una condicion realizable y su consecuencia probable en el futuro."},
        {"id": "q2", "enonce": "Cual es la estructura de la primera condicional ?", "choix": ["Si + presente, futuro", "Si + imperfecto de subjuntivo, condicional", "Si + futuro, presente", "Si + condicional, presente"], "reponse": 0, "explication": "La estructura es si + presente de indicativo, futuro simple en la proposicion principal."},
        {"id": "q3", "enonce": "Completa : « Si ___ manana, nos quedaremos en casa. »", "choix": ["llueve", "llovera", "lloviera", "llovia"], "reponse": 0, "explication": "Despues de si en la primera condicional, se usa el presente de indicativo : llueve."},
        {"id": "q4", "enonce": "Completa : « Si estudias, ___ el examen. »", "choix": ["apruebas", "aprobaras", "aprobaras", "aprobabas"], "reponse": 1, "explication": "En la proposicion principal se usa el futuro simple : aprobaras."},
        {"id": "q5", "enonce": "La primera condicional expresa una situacion realizable o hipotetica ?", "choix": ["Realizable", "Hipotetica y poco probable", "Imposible", "Pasada"], "reponse": 0, "explication": "La primera condicional expresa una situacion realmente posible."},
        {"id": "q6", "enonce": "Que estructura expresa una situacion hipotetica poco probable ?", "choix": ["Si + presente, futuro", "Si + imperfecto de subjuntivo, condicional", "Si + indicativo pasado, presente", "Si + gerundio, futuro"], "reponse": 1, "explication": "La segunda condicional (si + imperfecto de subjuntivo, condicional) expresa una situacion hipotetica poco probable."},
        {"id": "q7", "enonce": "Se necesita una coma cuando la proposicion con si se coloca primero ?", "choix": ["Si", "No, nunca", "Solo oralmente", "Depende del verbo"], "reponse": 0, "explication": "Una coma separa las dos proposiciones cuando la que tiene si se coloca primero."},
        {"id": "q8", "enonce": "Que significa « si » en esta estructura ?", "choix": ["Si (condicion)", "Cuando", "Aunque", "Porque"], "reponse": 0, "explication": "Si introduce la condicion en esta estructura."},
        {"id": "q9", "enonce": "Se puede invertir el orden de las dos proposiciones sin cambiar el sentido ?", "choix": ["Si", "No, nunca", "Solo en pasado", "Solo con subjuntivo"], "reponse": 0, "explication": "El orden de las dos proposiciones puede invertirse sin cambiar el sentido general."},
        {"id": "q10", "enonce": "Completa correctamente : « Ganare la carrera si me ___ mucho. » (entrenar, presente)", "choix": ["entreno", "entrenare", "entrenara", "entrenaba"], "reponse": 0, "explication": "Despues de si, se usa el presente de indicativo : me entreno."},
    ],
})

L.append({
    "slug": "pronombres-relativos-espagnol-4e", "titre": "Los pronombres relativos que, quien, el cual",
    "matiere": "espagnol", "niveau": "4e", "duree": "20 min",
    "resume": "Saber usar los pronombres relativos que, quien y el cual para unir dos ideas en una frase.",
    "objectifs": ["Usar que como sujeto o complemento", "Usar quien despues de una preposicion referida a personas", "Conocer el uso de el cual como alternativa mas formal"],
    "contenu": [
        "El pronombre relativo que es el mas usado en espanol : es invariable y puede referirse tanto a personas como a cosas, como sujeto (La mujer que vive aqui es medica) o como complemento (El libro que lei era genial) de la oracion de relativo.",
        "Despues de una preposicion, cuando el antecedente es una persona, se usa a menudo quien (o quienes en plural) en lugar de que : La persona a quien escribi es mi tia. Quien concuerda en numero, pero no en genero, con su antecedente.",
        "El cual (la cual, los cuales, las cuales) puede sustituir a que o quien, sobre todo en un estilo mas formal o escrito, y concuerda en genero y numero con el nombre al que se refiere : El hombre, el cual vive aqui, es medico. Con una preposicion : la persona a la cual escribi.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Cual es el pronombre relativo mas usado en espanol ?", "choix": ["Que", "Quien", "El cual", "Cuyo"], "reponse": 0, "explication": "Que es el pronombre relativo mas usado en espanol, invariable."},
        {"id": "q2", "enonce": "Que puede referirse tanto a personas como a cosas ?", "choix": ["Si", "No, solo a cosas", "No, solo a personas", "Nunca a personas"], "reponse": 0, "explication": "Que puede referirse tanto a personas como a cosas en espanol."},
        {"id": "q3", "enonce": "Que pronombre se usa a menudo despues de una preposicion cuando el antecedente es una persona ?", "choix": ["Quien", "Que", "Cuyo", "Cual"], "reponse": 0, "explication": "Quien se usa a menudo despues de una preposicion cuando el antecedente es una persona."},
        {"id": "q4", "enonce": "Completa : « El libro ___ lei era genial. » (complemento)", "choix": ["que", "quien", "el cual", "cuyo"], "reponse": 0, "explication": "Que se usa aqui como complemento, sin preposicion."},
        {"id": "q5", "enonce": "Completa : « La persona a ___ escribi es mi tia. »", "choix": ["que", "quien", "cual", "cuya"], "reponse": 1, "explication": "Despues de una preposicion (a) con un antecedente persona, se usa quien."},
        {"id": "q6", "enonce": "El cual concuerda en genero y numero ?", "choix": ["Si", "No, es invariable", "Solo en plural", "Solo en femenino"], "reponse": 0, "explication": "El cual (la cual, los cuales, las cuales) concuerda en genero y numero con el nombre al que se refiere."},
        {"id": "q7", "enonce": "En que registro se usa particularmente el cual ?", "choix": ["Un estilo mas formal y escrito", "Solo en el habla informal", "Solo con ninos", "Nunca se usa en espanol"], "reponse": 0, "explication": "El cual se usa particularmente en un estilo mas formal o escrito."},
        {"id": "q8", "enonce": "Quien concuerda en genero con su antecedente ?", "choix": ["No, solo en numero", "Si, siempre", "Solo en plural", "Nunca concuerda"], "reponse": 0, "explication": "Quien concuerda en numero (quien/quienes), pero no en genero, con su antecedente."},
        {"id": "q9", "enonce": "Que puede ser sujeto de una oracion de relativo ?", "choix": ["Si", "No, nunca", "Solo en pasado", "Solo con quien"], "reponse": 0, "explication": "Que puede ser sujeto de la oracion de relativo, como en « La mujer que vive aqui »."},
        {"id": "q10", "enonce": "Cual pronombre relativo es invariable ?", "choix": ["Que", "El cual unicamente", "Ninguno es invariable", "Solo quien"], "reponse": 0, "explication": "Que es invariable, a diferencia de quien (numero) y el cual (genero y numero)."},
    ],
})

L.append({
    "slug": "expresar-cantidad-espagnol-4e", "titre": "Expresar la cantidad : mucho, poco, demasiado",
    "matiere": "espagnol", "niveau": "4e", "duree": "20 min",
    "resume": "Saber usar los indicadores de cantidad mucho, poco, demasiado y bastante en espanol.",
    "objectifs": ["Usar mucho, poco, demasiado como adjetivos y adverbios", "Concordar correctamente estos indicadores cuando son adjetivos", "Conocer bastante y su uso"],
    "contenu": [
        "Mucho, poco y demasiado pueden usarse como adjetivos, y en ese caso concuerdan en genero y numero con el sustantivo : Tengo muchos amigos. Tengo poca paciencia. Como cuanto en exceso : Como demasiados dulces.",
        "Mucho, poco y demasiado tambien pueden usarse como adverbios, para modificar un verbo o un adjetivo : en ese caso, quedan invariables en la forma masculina singular. Estoy muy cansado (con el adverbio muy, forma corta de mucho). He dormido poco. Eres demasiado rapido.",
        "Bastante es invariable en genero, pero varia en numero (bastante/bastantes) : Tengo bastante dinero. Tengo bastantes amigos. La distincion entre la funcion adjetival (concordancia) y la funcion adverbial es esencial para usar correctamente estos indicadores de cantidad.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Mucho concuerda cuando se usa como adjetivo ?", "choix": ["Si", "No, nunca", "Solo en plural", "Solo en femenino"], "reponse": 0, "explication": "Como adjetivo, mucho concuerda en genero y numero con el sustantivo."},
        {"id": "q2", "enonce": "Completa : « Tengo much___ amigos. » (concordancia)", "choix": ["os", "o", "a", "as"], "reponse": 0, "explication": "Muchos amigos : el adjetivo concuerda en masculino plural."},
        {"id": "q3", "enonce": "Completa : « Tengo poc___ paciencia. » (concordancia)", "choix": ["a", "o", "os", "as"], "reponse": 0, "explication": "Poca paciencia : el adjetivo concuerda en femenino singular."},
        {"id": "q4", "enonce": "Cual es la forma adverbial corta de mucho delante de un adjetivo ?", "choix": ["Muy", "Mucho", "Mas", "Tan"], "reponse": 0, "explication": "Muy es la forma adverbial corta usada delante de un adjetivo : muy cansado."},
        {"id": "q5", "enonce": "En la frase « Estoy muy cansado », muy es adjetivo o adverbio ?", "choix": ["Adjetivo", "Adverbio", "Sustantivo", "Preposicion"], "reponse": 1, "explication": "Aqui, muy modifica el adjetivo cansado, es por tanto un adverbio."},
        {"id": "q6", "enonce": "En la frase « Tengo muchos amigos », muchos es adjetivo o adverbio ?", "choix": ["Adjetivo", "Adverbio", "Pronombre", "Preposicion"], "reponse": 0, "explication": "Aqui, muchos acompana y concuerda con el sustantivo amigos, es por tanto un adjetivo."},
        {"id": "q7", "enonce": "Bastante varia en genero ?", "choix": ["No, es invariable en genero", "Si, siempre", "Solo en plural", "Solo como adjetivo"], "reponse": 0, "explication": "Bastante es invariable en genero, pero varia en numero : bastante/bastantes."},
        {"id": "q8", "enonce": "Completa : « Como demasiad___ dulces. » (concordancia)", "choix": ["os", "o", "a", "as"], "reponse": 0, "explication": "Demasiados dulces : el adjetivo concuerda en masculino plural."},
        {"id": "q9", "enonce": "Completa : « Eres demasiado rapido. » demasiado es adjetivo o adverbio aqui ?", "choix": ["Adverbio", "Adjetivo", "Sustantivo", "Pronombre"], "reponse": 0, "explication": "Como adverbio (modifica rapido), demasiado queda invariable."},
        {"id": "q10", "enonce": "Que significa bastante ?", "choix": ["Assez", "Beaucoup", "Peu", "Trop"], "reponse": 0, "explication": "Bastante signifie « assez » en francais."},
    ],
})

L.append({
    "slug": "medio-ambiente-desarrollo-sostenible-espagnol-4e", "titre": "El medio ambiente y el desarrollo sostenible",
    "matiere": "espagnol", "niveau": "4e", "duree": "20 min",
    "resume": "Adquirir el vocabulario del medio ambiente y del desarrollo sostenible en espanol.",
    "objectifs": ["Adquirir el vocabulario del medio ambiente", "Saber expresar una opinion sobre un tema ecologico", "Comprender un breve texto sobre el desarrollo sostenible"],
    "contenu": [
        "El vocabulario del medio ambiente incluye palabras esenciales : el cambio climatico, el calentamiento global, la contaminacion, las energias renovables, el reciclaje, las especies en peligro de extincion, el desarrollo sostenible.",
        "Para expresar una opinion sobre un tema ecologico, se pueden usar estructuras como : En mi opinion, deberiamos reducir los residuos de plastico. Creo que las energias renovables son el futuro. Estoy convencido de que todos deberian reciclar.",
        "Muchos paises hispanohablantes llevan a cabo acciones por el medio ambiente : en Costa Rica, mas del noventa por ciento de la electricidad proviene de energias renovables ; en Mexico y Argentina, numerosos parques naturales protegen la biodiversidad frente al cambio climatico.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Como se dice « le changement climatique » en espanol ?", "choix": ["El cambio climatico", "El reciclaje", "La energia solar", "La contaminacion del agua"], "reponse": 0, "explication": "El cambio climatico significa « le changement climatique »."},
        {"id": "q2", "enonce": "Como se dice « les energies renouvelables » ?", "choix": ["Las energias renovables", "La energia nuclear", "El petroleo", "El carbon"], "reponse": 0, "explication": "Las energias renovables significa « les energies renouvelables »."},
        {"id": "q3", "enonce": "Como se dice « les especes menacees » ?", "choix": ["Las especies en peligro de extincion", "Las especies domesticas", "Las especies invasoras", "Solo las plantas"], "reponse": 0, "explication": "Las especies en peligro de extincion significa « les especes menacees »."},
        {"id": "q4", "enonce": "Como se dice « le developpement durable » ?", "choix": ["El desarrollo sostenible", "El calentamiento global", "Los residuos de plastico", "El reciclaje"], "reponse": 0, "explication": "El desarrollo sostenible significa « le developpement durable »."},
        {"id": "q5", "enonce": "Que estructura permite expresar una opinion ?", "choix": ["En mi opinion...", "Habia una vez...", "Como estas?", "Muchas gracias"], "reponse": 0, "explication": "« En mi opinion » es una estructura clasica para expresar una opinion."},
        {"id": "q6", "enonce": "Como se dice « le recyclage » ?", "choix": ["El reciclaje", "El calentamiento", "La deforestacion", "La contaminacion"], "reponse": 0, "explication": "El reciclaje significa « le recyclage »."},
        {"id": "q7", "enonce": "Que pais hispanohablante produce mas del noventa por ciento de su electricidad con energias renovables ?", "choix": ["Costa Rica", "Ningun pais hispanohablante", "Solo Espana", "Solo Mexico"], "reponse": 0, "explication": "Costa Rica produce mas del noventa por ciento de su electricidad a partir de energias renovables."},
        {"id": "q8", "enonce": "Argentina y Mexico protegen la biodiversidad con parques naturales ?", "choix": ["Si", "No, nunca", "Solo Argentina", "Solo Mexico"], "reponse": 0, "explication": "Argentina y Mexico cuentan ambos con numerosos parques naturales que protegen la biodiversidad."},
        {"id": "q9", "enonce": "Como expresar fuertemente una conviccion en espanol ?", "choix": ["Estoy convencido de que...", "Quizas...", "No lo se...", "Tal vez..."], "reponse": 0, "explication": "« Estoy convencido de que » permite expresar fuertemente una conviccion."},
        {"id": "q10", "enonce": "Como se dice « le rechauffement climatique » ?", "choix": ["El calentamiento global", "El reciclaje", "La energia solar", "La biodiversidad"], "reponse": 0, "explication": "El calentamiento global significa « le rechauffement climatique »."},
    ],
})

L.append({
    "slug": "argentina-mexico-cultura-espagnol-4e", "titre": "La cultura de Argentina y Mexico",
    "matiere": "espagnol", "niveau": "4e", "duree": "20 min",
    "resume": "Descubrir elementos culturales y geograficos de Argentina y Mexico, dos grandes paises hispanohablantes.",
    "objectifs": ["Situar Argentina y Mexico y conocer sus capitales", "Descubrir elementos culturales de estos dos paises", "Enriquecer el vocabulario sobre el mundo hispanohablante"],
    "contenu": [
        "Argentina es el segundo pais mas grande de America del Sur, con Buenos Aires como capital. Es conocida por el tango, baile y musica originarios de Buenos Aires, por sus vastas llanuras llamadas la Pampa, y por la Patagonia, una region de paisajes espectaculares en el sur del pais, compartida con Chile.",
        "Mexico, en America del Norte, tiene como capital la Ciudad de Mexico, una de las ciudades mas pobladas del mundo. Mexico es la cuna de civilizaciones antiguas como los mayas y los aztecas, cuyos vestigios se pueden visitar en sitios como Chichen Itza y Teotihuacan. La comida mexicana, como los tacos y el mole, es reconocida como Patrimonio Cultural Inmaterial de la Humanidad por la UNESCO.",
        "Ambos paises tienen una rica tradicion de fiestas populares : en Mexico, el Dia de los Muertos rinde homenaje a los difuntos con altares coloridos ; en Argentina, el asado, una comida a base de carne a la parrilla compartida en familia o entre amigos, es una tradicion social muy importante.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Cual es la capital de Argentina ?", "choix": ["Buenos Aires", "Cordoba", "Mendoza", "Rosario"], "reponse": 0, "explication": "La capital de Argentina es Buenos Aires."},
        {"id": "q2", "enonce": "Cual es la capital de Mexico ?", "choix": ["Guadalajara", "Ciudad de Mexico", "Cancun", "Monterrey"], "reponse": 1, "explication": "La capital de Mexico es la Ciudad de Mexico."},
        {"id": "q3", "enonce": "Que baile y musica son originarios de Buenos Aires ?", "choix": ["El tango", "La salsa", "El flamenco", "La cumbia"], "reponse": 0, "explication": "El tango es originario de Buenos Aires, Argentina."},
        {"id": "q4", "enonce": "Como se llama la vasta llanura argentina ?", "choix": ["La Pampa", "El Amazonas", "El Sahara", "La Patagonia unicamente"], "reponse": 0, "explication": "La Pampa es la vasta llanura fertil d'Argentina."},
        {"id": "q5", "enonce": "Que region del sur de Argentina comparte fronteras con Chile ?", "choix": ["La Patagonia", "El Yucatan", "La Pampa unicamente", "El Peten"], "reponse": 0, "explication": "La Patagonia es una region compartida entre Argentina y Chile, en el sur del continente."},
        {"id": "q6", "enonce": "Que civilizaciones antiguas se desarrollaron en el territorio mexicano ?", "choix": ["Los mayas y los aztecas", "Los incas unicamente", "Los vikingos", "Los romanos"], "reponse": 0, "explication": "Los mayas y los aztecas son civilizaciones antiguas que se desarrollaron en el territorio mexicano."},
        {"id": "q7", "enonce": "Que sitio arqueologico mexicano se puede visitar ?", "choix": ["Chichen Itza", "Machu Picchu", "Las piramides de Guiza", "Stonehenge"], "reponse": 0, "explication": "Chichen Itza es un sitio arqueologico maya que se puede visitar en Mexico."},
        {"id": "q8", "enonce": "Que fiesta mexicana rinde homenaje a los difuntos ?", "choix": ["El Dia de los Muertos", "La Navidad", "El Carnaval", "La Semana Santa unicamente"], "reponse": 0, "explication": "El Dia de los Muertos es una fiesta mexicana que rinde homenaje a los difuntos."},
        {"id": "q9", "enonce": "Que es el asado en Argentina ?", "choix": ["Una comida a base de carne a la parrilla, tradicion social", "Un baile tradicional", "Un tipo de musica", "Una fiesta religiosa"], "reponse": 0, "explication": "El asado es una comida a base de carne a la parrilla, una tradicion social muy importante en Argentina."},
        {"id": "q10", "enonce": "La comida mexicana esta reconocida por la UNESCO ?", "choix": ["Si, como Patrimonio Cultural Inmaterial de la Humanidad", "No, nunca", "Solo los tacos", "Solo en Mexico, no internacionalmente"], "reponse": 0, "explication": "La comida mexicana esta reconocida como Patrimonio Cultural Inmaterial de la Humanidad por la UNESCO."},
    ],
})

L.append({
    "slug": "soler-imperfecto-habitos-pasados-espagnol-4e", "titre": "Soler y el imperfecto para hablar de habitos pasados",
    "matiere": "espagnol", "niveau": "4e", "duree": "20 min",
    "resume": "Saber usar el imperfecto y la perifrasis soler + infinitivo para describir un habito del pasado.",
    "objectifs": ["Formar el imperfecto de los verbos regulares", "Usar el imperfecto para un habito pasado", "Conocer la perifrasis soler + infinitivo"],
    "contenu": [
        "El imperfecto se forma anadiendo las terminaciones -aba, -abas, -aba, -abamos, -abais, -aban para los verbos en -ar, y -ia, -ias, -ia, -iamos, -iais, -ian para los verbos en -er e -ir : hablar → hablaba, hablabas, hablaba... vivir → vivia, vivias, vivia...",
        "El imperfecto se usa en particular para describir un habito o una accion repetida en el pasado, sin precisar cuando empezo o termino : De nino, siempre iba a la playa en verano. Cada dia, comia pasta al mediodia.",
        "La perifrasis soler (en presente o imperfecto) + infinitivo tambien expresa un habito : Solia jugar al futbol los sabados. Esta estructura insiste claramente sobre el caracter habitual de la accion, de forma similar a « avoir l'habitude de » en frances.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Como se forma el imperfecto de los verbos en -ar ?", "choix": ["Con las terminaciones -aba, -abas, -aba...", "Con las terminaciones -ia, -ias, -ia...", "Con el verbo haber", "No existe imperfecto para los verbos en -ar"], "reponse": 0, "explication": "Los verbos en -ar forman el imperfecto con las terminaciones -aba, -abas, -aba, -abamos, -abais, -aban."},
        {"id": "q2", "enonce": "Cual es el imperfecto de « hablar » en la primera persona ?", "choix": ["Hablaba", "Hablare", "He hablado", "Hable"], "reponse": 0, "explication": "Hablaba es la primera persona singular del imperfecto de hablar."},
        {"id": "q3", "enonce": "Para que se usa en particular el imperfecto ?", "choix": ["Para un habito o una accion repetida en el pasado", "Para una accion unica y concluida", "Para el futuro", "Para una orden"], "reponse": 0, "explication": "El imperfecto se usa para describir un habito o una accion repetida en el pasado."},
        {"id": "q4", "enonce": "Completa : « De nino, ___ (ir) siempre a la playa. »", "choix": ["iba", "ire", "he ido", "voy"], "reponse": 0, "explication": "Iba (imperfecto) expresa un habito pasado, sin precision de inicio o fin."},
        {"id": "q5", "enonce": "Que perifrasis tambien expresa un habito pasado ?", "choix": ["Soler + infinitivo", "Ir a + infinitivo", "Acabar de + infinitivo", "Estar + gerundio"], "reponse": 0, "explication": "Soler + infinitivo es una perifrasis que expresa claramente un habito."},
        {"id": "q6", "enonce": "Completa : « ___ jugar al futbol los sabados. » (habito pasado con soler)", "choix": ["Solia", "Suelo", "Sole", "Solere"], "reponse": 0, "explication": "Solia (imperfecto de soler) expresa un habito en el pasado."},
        {"id": "q7", "enonce": "Cual es el imperfecto del verbo ser en la primera persona ?", "choix": ["Era", "Soy", "Sere", "Sea"], "reponse": 0, "explication": "El imperfecto del verbo ser es irregular : era, eras, era..."},
        {"id": "q8", "enonce": "El imperfecto precisa siempre el momento exacto de inicio o fin de una accion ?", "choix": ["No, nunca", "Si, siempre", "Solo en plural", "Solo con haber"], "reponse": 0, "explication": "El imperfecto no precisa el momento exacto de inicio o fin, a diferencia del preterito."},
        {"id": "q9", "enonce": "Cual es la terminacion del imperfecto para los verbos en -ir en la tercera persona singular ?", "choix": ["-ia", "-aba", "-era", "-ira"], "reponse": 0, "explication": "Los verbos en -ir tienen la terminacion -ia en la tercera persona singular del imperfecto."},
        {"id": "q10", "enonce": "Que estructura frances es similar a soler + infinitivo ?", "choix": ["Avoir l'habitude de", "Etre en train de", "Venir de", "Aller vers"], "reponse": 0, "explication": "Soler + infinitivo es similaire a « avoir l'habitude de » en francais."},
    ],
})

L.append({
    "slug": "viajes-vacaciones-vocabulario-espagnol-4e", "titre": "El vocabulario de los viajes y las vacaciones",
    "matiere": "espagnol", "niveau": "4e", "duree": "20 min",
    "resume": "Adquirir el vocabulario necesario para hablar de viajes, vacaciones y experiencias turisticas.",
    "objectifs": ["Adquirir el vocabulario de los viajes", "Saber contar una experiencia de vacaciones", "Comprender un breve relato de viaje"],
    "contenu": [
        "El vocabulario de los viajes incluye palabras esenciales : un vuelo, el equipaje, un pasaporte, un viaje, un alojamiento, un albergue juvenil, hacer turismo, visitar monumentos, un recuerdo, una guia turistica.",
        "Para contar vacaciones pasadas, se usa a menudo el preterito indefinido o el imperfecto : El verano pasado, viajamos a Andalucia. Visitamos muchos castillos y nos alojamos en una pequena casa rural cerca de la costa.",
        "Describir una experiencia turistica implica a menudo expresar una impresion : Fue impresionante! El paisaje era absolutamente espectacular. Me encanto la comida local. Estas expresiones enriquecen un relato de viaje y lo hacen mas vivo y personal.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Como se dice « un vol » en espanol ?", "choix": ["Un vuelo", "Un tren", "Un autobus", "Un barco"], "reponse": 0, "explication": "Un vuelo significa « un vol » en avion."},
        {"id": "q2", "enonce": "Como se dice « les bagages » ?", "choix": ["El equipaje", "El pasaporte", "El billete", "El hotel"], "reponse": 0, "explication": "El equipaje significa « les bagages »."},
        {"id": "q3", "enonce": "Como se dice « l'hebergement » ?", "choix": ["El alojamiento", "El transporte", "La comida", "El clima"], "reponse": 0, "explication": "El alojamiento significa « l'hebergement »."},
        {"id": "q4", "enonce": "Como se dice « une auberge de jeunesse » ?", "choix": ["Un albergue juvenil", "Un hotel de lujo", "Un camping", "Un aeropuerto"], "reponse": 0, "explication": "Un albergue juvenil significa « une auberge de jeunesse »."},
        {"id": "q5", "enonce": "Como se dice « faire du tourisme » ?", "choix": ["Hacer turismo", "Hacer las maletas", "Tomar el avion", "Reservar un hotel"], "reponse": 0, "explication": "Hacer turismo significa « faire du tourisme »."},
        {"id": "q6", "enonce": "Que tiempos se usan a menudo para contar vacaciones pasadas ?", "choix": ["El preterito indefinido y el imperfecto", "Solo el futuro", "Solo el presente", "Solo el imperativo"], "reponse": 0, "explication": "El preterito indefinido y el imperfecto se usan frecuentemente para contar vacaciones pasadas."},
        {"id": "q7", "enonce": "Como se dice « C'etait impressionnant! » ?", "choix": ["Fue impresionante!", "Era aburrido!", "Era cansado!", "Era barato!"], "reponse": 0, "explication": "Impresionante exprime une impression tres positive."},
        {"id": "q8", "enonce": "Como se dice « un souvenir » (objeto) ?", "choix": ["Un recuerdo", "Un pasaporte", "Un vuelo", "Una maleta"], "reponse": 0, "explication": "Un recuerdo designe egalement en espagnol un objet rapporte d'un voyage."},
        {"id": "q9", "enonce": "Como se dice « un guide touristique » ?", "choix": ["Una guia turistica", "Un albergue", "Un equipaje", "Un pasaporte"], "reponse": 0, "explication": "Una guia turistica significa « un guide touristique »."},
        {"id": "q10", "enonce": "Como se dice « L'ete dernier, nous avons voyage en Andalousie » ?", "choix": ["El verano pasado, viajamos a Andalucia.", "El verano proximo, viajaremos a Andalucia.", "Cada verano, viajamos a Andalucia.", "Ahora mismo, viajamos a Andalucia."], "reponse": 0, "explication": "Esta frase en preterito cuenta un viaje pasado datado : « el verano pasado »."},
    ],
})

L.append({
    "slug": "texto-argumentativo-breve-espagnol-4e", "titre": "Escribir un breve texto argumentativo",
    "matiere": "espagnol", "niveau": "4e", "duree": "20 min",
    "resume": "Aprender la estructura de un breve texto argumentativo en espanol para defender una opinion.",
    "objectifs": ["Conocer la estructura de un texto argumentativo sencillo", "Usar conectores logicos para organizar sus ideas", "Saber defender una opinion por escrito en espanol"],
    "contenu": [
        "Un texto argumentativo sencillo en espanol comprende generalmente tres partes : una introduccion que presenta el tema y anuncia la opinion defendida (Hoy en dia, mucha gente piensa que... En este texto, defendere que...), un desarrollo con argumentos y ejemplos, y una conclusion que resume la posicion defendida.",
        "Para organizar sus ideas, se usan conectores logicos : en primer lugar / ademas / finalmente para enumerar argumentos ; sin embargo / por otro lado para matizar o presentar un contraargumento ; por ejemplo para ilustrar una idea ; por lo tanto / en consecuencia para expresar una consecuencia.",
        "Para defender una opinion, se pueden usar expresiones como : Creo que... / En mi opinion... / Estoy convencido de que... Tambien se recomienda, en un texto equilibrado, mencionar brevemente un punto de vista opuesto antes de concluir firmemente sobre la propia posicion : Aunque algunos no esten de acuerdo, sigo pensando que...",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Cuantas partes comprende generalmente un texto argumentativo sencillo ?", "choix": ["Dos", "Tres : introduccion, desarrollo, conclusion", "Cinco", "Una sola"], "reponse": 1, "explication": "Un texto argumentativo sencillo comprende una introduccion, un desarrollo y una conclusion."},
        {"id": "q2", "enonce": "Que significa « en primer lugar » ?", "choix": ["Firstly", "Finally", "However", "For example"], "reponse": 0, "explication": "En primer lugar signifie « premierement », utilise pour introduire un premier argument."},
        {"id": "q3", "enonce": "Que conector permite introducir un contraargumento ?", "choix": ["En primer lugar", "Sin embargo", "Por ejemplo", "Por lo tanto"], "reponse": 1, "explication": "Sin embargo (cependant) permet d'introduire une nuance ou un contre-argument."},
        {"id": "q4", "enonce": "Que conector permite dar un ejemplo ?", "choix": ["Por ejemplo", "Finalmente", "Sin embargo", "Por lo tanto"], "reponse": 0, "explication": "Por ejemplo permet d'illustrer une idee par un exemple."},
        {"id": "q5", "enonce": "Que conector expresa una consecuencia ?", "choix": ["Por lo tanto", "En primer lugar", "Sin embargo", "Por ejemplo"], "reponse": 0, "explication": "Por lo tanto (par consequent) exprime une consequence logique."},
        {"id": "q6", "enonce": "Que expresion permite introducir la propia opinion ?", "choix": ["En mi opinion...", "Habia una vez...", "Fin.", "Como estas?"], "reponse": 0, "explication": "« En mi opinion » est une expression classique pour introduire une opinion personnelle."},
        {"id": "q7", "enonce": "Por que es recomendable mencionar un punto de vista opuesto en un texto equilibrado ?", "choix": ["Nunca es recomendable", "Para mostrar que se han considerado varios angulos antes de concluir", "Para cambiar de opinion al final", "Para llenar espacio"], "reponse": 1, "explication": "Mencionar un punto de vista opuesto muestra una reflexion equilibrada antes de concluir firmemente sobre la propia posicion."},
        {"id": "q8", "enonce": "Que hace la conclusion de un texto argumentativo ?", "choix": ["Resume la posicion defendida", "Introduce un nuevo tema", "Plantea una pregunta sin respuesta", "Enumera solo ejemplos"], "reponse": 0, "explication": "La conclusion resume y confirma la posicion defendida a lo largo del texto."},
        {"id": "q9", "enonce": "Que estructura introduce tipicamente un texto argumentativo ?", "choix": ["En este texto, defendere que...", "Fin.", "Habia una vez...", "Capitulo Uno"], "reponse": 0, "explication": "« En este texto, defendere que » es una formula de introduccion tipica de un texto argumentativo."},
        {"id": "q10", "enonce": "Que significa « por otro lado » ?", "choix": ["On the other hand", "Therefore", "Firstly", "Finally"], "reponse": 0, "explication": "Por otro lado signifie « d'un autre cote », utilise pour nuancer ou opposer une idee."},
    ],
})

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = insert_after(txt, "monumentos-simbolos-hispanos-5e", L)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print(f"{len(L)} lecciones Espanol 4e anadidas.")
