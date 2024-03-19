import math
import random


a = 10
b = 20
c = 30

# Se a è pari, stampo b+c
# Se a è dispari, stampo b-c

# Per verificare se a è pari
# if a % 2 == 0:

# Secondo modo, con & (and)
"""
010101 & 
000001 = 
==========
000001

010100 & 
000001 = 
==========
000000
"""
# if a & 1 == 0:


#######
# Terzo modo
# if math.floor(a/2)*2 == a:

# Non efficiente ma solo per
# dimostrarvi in quanti modi si
# può fare un calcolo
"""
while a>0:
    a=a-2
if a == 0: #test di parità
"""

# Supponiamo di aver scelto la tecnica con il modulo
a = 10
b = 20
c = 30

if a % 2 == 0:
    print(b + c)
else:
    print(b - c)

#Come evitare di copiare e copiare sempre lo stesso pezzo di codice? Con le Funzioni
def Arit(a,b,c):
    if a % 2 == 0:
        print(b + c)
    else:
        print(b - c)
#Funzione che genera nome di un colore casuale
def ColoreCasuale ():
    colori = ["rosso" , "verde", "blu", "giallo"] 
    return colori[random.randint(0, len (colori)-1)]

print(ColoreCasuale ())

#Ricordate che un digit è uno tra 0,1,2,3,4,5, 6, 7, 8, 9
#Problema: scrivere una funzione che costruisce una lista
#contenente tutte le possibili combinazioni di quattro digit
def crea_combinazione():
    lista=[]
    for i in range(0,10000):
        s=str(i)
        s=s.zfill(4)
       # while len(s) < 4:
        #    s= "0" + s
        lista.append(s)
    return lista
print(crea_combinazione())

#Modificare la GeneraListaDigit per generare una lista di liste del tipo
#[[0,0,0,0], [0,0,0,1], [0,0,0,2], ..., [9,9,9,8], [9,9,9,9]]