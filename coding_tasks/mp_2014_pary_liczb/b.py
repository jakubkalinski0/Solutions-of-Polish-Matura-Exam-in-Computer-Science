plik=open("PARY_LICZB.txt", "r")
lista=plik.readlines()
odp=open("ZADANIE5.txt", "a")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
for i in range(len(lista)):
    while lista[i][1]!=0:
        pom=lista[i][1]
        lista[i][1]=int(lista[i][0])%int(lista[i][1])
        lista[i][0]=pom
    if lista[i][0]==1:
        ile+=1
print(ile)
odp.write(str(ile))