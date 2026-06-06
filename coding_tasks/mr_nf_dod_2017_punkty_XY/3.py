plik=open("punkty.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write(f'{3}\n')
def odl(XA,YA,XB,YB):
    odleglosc=((int(XB)-int(XA))**2+(int(YB)-int(YA))**2)**(1/2)
    odleglosc=round(odleglosc)
    return odleglosc
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
maxodl=0
for i in range(len(lista)):
    for j in range(len(lista)):
        odleglosc=odl(lista[i][0],lista[i][1],lista[j][0],lista[j][1])
        if odleglosc>maxodl:
            maxodl=odleglosc
            punkt1=lista[i]
            punkt2=lista[j]
print(maxodl)
print(punkt1[0],punkt1[1],";",punkt2[0],punkt2[1])
odp.write(f'{maxodl,punkt1[0],punkt1[1],punkt2[0],punkt2[1]}\n')