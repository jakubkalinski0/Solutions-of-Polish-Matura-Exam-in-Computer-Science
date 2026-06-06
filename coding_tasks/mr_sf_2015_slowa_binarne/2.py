plik=open("slowa.txt","r")
lista=plik.readlines()
odp=open("wynik4.txt","a")
odp.write("2")
odp.write("\n")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    czyzero1=0
    if lista[i][0]=="0":
        czyzero1=1
    znak="0"
    zmiana=0
    for j in range(len(lista[i])):
        if lista[i][j]!=znak:
            zmiana+=1
            znak="1"
    if czyzero1==1 and zmiana==1:
        ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")