plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki_6_4.txt","w")
suma=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if lista[i][len(lista[i])-1]=="8":
        liczba=0
        for j in range(len(lista[i])-1):
            liczba+=int(lista[i][j])*(8**(len(lista[i])-2-j))
        suma+=liczba
print(suma)
odp.write(f'{suma}')