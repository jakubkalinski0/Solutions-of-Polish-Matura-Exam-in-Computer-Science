plik=open("2.txt","r")
lista=plik.readlines()
odp=open("wyniki.txt","a")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=int(lista[i])
def pierwsza(liczba):
    if liczba<2:
        return False
    for i in range(2,int(liczba**(1/2))+1):
        if liczba%i==0:
            return False
    return True
#100,10000
suma=0
for i in range(len(lista)):
    suma+=lista[i]
if pierwsza(suma):
    czy="TAK"
else:
    czy="NIE"
print(czy)
odp.write("2")
odp.write(" ")
odp.write(czy)