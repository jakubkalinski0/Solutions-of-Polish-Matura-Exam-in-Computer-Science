plik=open("hasla.txt", "r")
lista=plik.readlines()
odp=open("wyniki4c.txt", "w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    czy=0
    for z in range(len(lista[i])-1):
        if ord(lista[i][z])+ord(lista[i][(z+1)])==220:
            czy=1
            break
        else:
            czy=0
    if czy==1:
        print(lista[i])
        odp.write(lista[i])
        odp.write("\n")