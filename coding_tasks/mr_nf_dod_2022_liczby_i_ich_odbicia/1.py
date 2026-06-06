plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","w")
odp.write(f'1\n')
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if int(lista[i][::-1])%17==0:
        print(lista[i][::-1])
        odp.write(f'{lista[i][::-1]}\n')