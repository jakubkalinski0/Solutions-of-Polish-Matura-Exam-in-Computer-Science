plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("slowa.txt","w")
ile=0
odp.write("d")
odp.write("\n")
def czyAwB(slowo1,slowo2):
    for j in range(len(slowo1)-len(slowo2)+1):
        if slowo2==slowo1[j:len(slowo2)+j]:
            return True
    return False
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    C=""
    czy=0
    #prefiks
    czyP=0
    #sufiks
    czyS=0
    slowo1=lista[i][0]
    slowo2=lista[i][1]
    if czyAwB(lista[i][0],lista[i][1]):
        C=lista[i][0]
        czy=1
    #prefiks
    for j in range(len(slowo2)):
        if slowo2[j:]==slowo1[:len(slowo2)-j]:
            prefiks=slowo2[:len(slowo2)-j]
            czyP=1
            break
    #sufiks
    for k in range(len(slowo2)):
        if slowo2[:len(slowo2)-j]==slowo1[len(slowo1)-len(slowo2)+j:]:
            sufiks=slowo2[j:]
            czyS=1
            break
    if czy==0:
        C=slowo1+slowo2
    elif czy==1:
        C=slowo1
    elif czyP==1 and czyS==1:
        if len(prefiks)<len(sufiks):
            C=prefiks+slowo1
        else:
            C=slowo1+sufiks
    elif czyP==1 and czyS==0:
        C=prefiks+slowo1
    elif czyS==1 and czyP==0:
        C=slowo1+sufiks
    print(C)
    odp.write(C)
    odp.write("\n")
#nie wiadomo czy wyniki są dobre (NIGDZIE NIE ZNALAZŁEM ODP)