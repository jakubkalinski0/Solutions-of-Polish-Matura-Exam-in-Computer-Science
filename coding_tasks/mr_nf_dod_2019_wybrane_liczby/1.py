plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki4_1.txt","w")
def czypierwsza(liczba):
    if liczba<2:
        return False
    for j in range(2,int(liczba**(1/2))+1):
        if liczba%j==0:
            return False
    return True
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if int(lista[i])>=100 and int(lista[i])<=5000 and czypierwsza(int(lista[i])):
        print(lista[i])
        odp.write(f'{lista[i]}\n')