plik = open("binarne.txt", "r")
lista = plik.readlines()
odp = open("zadanie4.txt", "a")
odp.write("3")
odp.write("\n")
def binnadec(liczba):
    dec=0
    for i in range(len(liczba)):
        if liczba[i]=="1":
            dec+=2**(len(liczba)-1-i)
    return dec
maxliczbabin=0
maxliczbadec=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if binnadec(lista[i])<=65535:
        if binnadec(lista[i])>maxliczbadec:
            maxliczbabin=lista[i]
            maxliczbadec=binnadec(lista[i])
print(maxliczbabin, maxliczbadec)
odp.write(str(maxliczbabin))
odp.write("\n")
odp.write(str(maxliczbadec))
odp.write("\n")