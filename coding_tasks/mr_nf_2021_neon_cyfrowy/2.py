plik=open("instrukcje.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write("2")
odp.write("\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
instrukcja1=lista[0][0]
instrukcja3=""
ile1=1
ile2=0
for i in range(1,len(lista)):
    instrukcja2=lista[i][0]
    if instrukcja1==instrukcja2:
        ile1+=1
    else:
        if ile1>ile2:
            ile2=ile1
            instrukcja3=instrukcja1
        instrukcja1=lista[i][0]
        ile1=1
print(instrukcja3, ile2)
odp.write(str(instrukcja3))
odp.write(" ")
odp.write(str(ile2))
odp.write("\n")