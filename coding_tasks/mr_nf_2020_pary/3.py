plik=open("pary.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write("3")
odp.write("\n")
rowne=[]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    if int(lista[i][0])==len(lista[i][1]):
        rowne.append(lista[i])
for i in range(len(rowne)):
    czy=1
    for j in range(len(rowne)):
        if i!=j:
            if int(rowne[i][0])>int(rowne[j][0]):
                czy=0
            elif int(rowne[i][0])==int(rowne[j][0]):
                for n in range(min(len(rowne[i][1]),len(rowne[j][1]))):
                    if ord(rowne[i][1][n])>ord(rowne[j][1][n]):
                        czy=0
                        break
                    elif ord(rowne[i][1][n])<ord(rowne[j][1][n]):
                        break
    if czy==1:
        print(rowne[i])
        odp.write(f'{rowne[i][0]} {rowne[i][1]}')
        odp.write("\n")