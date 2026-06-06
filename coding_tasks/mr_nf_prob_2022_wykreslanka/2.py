plik=open("wykreslanka.txt","r")
lista=plik.readlines()
odp=open("zadanie4.txt","a")
odp.write(f'ZAD 4.2\n')
for i in range(len(lista)):
    lista[i]=lista[i].strip()
def znajdz_ciag(lista):
    najdluzszy_ciag=""
    dlugosc_najdluzszego_ciagu=0
    numery_wierszy=[]
    for w in range(len(lista)):
        ciag=lista[w][0]
        dlugosc_ciagu=1
        for k in range(1,len(lista[w])):
            if lista[w][k-1]==lista[w][k]:
                ciag+=lista[w][k]
                dlugosc_ciagu+=1
            else:
                if dlugosc_ciagu == dlugosc_najdluzszego_ciagu:
                    numery_wierszy.append(w)
                if dlugosc_ciagu>dlugosc_najdluzszego_ciagu:
                    dlugosc_najdluzszego_ciagu=dlugosc_ciagu
                    najdluzszy_ciag=ciag
                    numery_wierszy=[w]
                ciag=lista[w][k]
                dlugosc_ciagu=1
    return najdluzszy_ciag, dlugosc_najdluzszego_ciagu, numery_wierszy
odp.write(f'Dlugosc najdluzszego ciagu: {znajdz_ciag(lista)[1]}\nNajdluzszy ciag: {znajdz_ciag(lista)[0]}\n')
wiersze=znajdz_ciag(lista)[2]
odp.write(f'Wiersze, w ktorych sa te ciagi: ')
for i in range(len(wiersze)):
    odp.write(f'{str(wiersze[i])}, ')
odp.write("\n")