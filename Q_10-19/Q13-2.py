def merge_columns_and_write(infile1, infile2, outfile):
    col1 = open(infile1, encoding='utf-8').readlines()
    col2 = open(infile2, encoding='utf-8').readlines()
    with open(outfile, mode='w', encoding='utf-8') as f:
        f.writelines(f'{c1.strip()}\t{c2.strip()}\n' for c1, c2 in zip(col1, col2))

file_path1 = "data/col1.txt"
file_path2 = "data/col2.txt"
out_file_path = "data/marge13-2.txt"
merge_columns_and_write(file_path1, file_path2, out_file_path)