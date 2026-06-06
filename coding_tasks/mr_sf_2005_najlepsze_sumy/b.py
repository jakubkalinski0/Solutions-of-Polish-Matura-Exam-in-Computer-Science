odp=open("Raport5.txt","a")
odp.write("b")
odp.write("\n")
plik1=open("dane5-1.txt","r")
lista1=plik1.readlines()
plik2=open("dane5-2.txt","r")
lista2=plik2.readlines()
plik3=open("dane5-3.txt","r")
lista3=plik3.readlines()
dane=[lista1,lista2,lista3]
sumywyniki=[]
elementywyniki=[]
for i in range(len(dane)):
    for j in range(len(dane[i])):
        dane[i][j]=dane[i][j].strip()
        dane[i][j]=int(dane[i][j])
# !!!! ALGORYTM KEDANE'A !!!!
for i in range(len(dane)):
    ciag=dane[i]
    sumaodp=0
    elsumyodp=[]
    sumalok=0
    elsumylok=[]
    for j in range(len(ciag)):
        sumalok+=ciag[j]
        elsumylok.append(ciag[j])
        if sumalok>sumaodp:
            sumaodp=sumalok
            elsumyodp=elsumylok
        if sumalok<=0:
            sumalok=0
            elsumylok=[]
    sumywyniki.append(sumaodp)
    elementywyniki.append(elsumyodp)
print(sumywyniki,elementywyniki)
for i in range(len(sumywyniki)):
    odp.write(str(sumywyniki[i]))
    odp.write(" ")
odp.write("\n")


#działa ale dane5-3 wykonuje się znacząco zbbyt długo(nie kończy się wykonywać)
# wyniki=[]
# for i in range(len(dane)):
#     for j in range(len(dane[i])):
#         dane[i][j]=dane[i][j].strip()
#         dane[i][j]=int(dane[i][j])
# for z in range(len(dane)):
#     ciag=dane[z]
#     suma2=0
#     elsumy2=[]
#     for i in range(len(ciag)):
#         max=i
#         while max<=len(ciag):
#             suma1=0
#             elsumy1=[]
#             for j in range(i,max):
#                 suma1+=ciag[j]
#                 elsumy1.append(ciag[j])
#             if suma1>suma2:
#                 suma2=suma1
#                 elsumy2=elsumy1
#             max+=1
#     wyniki.append(suma2)
# print(wyniki)