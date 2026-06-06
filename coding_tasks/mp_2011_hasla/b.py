plik=open("hasla.txt", "r")
lista=plik.readlines()
odp=open("wyniki4b.txt", "w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    czy=0
    for z in range(len(lista[i])//2):
        if lista[i][z]==lista[i][-1-z]:
            czy=1
        else:
            czy=0
            break
    if czy==1:
        print(lista[i])
        odp.write(lista[i])
        odp.write("\n")