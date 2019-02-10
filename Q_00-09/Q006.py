def seq2charbigram(seq):
    charngram = {seq[i:i + 2] for i in range(len(seq) - 2 + 1)}
    return (charngram)


sent1 = "paraparaparadise"
sent2 = "paragraph"
X = seq2charbigram(sent1)
Y = seq2charbigram(sent2)
print(X | Y)
print(X & Y)
print(X - Y)
