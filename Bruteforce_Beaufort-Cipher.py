import string

Letter = string.ascii_lowercase
def encrypt():
    text = "enomarozi"
    reverse = Letter[::-1]
    encrypt = ""
    list_key = [Letter.index(i)+1 for i in "bac"*len(text)] 
    for i in range(len(text)):
        encrypt += Letter[(reverse.index(text[i])+list_key[i])%26]
    print(encrypt)
def decrypt():
    text = "xnopalnbu"
    reverse = Letter[::-1]
    decrypt = ""
    list_key = [Letter.index(i)+1 for i in "bac"*len(text)] 
    for i in range(len(text)):
        decrypt += reverse[(Letter.index(text[i])-list_key[i])%26]
    print(decrypt)
def brute_beaufort(key):
    text = "xnopalnbu"
    reverse = Letter[::-1]
    decrypt = ""
    list_key = [Letter.index(i)+1 for i in key*len(text)] 
    for i in range(len(text)):
        decrypt += reverse[(Letter.index(text[i])-list_key[i])%26]
    print("Key : "+key+" Decrypt --> "+decrypt)
for k in Letter:
    for e in Letter:
        for y in Letter:
            brute_beaufort(k+e+y)
