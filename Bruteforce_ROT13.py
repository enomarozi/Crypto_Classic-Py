import sys

def ROT13(n):
    text = sys.argv[1].lower()
    hasil = [chr((ord(i)+n-97)%26+97) for i in text]
    hasil1 = ",".join(hasil)
    return(hasil1.replace(",",""))
    
for i in range(26):
    print(str(i)+" "+(ROT13(i)))
