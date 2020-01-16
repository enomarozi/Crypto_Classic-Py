import string

Letter = string.ascii_lowercase
def encrypt():
    text = "enomarozi"
    encrypt = "".join([str(Letter.index(i)+1)+"-" for i in text])
    print(encrypt[:-1])
def decrypt():
    text = "5-14-15-13-1-18-15-26-9".split("-")
    decrypt = "".join([Letter[int(i)-1] for i in text])
    print(decrypt)
