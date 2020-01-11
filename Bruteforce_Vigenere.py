import string

letter = string.ascii_lowercase

def encrypt():
    text = "enomarozi".lower()
    key = "ancak".lower()
    if len(key) < len(text):
        key = (key*len(text))[:len(text)]
    result_text = [j for i in text for j in range(len(letter)) if i == letter[j]]
    result_key = [j for i in key for j in range(len(letter)) if i == letter[j]]
    process = [letter[(result_key[i]+result_text[j])%26] for i in range(len(result_key)) for j in range(len(result_text)) if i == j]
    encrypt = "".join(process)
    print(encrypt)
def decrypt():
    text = "enomarozi".lower()
    key = "ancak".lower()
    if len(key) < len(text):
        key = (key*len(text))[:len(text)]
    result_text = [j for i in text for j in range(len(letter)) if i == letter[j]]
    result_key = [j for i in key for j in range(len(letter)) if i == letter[j]]
    process = [letter[(result_text[j]-result_key[i])%26] for i in range(len(result_key)) for j in range(len(result_text)) if i == j]
    encrypt = "".join(process)
    print(encrypt)
def brute_decrypt(key):
    text = "enomarozi".lower()
    if len(key) < len(text):
        key = (key*len(text))[:len(text)]
    result_text = [j for i in text for j in range(len(letter)) if i == letter[j]]
    result_key = [j for i in key for j in range(len(letter)) if i == letter[j]]
    process = [letter[(result_text[j]-result_key[i])%26] for i in range(len(result_key)) for j in range(len(result_text)) if i == j]
    encrypt = "".join(process)
    if "enomaqnyh" in encrypt:
        print(key+" --> "+encrypt)

for i in letter:
    for j in letter:
        for k in letter:
            for l in letter:
                for m in letter:
                    for n in letter:
                        for o in letter:
                            for p in letter:
                                for q in letter:
                                    key = i+j+k+l+m+n+o+p+q
                                    brute_decrypt(key)
    

