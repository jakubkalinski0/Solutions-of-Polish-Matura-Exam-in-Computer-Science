plik=open("liczby.txt", "r")
lista=plik.readlines()
odp=open("zad_5.txt", "w")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    pierwiastek=int(int(lista[i])**0.5)
    czy=0
    if pierwiastek<2:
        czy=0
    for j in range(2,pierwiastek):
        if pierwiastek%j==0:
            czy=0
            break
        else:
            czy=1
    if pierwiastek==2:
        czy=1
    if czy==1 and (int(lista[i])**0.5).is_integer():
        print(lista[i])
        odp.write(str(lista[i]))
        odp.write("\n")