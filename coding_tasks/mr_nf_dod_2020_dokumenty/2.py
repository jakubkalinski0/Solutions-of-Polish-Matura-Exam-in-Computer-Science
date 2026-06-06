plik=open("identyfikator.txt","r")
lista=plik.readlines()
odp=open("wyniki4_2.txt","w")
def czypalindrom(ciag):
    if ciag==ciag[::-1]:
        return True
    else:
        return False
id=[]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    suma=0
    if czypalindrom(lista[i][:3]) or czypalindrom(lista[i][3:]):
        id.append(lista[i])
for i in range(len(id)):
    print(id[i])
    odp.write(id[i])
    odp.write("\n")