plik=open("slowa.txt", "r")
lista1=plik.readlines()
plik2=open("nowe.txt", "r")
lista2=plik2.readlines()
odp=open("wynik5.txt", "a")
odp.write("2")
odp.write("\n")
for i in range(len(lista1)):
    lista1[i]=lista1[i].strip()
for i in range(len(lista2)):
    lista2[i]=lista2[i].strip()
for i in range(len(lista2)):
    lustro=""
    suma1=0
    suma2=0
    for z in range(len(lista2[i])):
        lustro=lista2[i][z]+lustro
    for k in range(len(lista1)):
        if lista2[i]==lista1[k]:
            suma1+=1
        if lustro==lista1[k]:
            suma2+=1
    print(str(lista2[i]),suma1,suma2)
    odp.write(str(lista2[i])+" "+str(suma1)+" "+str(suma2))
    odp.write("\n")