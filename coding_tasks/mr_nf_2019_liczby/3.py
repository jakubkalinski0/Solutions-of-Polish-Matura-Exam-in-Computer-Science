import math
plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write("3\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
pierwszyodp=0
ileodp=0
NWD1=1
NWD2=1
NWDodp=0
for i in range(len(lista)-1):
    pierwszy=int(lista[i])
    jeden=pierwszy
    ile=1
    for j in range(i+1,len(lista)):
        dwa=int(lista[j])
        NWD1=math.gcd(jeden,dwa)
        if NWD1==1:
            break
        if NWD1!=1:
            ile+=1
            NWD2=NWD1
            jeden=NWD2
    if ile>ileodp:
        ileodp=ile
        pierwszyodp=pierwszy
        NWDodp=NWD2
print(pierwszyodp,ileodp,NWDodp)