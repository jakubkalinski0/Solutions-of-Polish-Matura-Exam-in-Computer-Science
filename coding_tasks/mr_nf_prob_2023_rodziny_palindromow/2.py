plik=open("slowa.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write("ZAD 4.2\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
rodziny=[]
for i in range(len(lista)):
    if lista[i]==lista[i][::-1]:
        rodziny.append(len(lista[i]))
rozne=len(set(rodziny))
print(rozne)
odp.write(f'Liczba rodzin w pliku: {rozne}\n')