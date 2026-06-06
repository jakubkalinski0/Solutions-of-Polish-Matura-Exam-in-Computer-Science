plik=open("kody.txt","r")
lista=plik.readlines()
plik2=open("cyfra_kodkreskowy.txt","r")
lista2=plik2.readlines()
odp=open("kody2.txt","w")
jakikod={}
for i in range(len(lista2)):
    lista2[i]=lista2[i].strip()
    lista2[i]=lista2[i].split()
    jakikod[lista2[i][0]]=lista2[i][1]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i][::-1]
    kontrolna=0
    kodkontrolna=""
    suma1=0
    suma2=0
    for j in range(0,len(lista[i]),2):
        suma1+=int(lista[i][j])
    for k in range(1,len(lista[i]),2):
        suma2+=int(lista[i][k])
    kontrolna=(10-(3*suma1+suma2)%10)%10
    kodkontrolna=jakikod[str(kontrolna)]
    print(kontrolna, kodkontrolna)
    odp.write(f'{kontrolna} {kodkontrolna}\n')