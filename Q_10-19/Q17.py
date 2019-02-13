def print_distinct(filepath):
    lines = open(filepath, encoding='utf-8').readlines()
    distinct_list ={line.split()[0] for line in lines}
    print(distinct_list)

filepath = "data/hightemp.txt"
print_distinct(filepath)