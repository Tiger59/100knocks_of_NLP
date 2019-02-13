def output_split_lines(path,n):
    lines = open(path, encoding='utf-8').readlines()
    length = len(lines)/n
    for i,line in enumerate(lines):
        if i%n==0:
            print("")
        print(line,end="")

path="data/hightemp.txt"
N=input("How long lines? : ")
output_split_lines(path,int(N))