plik=open("punkty.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","w")
odp.write(f'{1}\n')
def czypierwsza(liczba):
    if liczba<2:
        return False
    for i in range(2,int(liczba**(1/2))+1):
        if liczba%i==0:
            return False
    return True
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    if czypierwsza(int(lista[i][0])) and czypierwsza(int(lista[i][1])):
        ile+=1
print(ile)
odp.write(f'{ile}\n')