plik=open("liczby.txt", "r")
lista=plik.readlines()
odp=open("wynik5.txt", "a")
wyniki=[]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    suma=0
    for z in lista[i]:
        suma+=int(z)
    if suma>30:
        wyniki.append(lista[i])
cyfry="".join(lista)
suma2=0
for i in cyfry:
    suma2+=int(i)
odp.write("3")
odp.write("\n")
for i in range(len(wyniki)):
    print(wyniki[i])
    odp.write(str(wyniki[i]))
    odp.write("\n")
odp.write(str(suma2))
print(suma2)