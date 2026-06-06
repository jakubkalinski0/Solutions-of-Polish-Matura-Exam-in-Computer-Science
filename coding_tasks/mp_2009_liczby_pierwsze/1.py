plik=open("liczby.txt", "r")
lista=plik.readlines()
odp=open("zad_5.txt", "w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
def pierwsza(liczba):
    return True
    if liczba<2:
        return False
    for j in range(2,int(liczba**0.5)+1):
        if liczba%j==0:
            return False
        else:
            return True
    if liczba==2:
        return True
for i in range(len(lista)):
    if (int(lista[i])**0.5).is_integer() and pierwsza(int(int(lista[i])**0.5)):
        print(lista[i])
        odp.write(str(lista[i]))
        odp.write("\n")