plik=open("sygnaly.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write("3\n")
rozne=[]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    maxi=0
    mini=1000
    rozne.append(set(lista[i]))
    maxi=max(rozne[i])
    mini=min(rozne[i])
    if ord(maxi)-ord(mini)<=10:
        print(lista[i])
        odp.write(str(lista[i]))
        odp.write("\n")