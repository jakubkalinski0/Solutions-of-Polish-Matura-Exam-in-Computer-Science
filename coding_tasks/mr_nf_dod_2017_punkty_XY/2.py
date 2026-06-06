plik=open("punkty.txt","r")
lista=plik.readlines()
odp=open("wyniki4.txt","a")
odp.write(f'{2}\n')
# def czycyfropodobne(liczba1,liczba2):
#     liczba1=list(set(liczba1))
#     liczba1.sort()
#     liczba1="".join(liczba1)
#     liczba2=list(set(liczba2))
#     liczba2.sort()
#     liczba2="".join(liczba2)
#     if liczba1==liczba2:
#         return True
#     else:
#         return False
ile=0
for i in range(len(lista)):
    lista[i]=lista[i].strip()
    lista[i]=lista[i].split()
    # if czycyfropodobne(lista[i][0],lista[i][1]):
    #     ile+=1
    if set(lista[i][0])==set(lista[i][1]):
        ile+=1
print(ile)
odp.write(f'{ile}\n')