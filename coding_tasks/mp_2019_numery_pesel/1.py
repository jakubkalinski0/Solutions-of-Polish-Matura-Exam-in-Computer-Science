plik=open("dane.txt", "r")
lista=plik.readlines()
odp=open("wyniki6.txt", "w")
kobiety=0
mezczyzni=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if int(lista[i][-2])%2==0:
        kobiety+=1
    else:
        mezczyzni+=1
print(kobiety)
print(mezczyzni)
odp.write("1")
odp.write("\n")
odp.write(str(kobiety))
odp.write("\n")
odp.write(str(mezczyzni))
odp.write("\n")