import string
import numpy as np

Letter = string.ascii_lowercase
def encrypt():
    text = "DETEKTIF".lower()
    translate = str(input("Remove Letter = "))
    letter_key = "abcdefghijklmnopqrstuvwxyz".lower()
    result = [i for i in letter_key if translate != i]
    shap = np.reshape(result,(5,5))
    result_shape = ""
    for k in text:
        for i in range(5):
            fix_shape = [str(i+1)+str(j+1) for j in range(5) if shap[i][j] == k] 
            result_shape += "".join(fix_shape)
    print(result_shape)
    genap,ganjil,resultswap = "","",""
    for i in range(len(result_shape)):
        if i%2==0:
            genap += result_shape[i]
        else:
            ganjil += result_shape[i]
    resultswap = genap+ganjil
    result = [resultswap[:i][-2:] for i in range(2,len(resultswap)+2,2)]
    result_all = ""
    for i in result:
        result_all += str(shap[int(i[:-1])-1][int(i[1:])-1])
    print(result_all)
def decrypt():
    text = "aqiguuyq".lower()
    translate = str(input("Remove Letter = "))
    letter_key = "abcdefghijklmnopqrstuvwxyz".lower()
    result = [i for i in letter_key if translate != i]
    shap = np.reshape(result,(5,5))
    result_shape = ""
    for k in text:
        for i in range(5):
            fix_shape = [str(i+1)+str(j+1) for j in range(5) if shap[i][j] == k] 
            result_shape += "".join(fix_shape)
    result = "".join([result_shape[:i][-2:] for i in range(2,len(result_shape)+2,2)])
    result_all = ""
    for i in range(len(result)//2):
        result_all += shap[int(result[i])-1][int(result[i+(len(result)//2)])-1]
    print(result_all)
def brute_bifid(rem):
    text = "aqiguuyq".lower()
    translate = rem
    letter_key = "abcdefghijklmnopqrstuvwxyz".lower()
    result = [i for i in letter_key if translate != i]
    shap = np.reshape(result,(5,5))
    result_shape = ""
    for k in text:
        for i in range(5):
            fix_shape = [str(i+1)+str(j+1) for j in range(5) if shap[i][j] == k] 
            result_shape += "".join(fix_shape)
    result = "".join([result_shape[:i][-2:] for i in range(2,len(result_shape)+2,2)])
    result_all = ""
    for i in range(len(result)//2):
        result_all += shap[int(result[i])-1][int(result[i+(len(result)//2)])-1]
    print("Alphabet = "+letter_key+" key = "+rem+" hasil --> "+result_all)
for i in Letter:
    brute_bifid(i)
