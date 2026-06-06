plik=open("kody.txt","r")
lista=plik.readlines()
odp=open("kody1.txt","w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i][::-1]
    suma1=0
    suma2=0
    for j in range(0,len(lista[i]),2):
        suma1+=int(lista[i][j])
    for k in range(1,len(lista[i]),2):
        suma2+=int(lista[i][k])
    print(suma1, suma2)
    odp.write(str(suma1))
    odp.write(" ")
    odp.write(str(suma2))
    odp.write("\n")