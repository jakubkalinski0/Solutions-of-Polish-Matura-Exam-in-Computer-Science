plik=open("dzialki.txt","r")
lista=plik.readlines()
odp=open("wynik4.txt","a")
odp.write("3")
odp.write("\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
for i in range(49):
    lista.remove("")
maxbok=0
nrdzialek=[]
for i in range(0,len(lista),30):
    bok=0
    czyprzeszkoda=0
    while czyprzeszkoda==0:
        bok+=1
        for j in range(i,i+bok):
            for k in range(bok):
                if lista[j][k]=="X":
                    czyprzeszkoda=1
                    break
    if (bok-1)>maxbok:
        maxbok=bok-1
        nrdzialek=[]
        nrdzialek.append(i//30+1)
    elif (bok-1)==maxbok:
        nrdzialek.append(i//30+1)
print(maxbok)
odp.write(str(maxbok))
odp.write("\n")
for i in range(len(nrdzialek)):
    print(nrdzialek[i])
    odp.write(str(nrdzialek[i]))
    odp.write("\n")