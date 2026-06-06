plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("wyniki6.txt","w")
odp.write("a")
odp.write("\n")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if lista[i][0]==lista[i][len(lista[i])-1]:
        ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")