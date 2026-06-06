plik=open("dane_6_1.txt","r")
lista=plik.readlines()
odp=open("wyniki_6_1.txt","w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    znak=""
    nowy=""
    for j in range(len(lista[i])):
        znak=chr((ord(lista[i][j])-65+107)%26+65)
        nowy+=znak
    print(nowy)
    odp.write(str(nowy))
    odp.write("\n")