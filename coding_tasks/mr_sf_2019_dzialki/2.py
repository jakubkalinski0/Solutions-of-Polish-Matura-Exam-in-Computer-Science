plik=open("dzialki.txt","r")
lista=plik.readlines()
odp=open("wynik4.txt","a")
odp.write("2")
odp.write("\n")
linia=[]
nrdzialki1=0
nrdzialki2=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
for i in range(49):
    lista.remove("")
for i in range(0,len(lista),30):
    ile1=0
    napis=""
    for j in range(i,i+30):
        napis+=lista[j]
    linia.append(napis)
for i in range(len(linia)):
    dzialka1=linia[i][::-1]
    for j in range(len(linia)):
        if dzialka1==linia[j]:
            nrdzialki1=i+1
            nrdzialki2=j+1
            break
    if nrdzialki1!=0:
        break
print(nrdzialki1, nrdzialki2)
odp.write(str(nrdzialki1))
odp.write("\n")
odp.write(str(nrdzialki2))
odp.write("\n")