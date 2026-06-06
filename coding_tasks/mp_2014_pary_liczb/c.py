plik=open("PARY_LICZB.txt", "r")
lista=plik.readlines()
odp=open("ZADANIE5.txt", "a")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
for i in range(len(lista)):
    suma1=0
    suma2=0
    for q in range(len(lista[i][0])):
        suma1+=int(lista[i][0][q])
    for z in range(len(lista[i][1])):
        suma2+=int(lista[i][1][z])
    if suma1==suma2:
        ile+=1
print(ile)
odp.write(str(ile))