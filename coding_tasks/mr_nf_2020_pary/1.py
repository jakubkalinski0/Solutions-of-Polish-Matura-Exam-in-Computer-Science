plik=open("pary.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","w")
odp.write("1")
odp.write("\n")
def pierwsza(liczba):
    if liczba<4:            #4 bo hipoteza Goldbacha mówi o parzystych liczbach całkowitych WIĘKSZYCH OD 4
        return False
    for j in range(2,int(liczba**0.5)+1):
        if liczba%j==0:
            return False
    return True
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    liczba1=0
    liczba1odp=0
    liczba2=0
    liczba2odp=0
    roznica=-1
    if int(lista[i][0])%2==0 and int(lista[i][0])>4:
        for z in range(3,(int(lista[i][0])//2)+1):
            liczba1=z
            liczba2=int(lista[i][0])-liczba1
            if abs(liczba1-liczba2)>roznica and pierwsza(liczba1) and pierwsza(liczba2):
                liczba1odp=liczba1
                liczba2odp=liczba2
                roznica=abs(liczba1-liczba2)
        print(lista[i][0],liczba1odp,liczba2odp)
        odp.write(str(lista[i][0]))
        odp.write(" ")
        odp.write(str(liczba1odp))
        odp.write(" ")
        odp.write(str(liczba2odp))
        odp.write("\n")