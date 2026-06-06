plik=open("dane.txt", "r")
lista=plik.readlines()
odp=open("wyniki6.txt", "a")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if int(lista[i][2:4])==11 or int(lista[i][2:4])==31:
        ile+=1
print(ile)
odp.write("2")
odp.write("\n")
odp.write(str(ile))
odp.write("\n")