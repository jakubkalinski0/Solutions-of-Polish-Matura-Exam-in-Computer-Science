plik=open("gra.txt","r")
lista=plik.readlines()
odp=open("wyniki_5.txt","a")
odp.write("3")
odp.write("\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=list(lista[i])
#lewy górny róg
def w0k0(pokolenie,wiersz,kolumna):
    zywe=0
    if pokolenie[len(pokolenie)-1][len(pokolenie[wiersz])-1]=="X": zywe+=1
    if pokolenie[len(pokolenie)-1][kolumna]=="X": zywe+=1
    if pokolenie[len(pokolenie)-1][kolumna+1]=="X": zywe+=1
    if pokolenie[wiersz][len(pokolenie[wiersz])-1]== "X": zywe+=1
    if pokolenie[wiersz][kolumna+1]=="X": zywe+=1
    if pokolenie[wiersz+1][len(pokolenie[wiersz])-1]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna+1]=="X": zywe+=1
    return zywe
#lewy dolny róg
def wMaxk0(pokolenie,wiersz,kolumna):
    zywe=0
    if pokolenie[wiersz-1][len(pokolenie[wiersz])-1]=="X": zywe+=1
    if pokolenie[wiersz-1][kolumna]=="X": zywe+=1
    if pokolenie[wiersz-1][kolumna+1]=="X": zywe+=1
    if pokolenie[wiersz][len(pokolenie[wiersz])-1]== "X": zywe+=1
    if pokolenie[wiersz][kolumna+1]=="X": zywe+=1
    if pokolenie[0][len(pokolenie[wiersz])-1]=="X": zywe+=1
    if pokolenie[0][kolumna]=="X": zywe+=1
    if pokolenie[0][kolumna+1]=="X": zywe+=1
    return zywe
#prawy górny róg
def w0kMax(pokolenie,wiersz,kolumna):
    zywe=0
    if pokolenie[len(pokolenie)-1][kolumna-1]=="X": zywe+=1
    if pokolenie[len(pokolenie)-1][kolumna]=="X": zywe+=1
    if pokolenie[len(pokolenie)-1][0]=="X": zywe+=1
    if pokolenie[wiersz][kolumna-1]== "X": zywe+=1
    if pokolenie[wiersz][0]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna-1]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna]=="X": zywe+=1
    if pokolenie[wiersz+1][0]=="X": zywe+=1
    return zywe
#prawy dolny róg
def wMaxkMax(pokolenie,wiersz,kolumna):
    zywe=0
    if pokolenie[wiersz-1][kolumna-1]=="X": zywe+=1
    if pokolenie[wiersz-1][kolumna]=="X": zywe+=1
    if pokolenie[wiersz-1][0]=="X": zywe+=1
    if pokolenie[wiersz][kolumna-1]== "X": zywe+=1
    if pokolenie[wiersz][0]=="X": zywe+=1
    if pokolenie[0][kolumna-1]=="X": zywe+=1
    if pokolenie[0][kolumna]=="X": zywe+=1
    if pokolenie[0][0]=="X": zywe+=1
    return zywe
#góra bez rogów
def w0(pokolenie,wiersz,kolumna):
    zywe=0
    if pokolenie[len(pokolenie)-1][kolumna-1]=="X": zywe+=1
    if pokolenie[len(pokolenie)-1][kolumna]=="X": zywe+=1
    if pokolenie[len(pokolenie)-1][kolumna+1]=="X": zywe+=1
    if pokolenie[wiersz][kolumna-1]== "X": zywe+=1
    if pokolenie[wiersz][kolumna+1]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna-1]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna+1]=="X": zywe+=1
    return zywe
#dół bez rogów
def wMax(pokolenie,wiersz,kolumna):
    zywe=0
    if pokolenie[wiersz-1][kolumna-1]=="X": zywe+=1
    if pokolenie[wiersz-1][kolumna]=="X": zywe+=1
    if pokolenie[wiersz-1][kolumna+1]=="X": zywe+=1
    if pokolenie[wiersz][kolumna-1]== "X": zywe+=1
    if pokolenie[wiersz][kolumna+1]=="X": zywe+=1
    if pokolenie[0][kolumna-1]=="X": zywe+=1
    if pokolenie[0][kolumna]=="X": zywe+=1
    if pokolenie[0][kolumna+1]=="X": zywe+=1
    return zywe
