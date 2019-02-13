def sort_by_column(filepath, n):
    lines = open(filepath, encoding='utf-8').readlines()
    sorted_list = sorted(lines, key=lambda line:line.split()[n - 1], reverse=True)
    print(''.join(sorted_list))

filepath = "data/hightemp.txt"
n = 3#列目
sort_by_column(filepath, n)