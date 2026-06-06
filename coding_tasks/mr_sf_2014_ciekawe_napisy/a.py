plik=open("NAPIS.TXT","r")
lista=plik.readlines()
odp=open("ZADANIE5.txt","w")
odp.write("a")
odp.write("\n")
ile=0
def czypierwsza(liczba):
    if liczba<2:
        return False
    for i in range(2,int(liczba**(1/2))+1):
        if liczba%i==0:
            return False
    return True
for i in range(len(lista)):
     lista[i]=lista[i].strip()
     suma=0
     for j in range(len(lista[i])):
         suma+=ord(lista[i][j])
     if czypierwsza(suma):
         ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")