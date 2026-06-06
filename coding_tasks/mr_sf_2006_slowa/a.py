plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("wyniki.txt","w")
odp.write("a")
odp.write("\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
rozne=list(set(lista))
ile1=0
ile2=0
slowo=""
for i in range(len(rozne)):
    ile0=0
    for j in range(len(lista)):
        if rozne[i]==lista[j]:
            ile0+=1
    if ile0>1:
        ile1+=1
    if ile0>ile2:
        ile2=ile0
        slowo=rozne[i]
print(ile1)
print(slowo)
print(ile2)
odp.write(str(ile1))
odp.write("\n")
odp.write(str(slowo))
odp.write("\n")
odp.write(str(ile2))
odp.write("\n")