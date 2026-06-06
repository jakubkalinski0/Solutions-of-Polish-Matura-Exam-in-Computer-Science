plik=open("slowa.txt","r")
lista=plik.readlines()
odp=open("wynik4.txt","w")
odp.write("1")
odp.write("\n")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    zera=0
    jedynki=0
    for j in range(len(lista[i])):
        if lista[i][j]=="0":
            zera+=1
        else:
            jedynki+=1
    if zera>jedynki:
        ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")