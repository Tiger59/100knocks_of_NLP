sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sentence = sentence.replace(',','')
sentence = sentence.replace('.','')
words = sentence.split()
word_count = [len(i) for i in words]

print(word_count)