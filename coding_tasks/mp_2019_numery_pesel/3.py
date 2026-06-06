plik=open("dane.txt", "r")
lista=plik.readlines()
odp=open("wyniki6.txt", "a")
odp.write("3")
odp.write("\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if int(int(lista[i][0])+3*int(lista[i][1])+7*int(lista[i][2])+9*int(lista[i][3])+int(lista[i][4])+3*int(lista[i][5])+7*int(lista[i][6])+9*int(lista[i][7])+int(lista[i][8])+3*int(lista[i][9])+int(lista[i][10]))%10!=0:
        print(lista[i])
        odp.write(str(lista[i]))
        odp.write("\n")