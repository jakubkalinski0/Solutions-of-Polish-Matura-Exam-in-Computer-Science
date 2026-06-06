plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("wyniki6.txt","a")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
ile=0
for i in range(len(lista)):
    for j in range(len(lista[i])):
        czy=0
        if i>0 and abs(int(lista[i][j])-int(lista[i-1][j]))>128:
            czy=1
        if i<199 and abs(int(lista[i][j])-int(lista[i+1][j]))>128:
            czy=1
        if j>0 and abs(int(lista[i][j])-int(lista[i][j-1]))>128:
            czy=1
        if j<319 and abs(int(lista[i][j])-int(lista[i][j+1]))>128:
            czy=1
        ile+=czy
print(ile)
odp.write("3\n")
odp.write(str(ile))
odp.write("\n")