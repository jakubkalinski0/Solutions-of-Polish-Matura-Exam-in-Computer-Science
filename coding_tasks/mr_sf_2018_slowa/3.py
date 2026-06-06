plik=open("slowa.txt","r")
lista=plik.readlines()
odp=open("wyniki6.txt","a")
odp.write("3")
odp.write("\n")
ile=0
def czyanagram(litery1, litery2):
    for i in range(len(litery1)):
        ile1=0
        ile2=0
        for j in range(len(litery1)):
            if litery1[i]==litery1[j]:
                ile1+=1
        for k in range(len(litery2)):
            if litery1[i]==litery2[k]:
                ile2+=1
        if ile1!=ile2:
            return False
    return True
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    if czyanagram(list(lista[i][0]),list(lista[i][1])) and len(lista[i][0])==len(lista[i][1]):
        ile+=1
print(ile)
odp.write(str(ile))
odp.write("\n")