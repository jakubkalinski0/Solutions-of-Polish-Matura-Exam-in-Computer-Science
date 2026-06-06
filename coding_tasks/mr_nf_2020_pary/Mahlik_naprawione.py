# prawie dobrze
plik = open("przyklad.txt","r")
linie = plik.readlines()
liczby_do_badania = []
pierwsze_do_100 = []
wynik = ""
def czy_pierwsza(liczba):
    if liczba < 2:
        return
    # konieczna konwersja z float to int
    for i in range(2,int(liczba**0.5)+1):
        if liczba % i == 0:
            return False
    return True
for i in range(101):
    # konieczne sprawdzenie parzystości bo  2 jest pierwsza i parzysta, można dla i większego od 2
    if czy_pierwsza(i) and i % 2 != 0:
        pierwsze_do_100.append(i)
for linia in linie:
    linia = linia.strip()
    linia = linia.split()
    liczba = linia[0]
    liczba = int(liczba)
    if liczba > 4 and liczba % 2 == 0:
        liczby_do_badania.append(liczba)
print(liczby_do_badania)# [24, 6, 6]
print(pierwsze_do_100)
for i in range(len(liczby_do_badania)):
    for liczbapierwsza in pierwsze_do_100:
        roznica = liczby_do_badania[i] - liczbapierwsza
        if roznica in pierwsze_do_100:
            wynik += f'{liczby_do_badania[i]},{liczbapierwsza},{roznica}\n'
            break
print(wynik)