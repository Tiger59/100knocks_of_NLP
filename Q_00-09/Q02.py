word1 = 'パトカー'
word2 = 'タクシー'
s = ''.join(c1 + c2 for c1, c2 in zip(word1, word2))

print(s)