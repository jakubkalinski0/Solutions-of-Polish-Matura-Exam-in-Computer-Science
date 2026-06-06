plik=open("liczby.txt", "r")
lista=plik.readlines()
odp=open("wynik5.txt", "w")
parzyste=[]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if int(lista[i])%2==0:
        parzyste.append(int(lista[i]))
maxi=max(parzyste)
print(maxi)
odp.write("1")
odp.write("\n")
odp.write(str(maxi))
odp.write("\n")