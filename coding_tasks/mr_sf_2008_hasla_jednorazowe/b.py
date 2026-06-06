plik=open("slowa.txt","r")
lista=plik.readlines()
odp1=open("hasla_b.txt","w")
odp2=open("slowa_b.txt","w")
dwanascie=[]
def palindrom(napis):
    czy=0
    while czy==0:
        if napis!=napis[::-1]:
            napis=napis[:-1]
            czy=0
        else:
            czy=1
    return napis
suma=0
najdluzsze=0
najdluzsze_slowo=""
najkrotsze=1000000000
najkrotsze_slowo=""
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    najd_palindrom=palindrom(lista[i])
    reszta=lista[i][len(najd_palindrom)::]
    odwrocone=reszta[::-1]
    haslo=odwrocone+najd_palindrom+reszta
    print(haslo)
    odp1.write(haslo)
    odp1.write("\n")
    if len(haslo)==12:
        dwanascie.append(haslo)
    if len(haslo)>najdluzsze:
        najdluzsze=len(haslo)
        najdluzsze_slowo=haslo
    if len(haslo)<najkrotsze:
        najkrotsze=len(haslo)
        najkrotsze_slowo=haslo
    suma+=len(haslo)
print(dwanascie, najdluzsze_slowo, najkrotsze_slowo, suma)
odp2.write("1")
odp2.write("\n")
for i in range(len(dwanascie)):
    odp2.write(dwanascie[i])
    odp2.write("\n")
odp2.write("2")
odp2.write("\n")
odp2.write(str(najdluzsze_slowo))
odp2.write("\n")
odp2.write(str(najkrotsze_slowo))
odp2.write("\n")
odp2.write("3")
odp2.write("\n")
odp2.write(str(suma))