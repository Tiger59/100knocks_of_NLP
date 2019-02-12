def separate_columns(path):
    lines = open(path, encoding='utf-8').readlines()
    with open('data/col1.txt', mode='w', encoding='utf-8') as f1, open('data/col2.txt', mode='w', encoding='utf-8') as f2:
        f1.writelines(f'{line.split()[0]}\n' for line in lines)
        f2.writelines(f'{line.split()[1]}\n' for line in lines)

path="data/hightemp.txt"
separate_columns(path)