import sys

def ROT(n):
    text = sys.argv[1]
    if sys.argv[3] == "+":
        hasil = [chr(ord(i)+n) for i in text]
        hasil1 = "".join(hasil)
        return hasil1
    elif sys.argv[3] == "-":
        hasil = [chr(ord(i)-n) for i in text]
        hasil1 = "".join(hasil)
        return hasil1
for rot in range(int(sys.argv[2])):
    print(ROT(rot))

