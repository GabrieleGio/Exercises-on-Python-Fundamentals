import random
import time
#Conto il tempo che ci vuole per riempire una lista di 10 milioni con numeri casuali tra 1 e 1000
start = time.time_ns()
lista=[]
for v in range (1,10000000):
    lista.append(random.randint(1, 1000000000))
end = time.time_ns()

print(f"Il tempo richiesto è: {(end-start)/1000000000}")

#Ricerca
start = time.time_ns()
trovati = 0
for v in range (1,10000000):
    if random.randint(1, 10) in lista:
        trovati += 1
end = time.time_ns()

print(f"Il tempo richiesto per cercare è: {(end-start)/1000000000} e ne ha trovati {trovati}")

##############################################################################################################à

#Faccio la stessa cosa ma con i SET al posto delle LISTE  (è molto più veloce)

#Riempimento set
start = time.time_ns()
aSet = set()
for v in range (1,10000000):
    aSet.add(random.randint(1, 1000000000))
end = time.time_ns()

print(f"Il tempo richiesto è: {(end-start)/1000000000}")

#Ricerca
start = time.time_ns()
trovati = 0
for v in range (1,10000000):
    if random.randint(1, 10) in aSet:
        trovati += 1
end = time.time_ns()

print(f"Il tempo richiesto per cercare è: {(end-start)/1000000000} e ne ha trovati {trovati}")