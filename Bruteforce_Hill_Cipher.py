import numpy as np
import string

def hill_cipher(key):
    baris = 2
    kolom = 2
    key = np.reshape(key,(baris,kolom))
    text = "strikenoww"
    text_hill = ([""])
    for i in text:
        for j in range(25):
            if i==string.ascii_lowercase[j-1]:
                text_hill.append(j)
    encrypt = ""
    separate = []
    for j in range(len(text_hill)//baris):
        for i in range(2):
            separate.append(text_hill[1])
            del text_hill[i]
        b = np.reshape(separate,(2,1))
        sub_result = np.dot(key,b)
        result = sub_result%26
        
        for i in result:
            encrypt += string.ascii_lowercase[int(i-1)]
        separate = []
    print(key,encrypt)

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                key = [i,j,k,l]
                hill_cipher(key)
