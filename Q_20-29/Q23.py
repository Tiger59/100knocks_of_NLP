from Q20 import open_england
import re
ptn = re.compile(r'(=(=+)(.*?)=\2)')
print('\n'.join(f'{len(ptn.search(l).group(2))}\t{ptn.search(l).group(3)}' for l in open_england() if ptn.search(l)))