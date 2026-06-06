plik=open("napisy.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write(f'2\n')
napis=""
ktora=0
for i in range(19,len(lista),20):
    lista[i]=lista[i].strip()
    napis+=lista[i][ktora]
    ktora+=1
print(napis)
odp.write(f'{napis}\n')