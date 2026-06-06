plik1=open("sz.txt","r")
lista1=plik1.readlines()
plik2=open("klucze2.txt","r")
lista2=plik2.readlines()
odp=open("wynik4b.txt","w")
alfabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def szyfr(slowo1,slowo2):
    znak=""
    napis=""
    if len(slowo1)<=len(slowo2):
        for i in range(len(slowo1)):
            znak=chr((ord(slowo1[i])-65-(alfabet.index(slowo2[i])+1))%26+65)
            napis+=znak
    else:
        for i in range(len(slowo1)):
            znak=chr((ord(slowo1[i])-65-(alfabet.index(slowo2[i%len(slowo2)])+1))%26+65)
            napis+=znak
    return napis
for i in range(len(lista1)):
    lista1[i]=lista1[i].strip()
    lista2[i]=lista2[i].strip()
    zaszyfrowane=szyfr(lista1[i],lista2[i])
    print(zaszyfrowane)
    odp.write(zaszyfrowane)
    odp.write("\n")