plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wynik4.txt","a")
dwa=0
osiem=0
def dec(liczba):
    decy=0
    for j in range(len(liczba)):
        if liczba[-1-j]=="1":
            decy+=2**j
    return decy
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if dec(lista[i])%2==0:
        dwa+=1
    if dec(lista[i])%8==0:
        osiem+=1
print(dwa)
print(osiem)
odp.write("2")
odp.write("\n")
odp.write(str(dwa))
odp.write("\n")
odp.write(str(osiem))
odp.write("\n")