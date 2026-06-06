plik=open("cyfry.txt", "r")
lista=plik.readlines()
odp=open("zadanie4.txt", "a")
odp.write("c")
odp.write("\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    czy=0
    for c in range(len(lista[i])-1):
        if lista[i][c]<lista[i][c+1]:
            czy=1
        else:
            czy=0
            break
    if czy==1:
        print(lista[i])
        odp.write(lista[i])
        odp.write("\n")