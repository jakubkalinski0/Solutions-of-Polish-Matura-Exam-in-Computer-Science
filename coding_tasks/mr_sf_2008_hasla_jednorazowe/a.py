plik=open("slowa.txt","r")
lista=plik.readlines()
odp1=open("hasla_a.txt","w")
odp2=open("slowa_a.txt","w")
najdluzsze=0
najdluzsze_slowo=""
najkrotsze=31
najkrotsze_slowo=""
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    slowo=""
    for j in range(len(lista[i])):
        slowo=lista[i][j]+slowo
    if len(slowo)>najdluzsze:
        najdluzsze=len(slowo)
        najdluzsze_slowo=slowo
    if len(slowo)<najkrotsze:
        najkrotsze=len(slowo)
        najkrotsze_slowo=slowo
    print(slowo)
    odp1.write(slowo)
    odp1.write("\n")
print(najdluzsze_slowo,najdluzsze)
odp2.write(najdluzsze_slowo)
odp2.write(" ")
odp2.write(str(najdluzsze))
odp2.write("\n")
print(najkrotsze_slowo,najkrotsze)
odp2.write(najkrotsze_slowo)
odp2.write(" ")
odp2.write(str(najkrotsze))