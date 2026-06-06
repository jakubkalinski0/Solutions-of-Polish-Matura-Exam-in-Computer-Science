plik=open("napisy.txt", "r")
lista=plik.readlines()
odp=open("zadanie4.txt", "a")
equal=0
zeraa=0
jedynkii=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    jedynki=0
    zera=0
    for c in range(len(lista[i])):
        if int(lista[i][c])==1:
            jedynki+=1
        else:
            zera+=1
    if zera==len(lista[i]):
        zeraa+=1
    elif jedynki==len(lista[i]):
        jedynkii+=1
print("0",zeraa)
print("1",jedynkii)
odp.write("c")
odp.write("\n")
odp.write("0 ")
odp.write(str(zeraa))
odp.write("\n")
odp.write("1 ")
odp.write(str(jedynkii))
odp.write("\n")