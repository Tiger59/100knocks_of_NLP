from Q30 import load_mecab
path = '../data/neko.txt.mecab'
counter=0
max_count=0
count_list=[]
max_count_list=[]
for i in load_mecab(path):
    for j in i:
        if(j['pos']=='名詞'):
            counter+=1
            count_list.append(j['surface'])
            if(max_count<counter):
                max_count=counter
                max_count_list=count_list
        else:
            counter=0
            count_list=[]
print(max_count)
print(max_count_list)