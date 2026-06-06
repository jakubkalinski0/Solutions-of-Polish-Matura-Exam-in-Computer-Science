plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","w")
odp.write("1\n")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
potega=0
i=0
potegi=[]
czy=True
while czy:
    potega=3**i
    if potega<=100000:
        potegi.append(str(potega))
        czy=True
    if potega>100000:
        czy=False
        break
    i+=1
for i in range(len(lista)):
    for j in range(len(potegi)):
        if lista[i]==potegi[j]:
            ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")