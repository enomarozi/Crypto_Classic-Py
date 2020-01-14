import numpy as np

def brute_encrypt_decrypt(row,col,text):
    row = len(text)
    text_fix = ""
    if row*col < len(text):
        text_fix = text[:row*col]
    elif row*col >= len(text):
        text_fix = text.ljust(row*col," ")
    result_text = [i for i in text_fix]
    matrix = np.reshape(result_text,(row,col)).T
    result_all = ""
    for i in range(len(matrix)):
        result_all += "".join([matrix[i][j] for j in range(len(matrix[0]))])
    print("Band = "+str(col)+" --> "+result_all.replace(" ",""))
text = "enomarozi".lower().replace(" ","")
for i in range(1,len(text)+1):
    brute_encrypt_decrypt(len(text),i,text)
