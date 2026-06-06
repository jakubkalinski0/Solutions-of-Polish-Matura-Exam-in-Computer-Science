plik=open("slowa.txt","r")
lista=plik.readlines()
odp=open("rodziny.txt","w")
odp.write("ZAD 4.3\n")
for i in range(len(lista)):
    lista[i]=lista[i].strip()
rodziny=[[] for i in range(200)]
for i in range(len(lista)):
    if lista[i]==lista[i][::-1]:
        rodziny[len(lista[i])].append(lista[i])
posortowane=[]
odp.write(f'Palindromy kazdej rodziny w kolejnosci alfabetycznej: \n')
for rodzina in rodziny:
    if len(rodzina)>0:
        rodzina=sorted(rodzina)
        for element in rodzina:
            odp.write(f'{element},')