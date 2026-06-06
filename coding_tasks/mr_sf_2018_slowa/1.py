plik=open("slowa.txt","r")
lista=plik.readlines()
odp=open("wyniki6.txt","w")
odp.write("1")
odp.write("\n")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    for j in range(len(lista[i])):
        if lista[i][j][len(lista[i][j])-1]=="A":
            ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")