plik=open("dane_6_3.txt","r")
lista=plik.readlines()
odp=open("wyniki_6_3.txt","w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    if ord(lista[i][0][0])>ord(lista[i][1][0]):
        klucz=26-(ord(lista[i][0][0])-ord(lista[i][1][0]))
    elif ord(lista[i][0][0])<ord(lista[i][1][0]):
        klucz=ord(lista[i][1][0])-ord(lista[i][0][0])
    elif ord(lista[i][0][0])==ord(lista[i][1][0]):
        klucz=0
    znak=""
    nowy=""
    for j in range(len(lista[i][0])):
        znak=chr((ord(lista[i][0][j])-65+klucz)%26+65)
        nowy+=znak
    if nowy!=lista[i][1]:
        print(lista[i][0])
        odp.write(str(lista[i][0]))
        odp.write("\n")