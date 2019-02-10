def cipher(sent):
    result = ''
    for c in sent:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c
    return result


sent = input("Input clear text:")

result = cipher(sent)
print('cipher:' + result)

result2 = cipher(result)
print('decryption:' + result2)
