plik=open("pary.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write("2")
odp.write("\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    ile1=1
    ile2=0
    litera1=lista[i][1][0]
    litera2=""
    ciag1=litera1
    ciag2=""
    for j in range(1,len(lista[i][1])):
        litera2=lista[i][1][j]
        if litera1==litera2:
            ile1+=1
            ciag1+=litera2
        if litera1!=litera2:
            if ile1>ile2:
                ile2=ile1
                ciag2=ciag1
            ile1=1
            litera1=lista[i][1][j]
            ciag1=lista[i][1][j]
    print(ciag2,ile2)
    odp.write(ciag2)
    odp.write(" ")
    odp.write(str(ile2))
    odp.write("\n")
