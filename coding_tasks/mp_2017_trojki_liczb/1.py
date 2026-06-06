plik=open("liczby.txt", "r")
lista=plik.readlines()
odp=open("wyniki4.txt", "w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
ile=0
for i in range(len(lista)):
    if int(lista[i][0])<int(lista[i][1])<int(lista[i][2]):
        ile+=1
print(ile)
odp.write("1")
odp.write("\n")
odp.write(str(ile))
odp.write("\n")