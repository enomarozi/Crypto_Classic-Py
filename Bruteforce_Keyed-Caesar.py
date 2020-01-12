import string
from random import randint

#hijklmnopqrstuvwxyzabcdefg

letter = string.ascii_lowercase
def encrypt():
    text = "enomarozi".lower()
    shift = int(input("Input shift : "))
    letter_key = str(input("Input letter key : "))
    process_shift = "".join([chr((ord(i)+shift-97)%26+97) for i in text])
    result_subtitution = ""
    for i in range(len(process_shift)):
        for j in range(len(letter)):
            try:
                if process_shift[i] == letter[j]:
                    result_subtitution += letter_key[j]
            except:
                pass
    print(letter_key +" --> "+result_subtitution)
def decrypt():
    text = "mvwuizwhq".lower()
    shift = int(input("Input shift : "))
    letter_key = str(input("Input letter key : "))
    process_shift = "".join([chr((ord(i)+(-shift)-97)%26+97) for i in text])
    result_subtitution = ""
    for i in range(len(process_shift)):
        for j in range(len(letter)):
            try:
                if process_shift[i] == letter_key[j]:
                    result_subtitution += letter[j]
            except:
                pass
    print(letter_key +" --> "+result_subtitution)
def decrypt_brute(rot):
    text = "mvwuizwhq".lower()
    shift = rot
    letter_key = ""
    for i in range(200):
        add = string.ascii_lowercase[randint(0,25)]
        if add not in letter_key:
            letter_key += add
    #letter_key = "hijklmnopqrstuvwxyzabcdefg"
    process_shift = "".join([chr((ord(i)+(-shift)-97)%26+97) for i in text])
    result_subtitution = ""
    for i in range(len(process_shift)):
        for j in range(len(letter)):
            try:
                if process_shift[i] == letter_key[j]:
                    result_subtitution += letter[j]
            except:
                pass
    if "hijklmnop" in letter_key:
        print(letter_key +" --> "+result_subtitution)
while 1:
    for i in range(1,26):
        decrypt_brute(i)

    

