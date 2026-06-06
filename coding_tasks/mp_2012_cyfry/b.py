plik=open("cyfry.txt", "r")
lista=plik.readlines()
odp=open("zadanie4.txt", "a")
maxi=0
maximum=""
mini=1000000000
minimum=""
for i in range(len(lista)-1):
    lista[i]=lista[i].strip()
    suma=0
    for c in range(len(lista[i])):
        suma+=int(lista[i][c])
    if maxi<suma:
        maxi=suma
        maximum=lista[i]
    if mini>suma:
        mini=suma
        minimum=lista[i]
print(maximum)
print(minimum)
odp.write(str("b"))
odp.write("\n")
odp.write(str(maximum))
odp.write("\n")
odp.write(str(minimum))
odp.write("\n")