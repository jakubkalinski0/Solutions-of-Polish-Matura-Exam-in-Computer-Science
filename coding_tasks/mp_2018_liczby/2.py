plik=open("liczby.txt", "r")
lista=plik.readlines()
odp=open("wynik5.txt", "a")
palindromy=[]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    czy=0
    for j in range(len(lista[i])//2+1):
        if lista[i][j]!=lista[i][-j-1]:
            czy=0
            break
        else:
            czy=1
    if czy==1:
        palindromy.append(lista[i])
odp.write("2")
odp.write("\n")
for i in range(len(palindromy)):
    print(palindromy[i])
    odp.write(str(palindromy[i]))
    odp.write("\n")