plik=open("dane.txt", "r")
lista=plik.readlines()
odp=open("zadanie4.txt", "w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    czy=0
    for k in range(len(lista[i])//2):
        if lista[i][k]!=lista[i][-k-1]:
            czy=0
            break
        else:
            czy=1
    if czy==1:
        print(lista[i])
        odp.write(str(lista[i]))
        odp.write("\n")