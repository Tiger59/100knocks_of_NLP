from Q20 import open_england
import re

ptn = re.compile(r'\[\[Category:(.*)\]\]')
print('\n'.join(ptn.search(l).group(1) for l in open_england() if ptn.search(l)))
