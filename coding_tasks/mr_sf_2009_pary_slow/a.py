plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("zad_5.txt","w")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    for j in range(2):
        if lista[i][j]==lista[i][j][::-1]:
            ile+=1
print(ile)
odp.write("a")
odp.write("\n")
odp.write(str(ile))
odp.write("\n")