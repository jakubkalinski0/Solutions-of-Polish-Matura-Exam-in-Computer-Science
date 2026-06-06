plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki_6_1.txt","w")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if lista[i][len(lista[i])-1]=="8":
        ile+=1
print(ile)
odp.write(f'{ile}')