plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write(f'2\n')
maksroz=0
liczba=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if abs(int(lista[i][::-1])-int(lista[i]))>maksroz:
        maksroz=abs(int(lista[i][::-1])-int(lista[i]))
        liczba=lista[i]
print(liczba, maksroz)
odp.write(f'{liczba, maksroz}\n')