plik=open("liczby.txt", "r")
lista=plik.readlines()
odp=open("wyniki4.txt", "a")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
def nwd(a,b):
    while b!=0:
        pom=int(a)%int(b)
        a=b
        b=pom
    return a
suma=0
for i in range(len(lista)):
    suma+=nwd(nwd(lista[i][0],lista[i][1]),nwd(lista[i][1],lista[i][2]))
print(suma)
odp.write("2")
odp.write("\n")
odp.write(str(suma))
odp.write("\n")
