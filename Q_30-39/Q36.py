from Q30 import load_mecab
path = '../data/neko.txt.mecab'
count_dict={}
for i in load_mecab(path):
    for j in i:
        if(j['surface'] not in count_dict):
            count_dict[j['surface']]=1
        else:
            count_dict[j['surface']]+=1
for k,v in sorted(count_dict.items(), key=lambda x: -x[1]):
    print(str(k)+" : "+str(v))
