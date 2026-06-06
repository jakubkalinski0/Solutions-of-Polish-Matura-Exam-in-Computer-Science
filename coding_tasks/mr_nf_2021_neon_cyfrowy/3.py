plik=open("instrukcje.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write("3")
odp.write("\n")
dopisz=[]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    if lista[i][0]=="DOPISZ":
        dopisz.append(lista[i][1])
litery=list("".join(set(dopisz)))
litera=""
ile2=0
for i in range(len(litery)):
    ile1=0
    for j in range(0,len(dopisz)):
        if litery[i]==dopisz[j]:
            ile1+=1
    if ile1>ile2:
        ile2=ile1
        litera=litery[i]
print(litera, ile2)
odp.write(str(litera))
odp.write(" ")
odp.write(str(ile2))
odp.write("\n")