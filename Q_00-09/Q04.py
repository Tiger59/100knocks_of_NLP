sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sigh Peace Security Clause. Arthur King Can.'

words = sentence.split()
number_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
word_dict = {}

for i, word in enumerate(words, 1):
    if i in number_list:
        word_dict[word[:1]]=i
    else:
        word_dict[word[:2]]=i

print(word_dict)