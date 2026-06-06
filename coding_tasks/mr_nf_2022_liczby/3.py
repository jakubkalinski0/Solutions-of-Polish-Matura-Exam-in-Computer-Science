plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odptrojki=open("trojki.txt","w")
odp.write("3")
odp.write("\n")
ile3=0
trojkiodp=[]
ile5=0
piatkiodp=[]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
#POSORTUJ [lista.sort()] -> wtedy nie trzeba dawać "for i in range(len(lista)):" bo są po kole => znacznie mniej obliczeń do wykonania
for i in range(len(lista)):
    liczba1=int(lista[i])
    for j in range(len(lista)):
        liczba2=int(lista[j])
        if liczba2%liczba1==0 and liczba2!=liczba1:
            for k in range(len(lista)):
                liczba3=int(lista[k])
                if liczba3%liczba2==0 and liczba3!=liczba2:
                    trojki=[]
                    ile3+=1
                    print(liczba1,liczba2,liczba3)
                    trojki.append(liczba1)
                    trojki.append(liczba2)
                    trojki.append(liczba3)
                    trojkiodp.append(trojki)
                    for l in range(len(lista)):
                        liczba4=int(lista[l])
                        if liczba4%liczba3==0 and liczba4!=liczba3:
                            for m in range(len(lista)):
                                liczba5=int(lista[m])
                                if liczba5%liczba4==0 and liczba5!=liczba4:
                                    piatki=[]
                                    ile5+=1
                                    print(liczba1,liczba2,liczba3,liczba4,liczba5)
                                    piatki.append(liczba1)
                                    piatki.append(liczba2)
                                    piatki.append(liczba3)
                                    piatki.append(liczba4)
                                    piatki.append(liczba5)
                                    piatkiodp.append(piatki)
odp.write(str(ile3))
odp.write(" ")
odp.write(str(ile5))
odp.write("\n")
print(ile3)
for i in range(len(trojkiodp)):
    print(trojkiodp[i])
    odp.write(str(trojkiodp[i][0]))
    odp.write(" ")
    odp.write(str(trojkiodp[i][1]))
    odp.write(" ")
    odp.write(str(trojkiodp[i][2]))
    odp.write("\n")
    odptrojki.write(str(trojkiodp[i][0]))
    odptrojki.write(" ")
    odptrojki.write(str(trojkiodp[i][1]))
    odptrojki.write(" ")
    odptrojki.write(str(trojkiodp[i][2]))
    odptrojki.write("\n")
print(ile5)
for i in range(len(piatkiodp)):
    print(piatkiodp[i])
    odp.write(str(piatkiodp[i][0]))
    odp.write(" ")
    odp.write(str(piatkiodp[i][1]))
    odp.write(" ")
    odp.write(str(piatkiodp[i][2]))
    odp.write(" ")
    odp.write(str(piatkiodp[i][3]))
    odp.write(" ")
    odp.write(str(piatkiodp[i][4]))
    odp.write("\n")