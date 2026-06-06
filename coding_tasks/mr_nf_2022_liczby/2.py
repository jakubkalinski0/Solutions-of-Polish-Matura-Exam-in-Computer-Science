plik=open("liczby.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write("2")
odp.write("\n")
def pierwsze(liczba):
    czynniki=[]
    czynnik=2
    while liczba>1:
        if liczba%czynnik==0:
            liczba=liczba//czynnik
            czynniki.append(czynnik)
        else:
            czynnik+=1
    return czynniki
czynniki2=""
czynniki3=""
liczba2=0
liczba3=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    liczba1=int(lista[i])
    if len(pierwsze(liczba1))>len(czynniki2):
        czynniki2=pierwsze(liczba1)
        liczba2=liczba1
    if len(set(pierwsze(liczba1)))>len(set(czynniki3)):
        czynniki3=pierwsze(liczba1)
        liczba3=liczba1
print(liczba2,len(czynniki2),liczba3,len(czynniki3))
odp.write(str(liczba2))
odp.write(" ")
odp.write(str(len(czynniki2)))
odp.write(" ")
odp.write(str(liczba3))
odp.write(" ")
odp.write(str(len(czynniki3)))
odp.write("\n")


#ROZWIAZANIE NR 2 (nie dziala choc powinno)
# czynniki2=0
# czynniki3=0
# liczba2=0
# liczba3=0
# def pierwsze(liczba):
#     czynniki=""
#     czynnik=2
#     while liczba>1:
#         if liczba%czynnik==0:
#             liczba=liczba//czynnik
#             czynniki+=str(czynnik)
#         else:
#             czynnik+=1
#     return czynniki
# for i in range(len(lista)):
#     lista[i]=lista[i].strip()
#     if len(pierwsze(int(lista[i])))>czynniki2:
#         czynniki2=len(pierwsze(int(lista[i])))
#         liczba2=int(lista[i])
#     if len(set(pierwsze(int(lista[i]))))>czynniki3:
#         czynniki3=len(set(pierwsze(int(lista[i]))))
#         liczba3=int(lista[i])
# print(liczba2,czynniki2,liczba3,czynniki3)
#z jakiejś przyczyny 2 rozwiązanie nie zwraca dobrych wyników dla
#pliku "liczby" a dla "przykład" już rak = nie działa choć powinno