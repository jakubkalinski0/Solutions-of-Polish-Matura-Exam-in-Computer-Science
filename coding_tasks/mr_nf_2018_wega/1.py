plik=open("sygnaly.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
nowy=""
for i in range(39,len(lista),40):
    nowy+=lista[i][9]
print(nowy)
odp.write("1\n")
odp.write(str(nowy))
odp.write("\n")