def zad4_1_wiersze(dane):
    wynik = []
    for i in range(len(dane)):
        if dane[i].find("matura") != -1:
            wynik.append(i)

    return wynik

def zad4_1_kolumny(dane):
    wynik = []

    for j in range(len(dane[0])):
        kolumna = ""
        for i in range(len(dane)):
            kolumna += dane[i][j]
        if kolumna.find("matura") != -1:
            wynik.append(j)

    return wynik

def zad4_2(dane):
    wynik = []
    maks_dlugosc_plik = 1

    for w in range(len(dane)):
        dlugosc = 1
        maks_dlugosc = 1
        for i in range(1, len(dane[w])):
            if dane[w][i] == dane[w][i - 1]:
                dlugosc += 1
                maks_dlugosc = max(dlugosc, maks_dlugosc)
            else:
                dlugosc = 1
        if maks_dlugosc == maks_dlugosc_plik:
            wynik.append(w)
        elif maks_dlugosc > maks_dlugosc_plik:
            maks_dlugosc_plik = maks_dlugosc
            wynik.clear()
            wynik.append(w)
    
    return maks_dlugosc_plik, wynik

def sprawdz(dane, i1, j1, i2, j2):
    litery = set()

    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            if dane[i][j] in litery:
                return False
            litery.add(dane[i][j])

    return len(litery) == 26
            

def zad4_3(dane):
    for i in range(len(dane)):
        for j in range(len(dane[i])):
            for i2 in range(i, len(dane)):
                wys = i2 - i + 1
                if wys > 26:
                    break
                for j2 in range(j, len(dane[i])):
                    szer = j2 - j + 1

                    if wys * szer > 26:
                        break
                    elif wys * szer != 26:
                        continue

                    if sprawdz(dane, i, j, i2, j2):
                        print(f"Wysokość: {wys}, Szerokość: {szer}, Wiersz: {i}, Kolumna: {j}")



plik = open("wykreslanka.txt")

dane = plik.read().split("\n")

plik.close()

print("Zadanie 4.1")
print("Wiersze:")
print(zad4_1_wiersze(dane))
print("Kolumny:")
print(zad4_1_kolumny(dane))

print("Zadanie 4.2")
print(zad4_2(dane))

print("Zadanie 4.3")
zad4_3(dane)
