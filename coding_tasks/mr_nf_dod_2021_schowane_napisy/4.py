plik=open("napisy.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write(f'4\n')
haslo=""
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    ciag=""
    for j in range(len(lista[i])):
        if lista[i][j].isdigit():
            ciag+=lista[i][j]
    for j in range(0,len(ciag),2):
        if int(ciag[j:j+2])>=65 and int(ciag[j:j+2])<=90:
            haslo+=chr(int(ciag[j:j+2]))
    if haslo[len(haslo)-3:]=="XXX":
        break
print(haslo)
odp.write(f'{haslo}\n')