def count_line(path):
    return sum([1 for line in open(path)])

print(count_line('data/hightemp.txt'))