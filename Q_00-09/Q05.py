def seq2ngram(seq, n):
    words = seq.split()
    wordngram = [words[i:i + n] for i in range(len(words) - n + 1)]
    charngram = [seq[i:i + n] for i in range(len(seq) - n + 1)]
    return (charngram, wordgram)

print(seq2ngram("I am an NLPer", 2))
