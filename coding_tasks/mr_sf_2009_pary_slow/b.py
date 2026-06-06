plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("zad_5.txt","a")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    slowo1=lista[i][0]
    slowo2=lista[i][1]
    for j in range(len(slowo1)-len(slowo2)+1):
        if slowo2==slowo1[j:len(slowo2)+j]:
            ile+=1
            break
print(ile)
odp.write("b")
odp.write("\n")
odp.write(str(ile))
odp.write("\n")