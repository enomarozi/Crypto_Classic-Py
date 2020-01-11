import string
import numpy as np

letter = string.ascii_lowercase
def encrypt():
    text = "kenaikan harga bbm membuat rakyat kecil menderitax".replace(" ","").lower()
    subtitution = str(input("Subtitusi A = ")).lower() #g
    column = int(input("Columns = "))
    row = int(input("Rows = "))
    sub_process1 = [letter[i] for i in range(letter.index(subtitution),26)]
    sub_process2 = [i for i in letter if i not in sub_process1]
    letter_key = (",".join(sub_process1)+",".join(sub_process2)).replace(",","")
    result_subtitution = ""
    for i in range(len(text)):
        for j in range(len(letter)):
            if text[i] == letter[j]:
                result_subtitution += letter_key[j]
    if len(result_subtitution) <= column*row:
        dummy = result_subtitution.ljust(column*row,"x")
    elif len(result_subtitution) > column*row:
        dummy = result_subtitution[:column*row]
    encrypt = [i for i in dummy]
    a = np.reshape(encrypt,(row,column))
    result_all = "".join([a[j][i] for i in range(len(a.T)) for j in range(len(a.T[0]))])
    print(result_all) 
def decrypt():
    text = "qongsagzotokqghkgqqrjztgxhszekskggtmshxgikxdxx".replace(" ","").lower()
    text_list = [i for i in text]
    subtitution = str(input("Subtitusi A = ")).lower() #g
    column = 4
    row = 11
    if len(text_list) > column*row:
        list_fix = text_list[:column*row]
    elif len(text_list) <= column*row:
        list_fix = text_list.ljust(column*row,"x")
    a = np.reshape(list_fix,(column,row)).T
    result = ""
    for i in a:
        result += "".join(i)
    result_all = "".join([letter[j-letter.index(subtitution)] for i in range(len(result))  for j in range(len(letter)) if result[i] == letter[j]])
    print(result_all)
def decrypt_brute(co,ro,sub,text):
    text_list = [i for i in text]
    subtitution = sub
    column = co
    row = ro
    if len(text_list) > column*row:
        list_fix = text_list[:column*row]
    elif len(text_list) <= column*row:
        list_fix = text_list.ljust(column*row,"x")
    a = np.reshape(list_fix,(column,row)).T
    result = ""
    for i in a:
        result += "".join(i)
    result_all = "".join([letter[j-letter.index(subtitution)] for i in range(len(result))  for j in range(len(letter)) if result[i] == letter[j]])
    print("column = "+str(co)+" row "+str(ro)+" Subtitution "+sub)
text = "qongsagzotokqghkgqqrjztgxhszekskggtmshxgikxdx".replace(" ","").lower()   
for i in range(2,100):
    for j in range(2,len(text)//i):
        for k in letter:
            decrypt_brute(i,j,k,text)

