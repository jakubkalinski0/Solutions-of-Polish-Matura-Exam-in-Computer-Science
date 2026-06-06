plik=open("napisy.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write(f'3\n')
def czypalindrom(napis):
    if napis==napis[::-1]:
        return True
    else:
        return False
haslo=""
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if czypalindrom(lista[i][len(lista[i])-1]+lista[i]):
        haslo+=lista[i][24]
    if czypalindrom(lista[i]+lista[i][0]):
        haslo+=lista[i][25]
print(haslo)
odp.write(f'{haslo}\n')