plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write("2")
odp.write("\n")
for i in range(len(lista)):
    suma=0
    lista[i]=lista[i].strip()
    for j in range(len(lista[i])):
        suma+=int(lista[i][j])
    if suma==11:
        print(lista[i])
        odp.write(str(lista[i]))
        odp.write("\n")