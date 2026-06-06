plik = open("binarne.txt", "r")
lista = plik.readlines()
odp = open("zadanie4.txt", "a")
odp.write("2")
odp.write("\n")
def binnadec(liczba):
    dec=0
    for i in range(len(liczba)):
        if liczba[i]=="1":
            dec+=2**(len(liczba)-1-i)
    return dec
ile=0
mindl=10**32
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    czypopr=1
    for j in range(0,len(lista[i]),4):
        if binnadec(lista[i][j:j+4])>9:
            czypopr=0
            break
    if czypopr==0:
        ile+=1
        if len(lista[i])<mindl:
            mindl=len(lista[i])
print(ile, mindl)
odp.write(str(ile))
odp.write("\n")
odp.write(str(mindl))
odp.write("\n")