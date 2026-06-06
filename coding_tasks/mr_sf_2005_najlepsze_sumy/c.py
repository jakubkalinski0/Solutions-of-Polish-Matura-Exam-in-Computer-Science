odp=open("Raport5.txt","a")
odp.write("c")
odp.write("\n")
plik1=open("dane5-1.txt","r")
lista1=plik1.readlines()
plik2=open("dane5-2.txt","r")
lista2=plik2.readlines()
plik3=open("dane5-3.txt","r")
lista3=plik3.readlines()
dane=[lista1,lista2,lista3]
wyniki=[]
for i in range(len(dane)):
    for j in range(len(dane[i])):
        dane[i][j]=dane[i][j].strip()
for i in range(len(dane)):
    ciag=dane[i]
    znaki=(list(set(ciag)))
    ile2=0
    znak2=""
    for j in range(len(znaki)):
        znak1=znaki[j]
        ile1=0
        for z in range(len(ciag)):
            if znak1==ciag[z]:
                ile1+=1
        if ile1>ile2:
            ile2=ile1
            znak2=znak1
    wyniki.append(znak2)
print(wyniki)
for i in range(len(wyniki)):
    odp.write(str(wyniki[i]))
    odp.write(" ")
odp.write("\n")