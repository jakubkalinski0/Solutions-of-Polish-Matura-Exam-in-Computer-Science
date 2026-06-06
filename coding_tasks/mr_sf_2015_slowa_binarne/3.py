plik=open("slowa.txt","r")
lista=plik.readlines()
odp=open("wynik4.txt","a")
odp.write("3")
odp.write("\n")
wyniki=[]
ile2=0
ile3=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    ile1=0
    ile2=0
    for j in range(len(lista[i])):
        if lista[i][j]=="0":
            ile1+=1
        else:
            if ile1>ile2:
                ile2=ile1
            ile1=0
    if ile1>ile2:
        ile2=ile1
    if ile2 == ile3:
        wyniki.append(lista[i])
    if ile2>ile3:
        ile3=ile2
        wyniki=[]
        wyniki.append(lista[i])
print(ile3)
odp.write(str(ile3))
odp.write("\n")
for i in range(len(wyniki)):
    print(wyniki[i])
    odp.write(wyniki[i])
    odp.write("\n")