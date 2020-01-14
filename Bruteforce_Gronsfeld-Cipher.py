import string

Letter = string.ascii_lowercase
def encrypt():
    text = "BUDIDARMA".lower().replace(" ","")
    key = [0,1,2]*len(text)
    result = "".join([chr((ord(text[i])+key[i]-97)%26+97) for i in range(len(text))])
    print(result)
def decrypt():
    text = "bvfiecrnc".lower().replace(" ","")
    key = [0,1,2]*len(text)
    result = "".join([chr((ord(text[i])-key[i]-97)%26+97) for i in range(len(text))])
    print(result)
def brute_decrypt(n1,n2,n3):
    text = "bvfiecrnc".lower().replace(" ","")
    key = [n1,n2,n3]*len(text)
    result = "".join([chr((ord(text[i])-key[i]-97)%26+97) for i in range(len(text))])
    print(n1,n2,n3,result)
for n1 in range(10):
    for n2 in range(10):
        for n3 in range(10):
            brute_decrypt(n1,n2,n3)
