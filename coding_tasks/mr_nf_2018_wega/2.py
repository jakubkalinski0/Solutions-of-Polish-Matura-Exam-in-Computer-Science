plik=open("sygnaly.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
rozne=[]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    rozne.append("".join(set(lista[i])))
    rozne[i]=len(rozne[i])
maxi=max(rozne)
slowo=lista[rozne.index(maxi)]
print(slowo,maxi)
odp.write("2\n")
odp.write(str(slowo))
odp.write("\n")
odp.write(str(maxi))
odp.write("\n")