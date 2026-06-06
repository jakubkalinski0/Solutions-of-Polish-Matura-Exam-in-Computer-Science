plik=open("pierwsze.txt","r")
lista=plik.readlines()
odp=open("wyniki4_3.txt","w")
def czypierwsza(liczba):
    if liczba<2:
        return False
    for j in range(2,int(liczba**(1/2))+1):
        if liczba%j==0:
            return False
    return True
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    liczba=lista[i]
    waga=1111
    while len(str(waga))!=1:
        waga=0
        for j in range(len(liczba)):
            waga+=int(liczba[j])
        liczba=str(waga)
    if waga==1:
        ile+=1
print(ile)
odp.write(str(ile))