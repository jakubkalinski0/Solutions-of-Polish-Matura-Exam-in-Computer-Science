plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki_6_3.txt","w")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if lista[i][len(lista[i])-1]=="2" and lista[i][len(lista[i])-2]=="0":
        ile+=1
print(ile)
odp.write(f'{ile}')