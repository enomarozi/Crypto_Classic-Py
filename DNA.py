DNA_code = {'A':'CGG','B':'CGT','C':'CTA','D':'CTC','E':'CTG','F':'CTT',
            'G':'GAA','H':'GAC','I':'GAG','J':'GAT','K':'GCA','L':'GCC',
            'M':'GCG','N':'TCT','O':'GGA','P':'GGC','Q':'GGG','R':'GGT',
            'S':'GTA','T':'GTC','U':'GTG','V':'GTT','W':'TAA','X':'TAC',
            'Y':'TAG','Z':'TAT','a':'AAA','b':'AAC','c':'AAG','d':'AAT',
            'e':'ACA','f':'ACC','g':'ACG','h':'ACT','i':'AGA','j':'AGC',
            'k':'AGG','l':'AGT','m':'ATA','n':'ATC','o':'ATG','p':'ATT',
            'q':'CAA','r':'CAC','s':'CAG','t':'CAT','u':'CCA','v':'CCC',
            'w':'CCG','x':'CCT','y':'CGA','z':'CGT','1':'TCA','2':'TCC',
            '3':'TCG','4':'TCT','5':'TGA','6':'TGC','7':'TGG','8':'TGT',
            '9':'TTA','0':'TTC',' ':'TTG'}
list_text = 'CTAACTAAAAGTAGTACAATCACGACATTGAGAATCAGATTGATAACAATCACGAAAATCAATCCAATCACGTTGGTAAAAAGAATCCAGTTGCATACAATCCATAAAATCACGTTGCTCGCTCGGTTGCTATTCAATACATTGCTTAGTAAAACGTTGTTGCTAGTCCTTGGTATATCAATATCAATCTCGATCACGACGTCTAGGATTTCAATCCATTCGCACCAGTCTTCAATCTGATTGGTGAATAAAACTTTGAGACATCCATTGAAAAGCAAA'
result = [list_text[:i][-3:] for i in range(3,len(list_text)+3,3)]
for i in result:
    for j in DNA_code.items():
        if i == j[1]:
            print(j[0],end='')
