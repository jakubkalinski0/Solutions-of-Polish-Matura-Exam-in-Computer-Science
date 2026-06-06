odp=open("wyniki.txt","a")
def pierwsza(liczba):
    if liczba<2:
        return False
    for i in range(2,int(liczba**(1/2))+1):
        if liczba%i==0:
            return False
    return True
ile=0
#100,10000
for i in range(100,10000):
    suma=0
    napis=str(i)
    for j in range(len(napis)):
        suma+=int(napis[j])
    if pierwsza(suma):
        ile+=1
        print(i, suma)
print(ile)
odp.write("b")
odp.write("\n")
odp.write("1")
odp.write(" ")
odp.write(str(ile))
odp.write("\n")