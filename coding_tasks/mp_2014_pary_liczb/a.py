plik=open("PARY_LICZB.txt", "r")
lista=plik.readlines()
odp=open("ZADANIE5.txt", "w")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
for k in range(len(lista)):
    if int(lista[k][0])%int(lista[k][1])==0:
        ile+=1
    elif int(lista[k][1])%int(lista[k][0])==0:
        ile+=1
print(ile)
odp.write(str(ile))