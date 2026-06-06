plik=open("slowa.txt", "r")
lista=plik.readlines()
print(lista)
odp=open("wynik5.txt", "w")
odp.write("1")
odp.write("\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
for i in range(1,13):
    ile=0
    for k in range(len(lista)):
        if i==len(lista[k]):
            ile+=1
    print(str(i),":",ile)
    odp.write(str(i)+" "+str(ile))
    odp.write("\n")
