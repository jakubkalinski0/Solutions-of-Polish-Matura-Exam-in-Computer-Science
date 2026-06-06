plik1=open("dane1.txt","r")
lista1=plik1.readlines()
plik2=open("dane2.txt","r")
lista2=plik2.readlines()
odp=open("wynik4_4.txt","w")
for i in range(len(lista1)):
    lista1[i]=lista1[i].strip()
    lista1[i]=lista1[i].split()
    lista2[i]=lista2[i].strip()
    lista2[i]=lista2[i].split()
    ciag3=[]
    while lista1[i] and lista2[i]:
        if int(lista1[i][0])<=int(lista2[i][0]):
            ciag3.append(lista1[i][0])
            lista1[i].remove(lista1[i][0])
        else:
            ciag3.append(lista2[i][0])
            lista2[i].remove(lista2[i][0])
    if lista1[i]:
        for j in range(len(lista1[i])):
            ciag3.append(lista1[i][j])
    if lista2[i]:
        for j in range(len(lista2[i])):
            ciag3.append(lista2[i][j])
    for j in range(len(ciag3)):
        odp.write(ciag3[j])
        odp.write(" ")
    odp.write("\n")