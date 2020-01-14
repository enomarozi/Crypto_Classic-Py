import string
import numpy as np
from random import randint

def encrypt():
    text1 = "INDONESIA RAYA MERDEKA MERDEKA TANAHKU NEGERIKU YANG KUCINTA".lower().replace(" ","")
    print(text1)
    if len(text1)%25!=0:
        text = text1.ljust(len(text1)*2," ")
    list = [1,7,8,4,5]
    rer = 0
    for i in list:
        rer += i  
    list0 = [0,1,7,8,4,5]
    default = "abcdefghijklmnopqrstuvwxyz"
    default_key = np.reshape([i for i in default if "j" != i],(5,5)).T
    result = [text[:i][-25:] for i in range(rer,len(text),rer)]
    letter_key = "tuihbelasrdpnmcfgkoqvwxyz"
    key = np.reshape([i for i in letter_key if "j" != i],(5,5))
    rer = 0;rel = 0;reverse=""
    for j in result:
        for i in range(len(list)):
            rer += list[i]
            rel += list0[i]
            reverse += (j[rel:rer][::-1])
        rer = 0;rel = 0
    result_all = ""
    for k in reverse:
        for i in range(5):
            result_all += "".join([key[i][j] for j in range(5) if k == default_key[i][j]])
    print(result_all)
def decrypt():
    text1 = "ggmvnkfnsvatqtsttwvfvfsvawwptntotwgsvlvnyntqygdywlnto".lower().replace(" ","")
    default = "abcdefghijklmnopqrstuvwxyz"
    default_key = np.reshape([i for i in default if "j" != i],(5,5)).T
    letter_key = "tuihbelasrdpnmcfgkoqvwxyz"
    key = np.reshape([i for i in letter_key if "j" != i],(5,5))
    result_all = ""
    for k in text1:
        for i in range(5):
            result_all += "".join([default_key[i][j] for j in range(5) if k == key[i][j]])
    if len(result_all)%25!=0:
        text = result_all.ljust(len(result_all)*2," ")
    list = [1,7,8,4,5]
    rer = 0
    for i in list:
        rer += i  
    list0 = [0,1,7,8,4,5]
    result = [result_all[:i][-25:] for i in range(rer,len(text),rer)]
    rer = 0;rel = 0;reverse=""
    for j in result:
        for i in range(len(list)):
            rer += list[i]
            rel += list0[i]
            reverse += (j[rel:rer][::-1])
        rer = 0;rel = 0
    print(reverse[:len(text1)])
def brute_bazaries(n1,n2,n3,n4,n5,rem):
    try:
        text1 = "ggmvnkfnsvatqtsttwvfvfsvawwptntotwgsvlvnyntqygdywlnto".lower().replace(" ","")
        default = "abcdefghijklmnopqrstuvwxyz"
        default_key = np.reshape([i for i in default if rem != i],(5,5)).T
        letter_key = "tuihbelasrdpnmcfgkoqvwxyzj"
        key = np.reshape([i for i in letter_key if rem != i],(5,5))
        result_all = ""
        for k in text1:
            for i in range(5):
                result_all += "".join([default_key[i][j] for j in range(5) if k == key[i][j]])
        if len(result_all)%25!=0:
            text = result_all.ljust(len(result_all)*2," ")
        list = [n1,n2,n3,n4,n5]
        rer = 0
        for i in list:
            rer += i  
        list0 = [0,n1,n2,n3,n4,n5]
        result = [result_all[:i][-25:] for i in range(rer,len(text),rer)]
        rer = 0;rel = 0;reverse=""
        for j in result:
            for i in range(len(list)):
                rer += list[i]
                rel += list0[i]
                reverse += (j[rel:rer][::-1])
            rer = 0;rel = 0
        print(n1,n2,n3,n4,n5,rem,reverse[:len(text1)])
        if "indonesiarayamerdekamerdekatanahkunegerikuyangkuci" in reverse:
            print(n1,n2,n3,n4,n5,rem,reverse[:len(text1)])
    except:
        pass
for n1 in range(10):
    for n2 in range(10):
        for n3 in range(10):
            for n4 in range(10):
                for n5 in range(10):
                    for rem in string.ascii_lowercase:
                        brute_bazaries(n1,n2,n3,n4,n5,rem)
