plik=open("identyfikator.txt","r")
lista=plik.readlines()
odp=open("wyniki4_1.txt","w")
id=[]
maxsuma=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    suma=0
    for j in range(3,len(lista[i])):
        suma+=int(lista[i][j])
    if suma == maxsuma:
        id.append(lista[i])
    if suma>maxsuma:
        maxsuma=suma
        id.clear()
        id.append(lista[i])
for i in range(len(id)):
    print(id[i])
    odp.write(id[i])
    odp.write("\n")