#lewo bez rogów
def k0(pokolenie,wiersz,kolumna):
    zywe=0
    if pokolenie[wiersz-1][len(pokolenie[wiersz])-1]=="X": zywe+=1
    if pokolenie[wiersz-1][kolumna]=="X": zywe+=1
    if pokolenie[wiersz-1][kolumna+1]=="X": zywe+=1
    if pokolenie[wiersz][len(pokolenie[wiersz])-1]== "X": zywe+=1
    if pokolenie[wiersz][kolumna+1]=="X": zywe+=1
    if pokolenie[wiersz+1][len(pokolenie[wiersz])-1]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna+1]=="X": zywe+=1
    return zywe
#prawo bez rogów
def kMax(pokolenie,wiersz,kolumna):
    zywe=0
    if pokolenie[wiersz-1][kolumna-1]=="X": zywe+=1
    if pokolenie[wiersz-1][kolumna]=="X": zywe+=1
    if pokolenie[wiersz-1][0]=="X": zywe+=1
    if pokolenie[wiersz][kolumna-1]== "X": zywe+=1
    if pokolenie[wiersz][0]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna-1]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna]=="X": zywe+=1
    if pokolenie[wiersz+1][0]=="X": zywe+=1
    return zywe
#wnętrze bez zewnętrznych elementów
def reszta(pokolenie,wiersz,kolumna):
    zywe=0
    if pokolenie[wiersz-1][kolumna-1]=="X": zywe+=1
    if pokolenie[wiersz-1][kolumna]=="X": zywe+=1
    if pokolenie[wiersz-1][kolumna+1]=="X": zywe+=1
    if pokolenie[wiersz][kolumna-1]== "X": zywe+=1
    if pokolenie[wiersz][kolumna+1]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna-1]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna]=="X": zywe+=1
    if pokolenie[wiersz+1][kolumna+1]=="X": zywe+=1
    return zywe
pokolenie1=lista
pokolenie2=[['.' for i in range(20)] for j in range(12)]
obecnepokolenie=[]
przeszlepokolenie=[]
for i in range(100):
    for w in range(len(pokolenie1)):
        for k in range(len(pokolenie1[w])):
            czyzywa=0
            if pokolenie1[w][k]=="X":
                czyzywa=1
            ilezywych=0
            #rogi
            if w==0 and k==0: ilezywych=w0k0(pokolenie1,w,k)
            elif w==0 and k==len(pokolenie1[w])-1: ilezywych=w0kMax(pokolenie1,w,k)
            elif w==len(pokolenie1)-1 and k==0: ilezywych=wMaxk0(pokolenie1,w,k)
            elif w==len(pokolenie1)-1 and k==len(pokolenie1[w])-1: ilezywych=wMaxkMax(pokolenie1,w,k)
            #boki
            elif w==0 and k!=0 and k!=len(pokolenie1[w])-1: ilezywych=w0(pokolenie1,w,k)
            elif w==len(pokolenie1)-1 and k!=0 and k!=len(pokolenie1[w])-1: ilezywych=wMax(pokolenie1,w,k)
            elif k==0 and w!=0 and w!=len(pokolenie1)-1: ilezywych=k0(pokolenie1,w,k)
            elif k==len(pokolenie1[w])-1 and w!=0 and w!=len(pokolenie1)-1: ilezywych=kMax(pokolenie1,w,k)
            #reszta
            else: ilezywych=reszta(pokolenie1,w,k)
            ##################################################
            if czyzywa==1 and (ilezywych==2 or ilezywych==3):
                pokolenie2[w][k]="X"
            elif czyzywa==0 and ilezywych==3:
                pokolenie2[w][k]="X"
            else:
                pokolenie2[w][k]="."
    przeszlepokolenie=pokolenie1
    obecnepokolenie=pokolenie2
    pokolenie1=pokolenie2
    pokolenie2=[['.' for i in range(20)] for j in range(12)]
    ktore=0
    if przeszlepokolenie==pokolenie1:
        ktore=i+2
        #bo zaczynam od 1 czyli +1 i iterator zaczyna się od zera czyli +1
        break
ile=0
for z in range(len(obecnepokolenie)):
    for x in range(len(obecnepokolenie[z])):
        if obecnepokolenie[z][x]=="X":
            ile+=1
print(ktore,ile)
odp.write(str(ktore))
odp.write("\n")
odp.write(str(ile))