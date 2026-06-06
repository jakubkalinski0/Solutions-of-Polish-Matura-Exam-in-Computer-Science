plik=open("anagram.txt","r")
lista=plik.readlines()
odp=open("odp_4a.txt","w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    czy=1
    for j in range(len(lista[i])-1):
        if len(lista[i][j])!=len(lista[i][j+1]):
            czy=0
            break
    if czy==1:
        print(lista[i])
        for z in range(len(lista[i])):
            odp.write(lista[i][z])
            odp.write(" ")
        odp.write("\n")