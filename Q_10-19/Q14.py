def output_head_lines(path,n):
    lines = open(path, encoding='utf-8').readlines()
    for i in range(int(n)):
        print(lines[i],end="")

path="data/hightemp.txt"
N=input("How long lines? : ")
output_heads_lines(path,N)
