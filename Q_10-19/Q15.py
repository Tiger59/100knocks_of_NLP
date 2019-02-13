def output_tail_lines(path,n):
    lines = open(path, encoding='utf-8').readlines()
    length = len(lines)
    for i,line in enumerate(lines):
        if i >= length-int(n):
            print(line,end="")

path="data/hightemp.txt"
N=input("How long lines? : ")
output_tail_lines(path,N)