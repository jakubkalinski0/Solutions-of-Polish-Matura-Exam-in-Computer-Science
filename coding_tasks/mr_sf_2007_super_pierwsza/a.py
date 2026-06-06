odp=open("wyniki.txt","w")
odp1=open("1.txt","w")
def pierwsza(liczba):
    if liczba<2:
        return False
    for i in range(2,int(liczba**(1/2))+1):
        if liczba%i==0:
            return False
    return True
def binarna(liczba):
    LB=""
    while liczba>=1:
        if liczba%2==0:
            LB="0"+LB
        else:
            LB="1"+LB
        liczba=liczba//2
    return LB
ile=0
#2,1000
#100,10000
#1000,100000
for i in range(2,1000):
    suma1=0
    binarnie=binarna(i)
    suma2=0
    napis=str(i)
    for j in range(len(napis)):
        suma1+=int(napis[j])
    for z in range(len(binarnie)):
        suma2+=int(binarnie[z])
    if pierwsza(i) and pierwsza(suma1) and pierwsza(suma2):
        ile+=1
        print(i, suma1, binarnie, suma2)
        odp1.write(str(i))
        odp1.write("\n")
print(ile)
odp.write("a")
odp.write("\n")
odp.write(str(3))
odp.write(" ")
odp.write(str(ile))
odp.write("\n")