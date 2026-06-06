plik=open("liczby.txt","r")
lista=plik.readlines()
ile=0
odp=open("wyniki4.txt","w")
odp.write("1")
odp.write("\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if int(lista[i])%2!=0:
        ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")