plik=open("wykreslanka.txt","r")
lista=plik.readlines()
odp=open("zadanie4.txt","a")
odp.write(f'ZAD 4.3\n')
for i in range(len(lista)):
    lista[i]=lista[i].strip()
def czy_wszystkie_znaki(lista):
    znaki=""
    for w in range(len(lista)):
        for k in range(len(lista[w])):
            znaki+=lista[w][k]
    if len(list(set(znaki)))==26:
        return True
    else:
        return False
def znajdz_podtablice(lista):
    for w in range(len(lista)):
        for k in range(len(lista[w])):
            szerokosc=1
            wysokosc=26
            podlista=[]
            while szerokosc<=26 and k+szerokosc<=200 and w+wysokosc<=100:
                wysokosc=26//szerokosc
                for w2 in range(wysokosc):
                    podlista.append(lista[w+w2][k:k+szerokosc])
                if czy_wszystkie_znaki(podlista):
                    return f'Wysokosc: {wysokosc} Szerokosc:{szerokosc} Wiersz lewego rogu: {w} Kolumna lewego rogu: {k}'
                else:
                    podlista=[]
                    szerokosc+=1
odp.write(znajdz_podtablice(lista))