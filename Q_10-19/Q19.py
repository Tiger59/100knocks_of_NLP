def print_sorted(filepath):
    lines = open(filepath, encoding='utf-8').readlines()
    prefectures_list = [line.split()[0] for line in lines]
    count_prefactures={}
    for i in prefectures_list:
        if i not in count_prefactures:
            count_prefactures[i] = 1
        else:
            count_prefactures[i] +=1
    for k, v in sorted(count_prefactures.items(), key=lambda x: -x[1]):
        print(str(v)+" "+str(k))

filepath = "data/hightemp.txt"
print_sorted(filepath)