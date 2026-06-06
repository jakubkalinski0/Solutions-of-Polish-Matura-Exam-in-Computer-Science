plik=open("NAPIS.TXT","r")
lista=plik.readlines()
odp=open("ZADANIE5.txt","a")
odp.write("c")
odp.write("\n")
for i in range(len(lista)):
     lista[i]=lista[i].strip()
rozne=list(set(lista))
for i in range(len(rozne)):
    slowo=rozne[i]
    ile=0
    for j in range(len(lista)):
        if slowo==lista[j]:
            ile+=1
    if ile>1:
        print(slowo)
        odp.write(slowo)
        odp.write("\n")