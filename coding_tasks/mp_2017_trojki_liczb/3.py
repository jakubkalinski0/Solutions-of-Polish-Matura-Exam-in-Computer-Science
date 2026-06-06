plik=open("liczby.txt", "r")
lista=plik.readlines()
odp=open("wyniki4.txt", "a")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    lista[i]="".join(lista[i])
sumy=[]
for i in range(len(lista)):
    suma=0
    liczba=int(lista[i])
    for j in range(len(str(liczba))):
        suma+=liczba%10
        liczba=liczba//10
    sumy.append(int(suma))
ile35=0
ilemax=0
maxi=max(sumy)
for i in range(len(sumy)):
    if sumy[i]==35:
        ile35+=1
    if sumy[i]==maxi:
        ilemax+=1
print(ile35)
print(maxi)
print(ilemax)
odp.write("3")
odp.write("\n")
odp.write(str(ile35))
odp.write("\n")
odp.write(str(maxi))
odp.write("\n")
odp.write(str(ilemax))
odp.write("\n")