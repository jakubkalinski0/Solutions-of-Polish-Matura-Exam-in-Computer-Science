plik=open("anagram.txt","r")
lista=plik.readlines()
odp=open("odp_4b.txt","w")
def sortowanie(litery):
    n=len(litery)
    while n>=0:
        for j in range(n-1):
            if ord(litery[j])>ord(litery[j+1]):
                pom=litery[j+1]
                litery[j+1]=litery[j]
                litery[j]=pom
        n=n-1
    return "".join(litery)
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    czy1=1
    for j in range(len(lista[i])-1):
        if len(lista[i][j])!=len(lista[i][j+1]):
            czy=0
            break
    if czy1==1:
        if sortowanie(list(lista[i][0]))==sortowanie(list(lista[i][1])) and sortowanie(list(lista[i][0]))==sortowanie(list(lista[i][2])) and sortowanie(list(lista[i][0]))==sortowanie(list(lista[i][3])) and sortowanie(list(lista[i][0]))==sortowanie(list(lista[i][4])):
            print(lista[i])
            for z in range(len(lista[i])):
                odp.write(lista[i][z])
                odp.write(" ")
            odp.write("\n")