plik=open("slowa.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","w")
odp.write("ZAD 4.1\n")
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
for i in range(len(lista)):
    if lista[i]==lista[i][::-1]:
        ile+=1
odp.write(f'Liczba slow, ktore sa palindromami: {ile}\n')
print(ile)