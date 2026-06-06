plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wynik4.txt","a")
def dec(liczba):
    decy=0
    for j in range(len(liczba)):
        if liczba[-1-j]=="1":
            decy+=2**j
    return decy
maxiL=0
maxiW=0
miniL=10000000000000000000000000000000000
miniW=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if maxiL<dec(lista[i]):
        maxiL=dec(lista[i])
        maxiW=i
    if miniL>dec(lista[i]):
        miniL=dec(lista[i])
        miniW=i
print(miniW+1)
print(maxiW+1)
odp.write("3")
odp.write("\nnajmniejsza:")
odp.write(str(miniW+1))
odp.write("\nnajwieksza:")
odp.write(str(maxiW+1))
odp.write("\n")