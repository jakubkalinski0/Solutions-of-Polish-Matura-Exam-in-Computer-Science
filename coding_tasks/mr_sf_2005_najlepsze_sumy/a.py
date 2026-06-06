odp=open("Raport5.txt","w")
odp.write("a")
odp.write("\n")
ciag=[1,-2,6,-5,7,-3]
elsumy2=[]
suma2=0
for i in range(len(ciag)):
    max=i
    while max<=len(ciag):
        suma1=0
        elsumy1=[]
        for j in range(i,max):
            suma1+=ciag[j]
            elsumy1.append(ciag[j])
        if suma1>suma2:
            suma2=suma1
            elsumy2=elsumy1
        max+=1
print(elsumy2,suma2)
odp.write(str(suma2))
odp.write("\n")