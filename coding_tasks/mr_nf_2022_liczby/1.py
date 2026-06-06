plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","w")
odp.write("1")
odp.write("\n")
ile=0
czy=1
pierwsza=""
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if lista[i][0]==lista[i][len(lista[i])-1]:
        ile+=1
    if czy==1 and lista[i][0]==lista[i][len(lista[i])-1]:
        pierwsza=lista[i]
        czy=0
print(ile, pierwsza)
odp.write(str(ile))
odp.write(" ")
odp.write(str(pierwsza))
odp.write("\n")