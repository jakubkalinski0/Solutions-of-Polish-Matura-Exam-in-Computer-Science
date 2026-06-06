plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write(f'4\n')
for i in range(len(lista)):
    lista[i]=lista[i].strip()
ileroz=len(set(lista))
ile2=0
ile3=0
rozne=list(set(lista))
for i in range(len(rozne)):
    ile=0
    for j in range(len(lista)):
        if rozne[i]==lista[j]:
            ile+=1
    if ile==2:
        ile2+=1
    if ile==3:
        ile3+=1
print(ileroz, ile2, ile3)
odp.write(f'{ileroz,ile2,ile3}\n')