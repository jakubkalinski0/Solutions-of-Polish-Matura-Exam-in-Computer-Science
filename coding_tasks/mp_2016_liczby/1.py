plik=open("dane_6.txt", "r")
lista=plik.readlines()
ile=0
odp=open("wyniki_6.txt", "w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    czy=0
    liczba=int(lista[i])
    pierwiastek=liczba**0.5
    if liczba<2:
        czy=0
    for j in range(2,int(pierwiastek)+1):
        if liczba%j==0:
            czy=0
            break
        else:
            czy=1
    if liczba==2:
        czy=1
    if czy==1:
        ile+=1
print(ile)
odp.write("1")
odp.write("\n")
odp.write(str(ile))
odp.write("\n")