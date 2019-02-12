def translate_tab2space(path):
    s = open(path, encoding='utf-8').read()
    replaced = s.replace("\t", " ")
    return replaced

print(translate_tab2space(path))