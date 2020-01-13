import string

Letter = string.ascii_lowercase
def encrypt():
    text = "enomarozi"
    hasil = "".join([Letter[Letter[::-1].index(i)] for i in text])
    print(hasil)
def decrypt():
    text = "vmlnzilar"
    hasil = "".join([Letter[::-1][Letter.index(i)] for i in text])
    print(hasil)
def brute_decrypt(n):
    text = "vmlnzilar"
    subtitution = n
    sub_process1 = [Letter[i] for i in range(Letter.index(subtitution),26)]
    sub_process2 = [i for i in Letter if i not in sub_process1]
    letter_key = (",".join(sub_process1)+",".join(sub_process2)).replace(",","")
    hasil = "".join([letter_key[::-1][Letter.index(i)] for i in text])
    print(letter_key[::-1],n,hasil)
for i in Letter:
    brute_decrypt(i)
