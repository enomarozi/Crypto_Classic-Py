def encrypt():
    text = "enomarozi".lower().replace(" ","")
    alberti_disk1 = "abcdefgilmnopqrstvxz1234".lower()
    alberti_disk2 = "c&bmdgpfznxyvtoskerlhaiq"
    result = ""
    for i in range(len(text)):
        for j in range(len(alberti_disk1)):
            if text[i]==alberti_disk1[j]:
                result += alberti_disk2[j]
    result = result*2
    leng = 1;inc = 2
    test = 0;list_test = [0]
    for i in range(len(text)):
        test += inc
        list_test.append(test)
    result_all = [result[:i][-leng:] for i in range(leng,len(result)+leng,leng)]
    encrypt = ""
    for i in range(len(result_all)):
        try:
            encrypt += "".join([alberti_disk2[(alberti_disk2.index(j)+list_test[i])%24] for j in result_all[i]])
        except:
            pass
    print("Length : "+str(leng)+" Increment : "+str(inc)+" Encrypt : "+encrypt[:len(text)])
def decrypt():
    text = "dvsszcqnq"
    alberti_disk1 = "abcdefgilmnopqrstvxz1234".lower()
    alberti_disk2 = "c&bmdgpfznxyvtoskerlhaiq"
    result = text*2
    leng = 1;inc = 2
    test = 0;list_test = [0]
    for i in range(len(text)):
        test += inc
        list_test.append(test)
    result_all = [result[:i][-leng:] for i in range(leng,len(result)+leng,leng)]
    decrypt = ""
    for i in range(len(result_all)):
        try:
            decrypt += "".join([alberti_disk1[(alberti_disk2.index(j)-list_test[i])%24] for j in result_all[i]])
        except:
            pass
    print("Length : "+str(leng)+" Increment : "+str(inc)+" Decrypt : "+decrypt[:len(text)])
def brute_alberti(length,increment):
    text = "dvsszcqnq"
    alberti_disk1 = "abcdefgilmnopqrstvxz1234".lower()
    alberti_disk2 = "c&bmdgpfznxyvtoskerlhaiq"
    result = text*2
    leng = length;inc = increment
    test = 0;list_test = [0]
    for i in range(len(text)):
        test += inc
        list_test.append(test)
    result_all = [result[:i][-leng:] for i in range(leng,len(result)+leng,leng)]
    decrypt = ""
    for i in range(len(result_all)):
        try:
            decrypt += "".join([alberti_disk1[(alberti_disk2.index(j)-list_test[i])%24] for j in result_all[i]])
        except:
            pass
    print("Length : "+str(leng)+" Increment : "+str(inc)+" Decrypt : "+decrypt[:len(text)])
for i in range(1,10):
    for j in range(1,10):
        brute_alberti(i,j)

