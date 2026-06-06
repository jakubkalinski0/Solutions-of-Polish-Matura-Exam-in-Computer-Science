plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write("2\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    suma=0
    for j in range(len(lista[i])):
        cyfra=int(lista[i][j])
        silnia=1
        for z in range(2,cyfra+1):
            silnia=silnia*z
        suma+=silnia
    if int(lista[i])==suma:
        print(lista[i])
        odp.write(lista[i])
        odp.write("\n")