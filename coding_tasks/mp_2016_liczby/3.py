plik=open("dane_6.txt", "r")
lista=plik.readlines()
ile=0
odp=open("wyniki_6.txt", "a")
pierwsze=[]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    czy=0
    liczba=int(lista[i])
    pierwiastek=liczba**0.5
    if liczba<2:
        czy=0
    for j in range(2,int(pierwiastek)+1):
        if liczba%j==0:
            czy=0
            break
        else:
            czy=1
    if liczba==2:
        czy=1
    if czy==1:
        pierwsze.append(int(lista[i]))
wyniki=[]
for i in range(len(pierwsze)-1):
    if abs(pierwsze[i]-pierwsze[i+1])==2:
        ile+=1
        wyniki.append(pierwsze[i])
        wyniki.append(pierwsze[i+1])
print(ile)
odp.write("3")
odp.write("\n")
odp.write(str(ile))
for i in range(0,len(wyniki),2):
    print(wyniki[i],wyniki[i+1])
    odp.write("\n")
    odp.write(str(wyniki[i])+" "+str(wyniki[i+1]))