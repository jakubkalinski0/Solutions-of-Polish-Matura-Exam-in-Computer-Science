plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki_6_2.txt","w")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if lista[i][len(lista[i])-1]=="4":
        czyzero=0
        for j in range(len(lista[i])-1):
            if lista[i][j]=="0":
                czyzero=1
                break
        if czyzero==0:
            ile+=1
print(ile)
odp.write(f'{ile}')