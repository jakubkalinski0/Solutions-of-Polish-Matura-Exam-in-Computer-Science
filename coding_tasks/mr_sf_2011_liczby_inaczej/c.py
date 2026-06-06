plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("zadanie6.txt","a")
odp.write("c")
odp.write("\n")
ile=0
suma=0
dec=[]
def binnadec(liczba):
    dec=0
    for i in range(len(liczba)):
        if liczba[i]=="1":
            dec+=2**(len(liczba)-1-i)
    return dec
def decnabin(liczba):
    bin=""
    while liczba>0:
        bin=str(liczba%2)+bin
        liczba=liczba//2
    return bin
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if len(lista[i])==9:
        ile+=1
        suma+=binnadec(lista[i])
print(ile)
print(decnabin(suma))
odp.write(str(ile))
odp.write(" ")
odp.write(decnabin(suma))
odp.write("\n")