plik=open("napisy.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","w")
odp.write(f'1\n')
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    for j in range(len(lista[i])):
        if lista[i][j].isdigit():
            ile+=1
print(ile)
odp.write(f'{ile}\n')