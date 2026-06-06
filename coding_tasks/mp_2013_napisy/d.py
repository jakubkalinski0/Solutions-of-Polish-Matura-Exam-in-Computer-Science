plik=open("napisy.txt", "r")
lista=plik.readlines()
odp=open("zadanie4.txt", "a")
odp.write("d")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
for k in range(2,17):
    ile=0
    for l in range(len(lista)):
        if len(lista[l])==k:
            ile+=1
    print(k,":",ile)
    odp.write("\n")
    odp.write(str(k))
    odp.write(" ")
    odp.write(str(ile))