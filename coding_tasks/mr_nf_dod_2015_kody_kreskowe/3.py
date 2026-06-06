plik=open("kody.txt","r")
lista=plik.readlines()
plik2=open("cyfra_kodkreskowy.txt","r")
lista2=plik2.readlines()
odp=open("kody3.txt","w")
jakikod={}
for i in range(len(lista2)):
    lista2[i]=lista2[i].strip()
    lista2[i]=lista2[i].split()
    jakikod[lista2[i][0]]=lista2[i][1]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    kod="11011010"
    for j in range(len(lista[i])):
        kod+=jakikod[lista[i][j]]
    lista[i]=lista[i][::-1]
    suma1=0
    suma2=0
    for k in range(0,len(lista[i]),2):
        suma1+=int(lista[i][k])
    for l in range(1,len(lista[i]),2):
        suma2+=int(lista[i][l])
    kontrolna=(10-(3*suma1+suma2)%10)%10
    kodkontrolna=jakikod[str(kontrolna)]
    kod+=kodkontrolna
    kod+="11010110"
    print(kod)
    odp.write(kod)
    odp.write("\n")