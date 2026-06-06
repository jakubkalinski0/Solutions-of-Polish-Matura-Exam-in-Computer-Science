plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("zadanie6.txt","w")
odp.write("a")
odp.write("\n")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if lista[i][len(lista[i])-1]=="0":
        ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")