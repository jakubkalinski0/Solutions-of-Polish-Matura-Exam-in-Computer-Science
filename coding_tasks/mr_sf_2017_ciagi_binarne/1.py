plik = open("binarne.txt", "r")
lista = plik.readlines()
odp = open("zadanie4.txt", "w")
odp.write("1")
odp.write("\n")
ile=0
maxdl=0
maxnapis=""
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if lista[i][:len(lista[i])//2]==lista[i][len(lista[i])//2::]:
        ile+=1
        if len(lista[i])>maxdl:
            maxdl=len(lista[i])
            maxnapis=lista[i]
print(ile, maxdl, maxnapis)
odp.write(str(ile))
odp.write("\n")
odp.write(str(maxdl))
odp.write("\n")
odp.write(str(maxnapis))
odp.write("\n")