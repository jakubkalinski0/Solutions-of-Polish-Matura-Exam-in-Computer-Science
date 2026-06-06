plik=open("dane.txt","r")
lista=plik.readlines()
odp=open("wyniki.txt","a")
odp.write("c")
odp.write("\n")
ile=0
def palindrom(napis):
    for i in range(int(len(napis)/2)+1):
        if napis[i]!=napis[-1-i]:
            return False
    return True
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    if palindrom(lista[i]):
        ile+=1
print(ile)
odp.write(str(ile))