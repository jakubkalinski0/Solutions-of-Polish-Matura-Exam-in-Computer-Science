plik=open("punkty.txt","r")
lista=plik.readlines()
plik.close()
odp=open("zadanie4.txt","w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
def dl_boku(p1,p2):
    b=(int(p1[0])-int(p2[0]))**2+(int(p1[1])-int(p2[1]))**2
#nie ma pierwiastka bo korzystajac z twierdzenia pitagorasa kazdy bok podnosimy do kwadratu co usuwa pierwiastek
    return b
def czy_trojkat_prostokatny(boki):
    if boki[0]+boki[1]==boki[2]:
#nie ma kwadratow w twierdzeniu pitagorasa poniewaz usunely sie wraz z pierwiastkiem, ktory występowal w trakcie liczenia dlugosci boku
        return True
    else:
        return False
N=int(lista[0][0])
trojkaty=[]
ile=0
for i in range(N):
    punkt1=lista[i+1]
    for j in range(i+1,N):
        punkt2=lista[j+1]
        for k in range(j+1,N):
            punkt3=lista[k+1]
            boki=[]
            boki.append(dl_boku(punkt1,punkt2))
            boki.append(dl_boku(punkt2,punkt3))
            boki.append(dl_boku(punkt1,punkt3))
            boki.sort()
            if czy_trojkat_prostokatny(boki):
                trojkaty.append([i,j,k])
                ile+=1
print(ile)
odp.write(f'{ile}\n')
for i in range(len(trojkaty)):
    print(trojkaty[i][0],trojkaty[i][1],trojkaty[i][2])
    odp.write(f'{trojkaty[i][0]} {trojkaty[i][1]} {trojkaty[i][2]}\n')
odp.close()