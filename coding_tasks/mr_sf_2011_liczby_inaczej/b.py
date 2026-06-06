plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("zadanie6.txt","a")
odp.write("b")
odp.write("\n")
dec=[]
def binnadec(liczba):
    dec=0
    for i in range(len(liczba)):
        if liczba[i]=="1":
            dec+=2**(len(liczba)-1-i)
    return dec
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    dec.append(binnadec(lista[i]))
print(max(dec))
print(lista[dec.index(max(dec))])
odp.write(str(max(dec)))
odp.write(" ")
odp.write(lista[dec.index(max(dec))])
odp.write("\n")