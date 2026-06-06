plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("zad_5.txt","a")
ile=0
def czyAwB(slowo1,slowo2):
    for j in range(len(slowo1)-len(slowo2)+1):
        if slowo2==slowo1[j:len(slowo2)+j]:
            return True
    return False
def prefiks(slowo1,slowo2):
    for j in range(len(slowo2)):
        if slowo2[j:]==slowo1[:len(slowo2)-j]:
            return True
    return False
def sufiks(slowo1,slowo2):
    for j in range(len(slowo2)):
        if slowo2[:len(slowo2)-j]==slowo1[len(slowo1)-len(slowo2)+j:]:
            return True
    return False
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    if czyAwB(lista[i][0],lista[i][1]) or prefiks(lista[i][0],lista[i][1]) or sufiks(lista[i][0],lista[i][1]):
        ile+=0
    else:
        ile+=1
print(ile)
odp.write("c")
odp.write("\n")
odp.write(str(ile))
odp.write("\n")