plik=open("napisy.txt", "r")
lista=plik.readlines()
odp=open("zadanie4.txt", "a")
equal=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    jedynki=0
    zera=0
    for c in range(len(lista[i])):
        if int(lista[i][c])==1:
            jedynki+=1
        else:
            zera+=1
    if jedynki==zera:
        equal+=1
print(equal)
odp.write("b")
odp.write("\n")
odp.write(str(equal))
odp.write("\n")