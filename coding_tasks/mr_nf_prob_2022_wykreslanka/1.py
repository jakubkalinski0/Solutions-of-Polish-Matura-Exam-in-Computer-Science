plik=open("wykreslanka.txt","r")
lista=plik.readlines()
odp=open("zadanie4.txt","w")
odp.write(f'ZAD 4.1\n')
for i in range(len(lista)):
    lista[i]=lista[i].strip()
def znajdz_wiersze(lista):
    wiersze=[]
    for w in range(len(lista)):
        for k in range(len(lista[w])-5):
            slowo=""
            slowo=lista[w][k:k+6]
            if slowo=="matura":
                wiersze.append(w)
    return wiersze
def znajdz_kolumny(lista):
    kolumny=[]
    for w in range(len(lista)-5):
        for k in range(len(lista[w])):
            slowo=""
            slowo=lista[w][k]+lista[w+1][k]+lista[w+2][k]+lista[w+3][k]+lista[w+4][k]+lista[w+5][k]
            if slowo=="matura":
                kolumny.append(k)
    return kolumny
wiersze=sorted(list(set(znajdz_wiersze(lista))))
kolumny=sorted(list(set(znajdz_kolumny(lista))))
odp.write(f'WIERSZE:\n')
for i in wiersze:
    odp.write(f'{str(i)}\n')
odp.write(f'KOLUMNY:\n')
for i in kolumny:
    odp.write(f'{str(i)}\n')