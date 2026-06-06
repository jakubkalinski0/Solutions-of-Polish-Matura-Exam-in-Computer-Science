plik1=open("wyniki4.txt","r")
lista1=plik1.readlines()
plik2=open("odp1dobre.txt", "r")
lista2=plik2.readlines()
for i in range(len(lista1)):
    lista1[i]=lista1[i].strip()
    lista1[i]=lista1[i].split()
for i in range(len(lista2)):
    lista2[i]=lista2[i].strip()
    lista2[i]=lista2[i].split()
for i in range(len(lista2)):
    if lista1[i+1][0]==lista2[i][0] and lista1[i+1][1]==lista2[i][1] and lista1[i+1][2]==lista2[i][2]:
        print(1)