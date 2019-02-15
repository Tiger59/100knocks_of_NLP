from Q20.py import open_england
import re
ptn = re.compile(r'\[\[Category:.*?\]\]')
print(''.join(l for l in open_england() if ptn.search(l)))