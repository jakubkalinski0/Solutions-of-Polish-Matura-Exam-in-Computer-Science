plik=open("dzialki.txt","r")
lista=plik.readlines()
odp=open("wynik4.txt","w")
odp.write("1")
odp.write("\n")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
for i in range(49):
    lista.remove("")
for i in range(0,len(lista),30):
    ile1=0
    for j in range(i,i+30):
        for k in range(30):
            if lista[j][k]=="*":
                ile1+=1
    if (ile1/900)*100>=70:
        ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")