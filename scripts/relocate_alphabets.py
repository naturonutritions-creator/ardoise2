path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

def extract_and_remove(txt, slug):
    marker = "\n  {\n    "
    idx = txt.index(f'slug: "{slug}"')
    start = txt.rindex(marker, 0, idx) + 1  # start of "  {\n    slug..."
    # find the end: this lesson block ends with "\n  },\n  },\n" right before next "\n  {\n"
    next_marker_idx = txt.index(marker, idx)
    end = next_marker_idx + 1  # up to (not including) the "  {\n    " of next lesson
    block = txt[start:end]
    new_txt = txt[:start] + txt[end:]
    return new_txt, block

txt, esp_block = extract_and_remove(txt, "alfabeto-espagnol-6e")
txt, ita_block = extract_and_remove(txt, "alfabeto-italien-6e")

def insert_before(txt, slug, block):
    marker = "\n  {\n    "
    idx = txt.index(f'slug: "{slug}"')
    pos = txt.rindex(marker, 0, idx) + 1
    return txt[:pos] + block + txt[pos:]

txt = insert_before(txt, "familia-amigos-espagnol-6e", esp_block)
txt = insert_before(txt, "famiglia-amici-italien-6e", ita_block)

with open(path, 'w') as f:
    f.write(txt)
print("relocated")
