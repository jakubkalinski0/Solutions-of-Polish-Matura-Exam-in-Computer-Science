plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("wyniki6.txt","a")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
ile2=0
for j in range(0,320):
    ile1=1
    for i in range(0,199):
        if lista[i][j]==lista[i+1][j]:
            ile1+=1
        else:
            if ile1>ile2:
                ile2=ile1
            ile1=1
    if ile1>ile2:
        ile2=ile1
print(ile2)
odp.write("4\n")
odp.write(str(ile2))
odp.write("\n")