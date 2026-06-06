plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("wyniki.txt","a")
odp.write("b")
odp.write("\n")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if lista[i][-1]=="A" or lista[i][-1]=="C" or lista[i][-1]=="E":
        ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")