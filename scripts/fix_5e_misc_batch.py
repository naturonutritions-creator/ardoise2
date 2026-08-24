import re

path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

slugs = ['pays-anglophones-5e','fetes-traditions-anglophones-5e','monuments-symboles-anglophones-5e','paises-hispanohablantes-5e','fiestas-tradiciones-hispanas-5e','monumentos-simbolos-hispanos-5e','italia-regioni-5e','feste-tradizioni-italiane-5e','monumenti-simboli-italiani-5e']

qblock_re = re.compile(r'\{\s*id: "q\d+",.*?explication: "[^"]*",\s*\}', re.DOTALL)

for s in slugs:
    idx = txt.index(f'slug: "{s}"')
    window = txt[idx:idx+9500]
    close_marker = "\n    ],\n  },\n  },"
    close_idx_rel = window.index(close_marker)
    qarray_marker = "questions: ["
    qarray_start_rel = window.index(qarray_marker) + len(qarray_marker)
    quiz_body = window[qarray_start_rel:close_idx_rel]
    blocks = qblock_re.findall(quiz_body)
    kept = blocks[:10]
    new_blocks = []
    for i, b in enumerate(kept, start=1):
        nb = re.sub(r'id: "(?:extra_)?q\d+"', f'id: "q{i}"', b, count=1)
        new_blocks.append(nb)
    new_quiz_body = "\n      " + ",\n      ".join(new_blocks) + "\n    "
    abs_qarray_start = idx + qarray_start_rel
    abs_close_idx = idx + close_idx_rel
    txt = txt[:abs_qarray_start] + new_quiz_body + txt[abs_close_idx:]

with open(path, 'w') as f:
    f.write(txt)

print("repaired", len(slugs), "lessons")
