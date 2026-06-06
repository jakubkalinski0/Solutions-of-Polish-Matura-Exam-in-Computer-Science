plik=open("dane_6_2.txt","r")
lista=plik.readlines()
odp=open("wyniki_6_2.txt","w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    znak=""
    nowy=""
    for j in range(len(lista[i][0])):
        znak=chr((ord(lista[i][0][j])-65-int(lista[i][1]))%26+65)
        nowy+=znak
    print(nowy)
    odp.write(str(nowy))
    odp.write("\n")
#bledne dane w paru miejscach(brak klucza)