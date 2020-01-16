import string
from random import randint

Letter = string.ascii_lowercase+string.digits
def encrypt():
    text = "enomarozi"
    key = "enox46mksjw137grdt5ufz0y29p8lqvaihbc"
    encrypt = "".join([key[Letter.index(j)] for i in text for j in key if i==j])
    print("Key : "+key+" --> "+encrypt)
def decrypt():
    text = "47g3etg9s"
    key = "enox46mksjw137grdt5ufz0y29p8lqvaihbc"
    decrypt = "".join([Letter[key.index(j)] for i in text for j in key if i==j])
    print("Key : "+key+" --> "+decrypt)
def brute_cryptogram():
    text = "47g3etg9s"
    key = ""
    for i in range(200):
        add = Letter[randint(0,35)]
        if add not in key:
            key += add
    decrypt = "".join([Letter[key.index(j)] for i in text for j in key if i==j])
    print("Key : "+key+" --> "+decrypt)
while 1:
    brute_cryptogram()
