#Comprehension
lista = [1,2,3,4,5]

lista2 = [x*x for x in lista]
print (lista2)

#Nel modo classico
lista2=[]
for x in lista:
    lista2.append(x*x)

lista = [2,3,4]
lista3 = [y for x in lista for y in range(1,x)]
print(lista3)