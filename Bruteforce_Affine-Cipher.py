import string

Letter = string.ascii_lowercase
def encrypt():
    text = "GILDA".lower().replace(" ","")
    shift = int(input("Input Shift = "))
    coprime = int(input("Input Coprome = "))
    hasil = "".join([Letter[(coprime*Letter.index(i)+shift)%26] for i in text])
    print(hasil)
def decrypt():
    text = "fqxjdsxwh".lower().replace(" ","")
    shift = int(input("Input Shift = "))
    coprime = int(input("Input Coprome = "))
    hasil = "".join([Letter[coprime*(Letter.index(i)-shift)%26] for i in text])
    print(hasil)
def brute_decrypt(rot,prime):
    text = "fqxjdsxwh".lower().replace(" ","")
    shift = rot
    coprime = prime
    hasil = "".join([Letter[coprime*(Letter.index(i)-shift)%26] for i in text])
    if "enomarozi" in hasil:
        print("Shift = "+str(rot)+" Coprime= "+str(prime)+" hasil --> "+hasil)
for rot in range(26):
    for coprime in range(9999):
        brute_decrypt(rot,coprime)
