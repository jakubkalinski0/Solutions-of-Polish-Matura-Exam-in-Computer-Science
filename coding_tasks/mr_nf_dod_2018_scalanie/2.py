plik1=open("dane1.txt","r")
lista1=plik1.readlines()
plik2=open("dane2.txt","r")
lista2=plik2.readlines()
odp=open("wynik4_2.txt","w")
ile=0
for i in range(len(lista1)):
    lista1[i]=lista1[i].strip()
    lista1[i]=lista1[i].split()
    lista2[i]=lista2[i].strip()
    lista2[i]=lista2[i].split()
    parz1=0
    parz2=0
    for j in range(len(lista1[i])):
        if int(lista1[i][j])%2==0:
            parz1+=1
    for j in range(len(lista2[i])):
        if int(lista2[i][j])%2==0:
            parz2+=1
    if parz1==5 and parz2==5:
        ile+=1
print(ile)
odp.write(f'{ile}')