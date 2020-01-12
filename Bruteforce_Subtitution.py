import string
from random import randint

letter = string.ascii_lowercase

def encrypt():
    text = "vydnjvndineznuuffyfukngenvhngvysjbfydxyejgnr".replace(" ","").lower()
    letter_key = ""
    for i in range(200):
        add = string.ascii_lowercase[randint(0,25)]
        if add not in letter_key:
            letter_key += add
    result_subtitution = ""
    for i in range(len(text)):
        for j in range(len(letter)):
            try:
                if text[i] == letter[j]:
                    result_subtitution += letter_key[j]
            except:
                pass
    print(letter_key +" --> "+result_subtitution)
while 1:
    encrypt()
