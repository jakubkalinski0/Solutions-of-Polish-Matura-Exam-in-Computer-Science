plik=open("instrukcje.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write("4")
odp.write("\n")
napis=[]
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    if lista[i][0]=="DOPISZ":
        napis.append(lista[i][1])
    if lista[i][0]=="ZMIEN":
        napis[len(napis)-1]=lista[i][1]
    if lista[i][0]=="USUN":
        napis.pop()
    if lista[i][0]=="PRZESUN":
        for j in range(len(napis)):
            if napis[j]==lista[i][1]:
                znak=chr((ord(napis[j])-65+1)%26+65)
                napis[j]=znak
                break
print("".join(napis))
odp.write("".join(napis))