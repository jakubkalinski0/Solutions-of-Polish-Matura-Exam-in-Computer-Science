plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("wyniki6.txt","a")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
ile=0
for i in range(len(lista)):
    for j in range(len(lista)):
        if int(lista[i][j])!=int(lista[i][-1-j]):
            ile+=1
            break
print(ile)
odp.write("2\n")
odp.write(str(ile))
odp.write("\n")