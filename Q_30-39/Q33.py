from Q30 import load_mecab
path = '../data/neko.txt.mecab'
for i in load_mecab(path):
    for j in i:
        if(j['pos1']=='サ変接続'):
            print(j['surface'])