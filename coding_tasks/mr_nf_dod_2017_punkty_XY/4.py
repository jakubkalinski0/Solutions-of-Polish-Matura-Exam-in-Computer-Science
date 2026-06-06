plik=open("punkty.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write(f'{4}\n')
wew=0
zew=0
bok=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    if int(lista[i][0])<5000 and int(lista[i][1])<5000:
        wew+=1
    if int(lista[i][0])==5000 or int(lista[i][1])==5000:
        bok+=1
    if int(lista[i][0])>5000 or int(lista[i][1])>5000:
        zew+=1
print(wew,bok,zew)
odp.write(f'{wew,bok,zew}')