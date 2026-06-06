plik=open("napisy.txt", "r")
lista=plik.readlines()
odp=open("zadanie4.txt", "w")
parzyste=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if len(lista[i])%2==0:
        parzyste+=1
print(parzyste)
odp.write("a")
odp.write("\n")
odp.write(str(parzyste))
odp.write("\n")