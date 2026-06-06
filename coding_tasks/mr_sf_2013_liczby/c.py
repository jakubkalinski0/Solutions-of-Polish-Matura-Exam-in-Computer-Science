plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("wyniki6.txt","a")
odp.write("c")
odp.write("\n")
ile=0
min1=10000000
min2=0
max1=-1
max2=0
def octtodec(liczba):
    suma=0
    for i in range(len(liczba)):
        suma+=int(liczba[i])*(8**(len(liczba)-1-i))
    return suma
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    czy=1
    for j in range(len(lista[i])-1):
        if lista[i][j]>lista[i][j+1]:
            czy=0
            break
    if czy==1:
        ile+=1
        if octtodec(lista[i])<min1:
            min1=octtodec(lista[i])
            min2=lista[i]
        if octtodec(lista[i])>max1:
            max1=octtodec(lista[i])
            max2=lista[i]
print(ile)
print(min2)
print(max2)
odp.write(str(ile))
odp.write("\n")
odp.write(min2)
odp.write("\n")
odp.write(max2)