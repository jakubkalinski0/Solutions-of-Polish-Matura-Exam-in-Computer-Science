plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("wyniki6.txt","w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
maxi1=-1
mini1=256
maxi2=-1
mini2=256
for i in range(len(lista)):
    for j in range(len(lista[i])):
        maxi2=int(lista[i][j])
        mini2=int(lista[i][j])
        if maxi2>maxi1:
            maxi1=maxi2
        if mini2<mini1:
            mini1=mini2
print(maxi1, mini1)
odp.write("1\n")
odp.write(str(maxi1))
odp.write("\n")
odp.write(str(mini1))
odp.write("\n")