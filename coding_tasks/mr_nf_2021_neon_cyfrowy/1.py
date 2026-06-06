plik=open("instrukcje.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","w")
odp.write("1")
odp.write("\n")
napis=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    if lista[i][0]=="DOPISZ":
        napis+=1
    if lista[i][0]=="USUN":
        napis-=1
print(napis)
odp.write(str(napis))
odp.write("\n")