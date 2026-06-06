plik=open("NAPIS.TXT","r")
lista=plik.readlines()
odp=open("ZADANIE5.txt","a")
odp.write("b")
odp.write("\n")
for i in range(len(lista)):
     lista[i]=lista[i].strip()
     czy=1
     for j in range(len(lista[i])-1):
         if ord(lista[i][j])>=ord(lista[i][j+1]):
             czy=0
             break
     if czy==1:
         print(lista[i])
         odp.write(lista[i])
         odp.write("\n")