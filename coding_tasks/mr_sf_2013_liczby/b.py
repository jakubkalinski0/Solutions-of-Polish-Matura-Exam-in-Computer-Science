plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("wyniki6.txt","a")
odp.write("b")
odp.write("\n")
ile=0
def octtodec(liczba):
    suma=0
    for i in range(len(liczba)):
        suma+=int(liczba[i])*(8**(len(liczba)-1-i))
    return str(suma)
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    dec=octtodec(lista[i])
    if dec[0]==dec[len(dec)-1]:
        ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")