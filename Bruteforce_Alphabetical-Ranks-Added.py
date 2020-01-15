import string
from random import randint

letter = string.ascii_lowercase
def encrypt():
    text = "enomarozi".lower().replace(" ","")
    adds0 = 0;adds1 = 0;Letter=letter
    encrypt0 = [];encrypt1 = []
    for i in text:
        adds0 += Letter.index(i)
        adds1 += Letter.index(i)+1
        encrypt0.append(str(adds0))
        encrypt1.append(str(adds1))
    print("Init Letter 0 : "+" ".join(encrypt0))
    print("Init Letter 1 : "+" ".join(encrypt1))
def decrypt():
    text = "0 4 17 31 43 43 60 74 99 107".split(" ")
    decrypt0 = ""
    Letter=letter
    for i in range(len(text)-1):
        try:
            decrypt0 += Letter[int(text[i+1])-int(text[i])]
        except:
            pass
    print(decrypt0)
def brute_aphabetical():
    text = "0 4 17 31 43 43 60 74 99 107".split(" ")
    decrypt0 = ""
    Letter= ""
    for i in range(200):
        add = string.ascii_lowercase[randint(0,25)]
        if add not in Letter:
            Letter += add
    for i in range(len(text)-1):
        try:
            decrypt0 += Letter[int(text[i+1])-int(text[i])]
        except:
            pass
    print("Alphabet : "+Letter+" Decrypt --> "+decrypt0)
while 1:
    brute_aphabetical()
