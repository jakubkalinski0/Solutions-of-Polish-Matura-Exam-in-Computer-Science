plik=open("slowa.txt","r")
lista=plik.readlines()
odp=open("wyniki6.txt","a")
odp.write("2")
odp.write("\n")
ile=0
def czy1w2(napis1, napis2):
    for i in range(len(napis2)-len(napis1)+1):
        if napis1==napis2[i:len(napis1)+i]:
            return True
    return False
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    if czy1w2(lista[i][0],lista[i][1]):
        ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")