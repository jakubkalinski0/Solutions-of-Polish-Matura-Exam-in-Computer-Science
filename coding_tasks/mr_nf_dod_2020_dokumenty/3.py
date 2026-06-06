plik=open("identyfikator.txt","r")
lista=plik.readlines()
odp=open("wyniki4_3.txt","w")
literynaliczby={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35}
wagi={0:7,1:3,2:1,4:7,5:3,6:1,7:7,8:3}
id=[]
maxsuma=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    suma=0
    for j in range(3):
        suma+=literynaliczby[lista[i][j]]*wagi[j]
    for j in range(4,len(lista[i])):
        suma+=int(lista[i][j])*wagi[j]
    if (suma%10)!=int(lista[i][3]):
        id.append(lista[i])
for i in range(len(id)):
    print(id[i])
    odp.write(id[i])
    odp.write("\n")