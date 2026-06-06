plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write("3")
odp.write("\n")
def czypierwsza(liczba):
    for i in range(2,int(liczba**0.5)+1):
        if liczba%i==0:
            return False
    return True
for i in range(len(lista)):
    suma=0
    lista[i]=lista[i].strip()
    liczba=int(lista[i])
    if 4000<=liczba<=5000 and czypierwsza(liczba):
        print(lista[i])
        odp.write(str(lista[i]))
        odp.write("\n")