import random
##Tabellina del 23
for v in range(1,10):
    print(23*v)

#sapendo che la funzione random.randint(start,end)
#genera un numero casuale compreso tra start e end, end compreso,
#costruire una lista di numeri casuali lunga 100 e stampare la somma di tutti i suoi numeri
num=[]
for n in range (100):
    num.append(random.randint(1,10))
    print("La mia lista è:",num)
print("la somma dei miei numeri è: ",sum(num))  

#Costruire due liste, la prima che contiene i numeri pari fino a 1000
#la seconda che contiene i numeri dispari fino a 1000
#a partire dalle prime due liste,
#costruire una terza lista che contiene prima tutti i pari e poi tutti i dispari
pari = [p for p in range(1,1001) if p % 2 == 0]
print(pari)

dispari = [p for p in range(1,1001) if p % 2 != 0]
print(dispari)

tutti = []
tutti.extend(pari)
tutti.extend(dispari)
print(tutti)