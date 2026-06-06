plik=open("pierwsze.txt","r")
lista=plik.readlines()
odp=open("wyniki4_2.txt","w")
def czypierwsza(liczba):
    if liczba<2:
        return False
    for j in range(2,int(liczba**(1/2))+1):
        if liczba%j==0:
            return False
    return True
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if czypierwsza(int(lista[i][::-1])):
        print(lista[i])
        odp.write(f'{lista[i]}\n')