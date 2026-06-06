plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki_6_5.txt","w")
min=10000000000000000
kodmin=0
max=0
kodmax=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    podstawa=int(lista[i][len(lista[i])-1])
    liczba=0
    for j in range(len(lista[i])-1):
        liczba+=int(lista[i][j])*(podstawa**(len(lista[i])-2-j))
    if liczba>max:
        max=liczba
        kodmax=lista[i]
    if liczba<min:
        min=liczba
        kodmin=lista[i]
print(min,kodmin)
print(max,kodmax)
odp.write(f'{min, kodmin}\n')
odp.write(f'{max, kodmax}')