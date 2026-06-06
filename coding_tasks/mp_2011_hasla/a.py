plik=open("hasla.txt", "r")
lista=plik.readlines()
parzyste=0
nieparzyste=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=len(lista[i])
    if lista[i]%2==0:
        parzyste+=1
    else:
        nieparzyste+=1
odp=open("wyniki4a.txt", "w")
odp.write("parzyste:")
odp.write(str(parzyste))
odp.write("\nnieparzyste:")
odp.write(str(nieparzyste))
print("parzyste:",parzyste,"nieparzyste:",nieparzyste)