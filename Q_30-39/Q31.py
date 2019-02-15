from Q30 import load_mecab
path = '../data/neko.txt.mecab'
for i in load_mecab(path):
    for j in i:
        print(j['surface'])