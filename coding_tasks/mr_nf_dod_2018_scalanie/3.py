plik1=open("dane1.txt","r")
lista1=plik1.readlines()
plik2=open("dane2.txt","r")
lista2=plik2.readlines()
odp=open("wynik4_3.txt","w")
wiersze=[]
ile=0
for i in range(len(lista1)):
    lista1[i]=lista1[i].strip()
    lista1[i]=lista1[i].split()
    lista2[i]=lista2[i].strip()
    lista2[i]=lista2[i].split()
    if set(lista1[i])==set(lista2[i]):
        ile+=1
        wiersze.append(i+1)
print(ile)
for i in range(len(wiersze)):
    print(wiersze[i])
odp.write(f'{ile, wiersze[i]}')