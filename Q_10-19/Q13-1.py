def merge_columns(infile1, infile2, outfile):
    col1 = open(infile1, encoding='utf-8').readlines()
    col2 = open(infile2, encoding='utf-8').readlines()
    with open(outfile, mode='w', encoding='utf-8') as f:
        f.writelines(f'{c1.strip()}\t{c2.strip()}\n' for c1, c2 in zip(col1, col2))

file1_path = "data/col1.txt"
file2_path = "data/col2.txt"
output_path="data/marge13-1.txt"
merge_columns(file1_path, file2_path, output_path)