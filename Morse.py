import morselib

def decrypt():
    text = ". -. --- -- .- .-. --- --.. ..".split(" ")
    result_all = ""
    for i in text:
        for j in morselib.morse.keys():
            if i == morselib.morse[j]:
                result_all += j
    print(result_all)
def encrypt():
    text = "ENOMAROZI"
    result_all = " ".join([morselib.morse[i] for i in text if i in morselib.morse.keys()]) 
    print(result_all)

    
