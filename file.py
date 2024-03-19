fin = open("alice.txt", "r")
linee = fin.readlines()
fin.close()

#readlines legge tutte le righe incluso il carattere a capo (eol/eoln)
#come faccio a togliere questi fine riga?
l1 = []
for l in linee:
    l1.append(l.strip())
linee = l1
print(linee)


s="alfa;beta;gamma"
# Come posso ottenere la lista ["alfa, "beta", "gamma"]?
print(s.split(";"))

#Dato alice.txt, stampare, una per riga, tutte le parole che la compongono
parole=[]
for l in linee:
    parole.extend(l.split(" "))
print(parole)

def Maiuscola(c):
    return c.isupper()

s="Nel mezzo del cammin di nostra vita"
print(list(filter(Maiuscola,s)))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def Pari(n):
    return n % 2 == 0

print(list(filter(Pari, lista)))

#Data una lista di stringhe, eliminare dalla lista tutte le stringe vuote
ls = ["uno","", "due", "tre", "","","","","","fine"]
lnuova = []
for i in ls:
    if len(i)>0:
        lnuova.append(i)
print(lnuova)

#Contare quanti caratteri ci sono in alice.txt
#Contare quanti caratteri non spazi bianchi ci sono in alice.txt
#Contare quanti caratteri alfanumerici[a-zA-Z0-9] ci sono in alice.txt
fin = open("alice.txt", "r")
testo = fin.read()
numero_caratteri = len(testo)
print("Caratteri totali: ",numero_caratteri)
cnpb=0
alfanum=0
for z in testo:
    if z !=" ":
        cnpb+=1
print("Caratteri senza spazi bianchi: ",cnpb)
for k in testo:
    if k.isalnum():
        alfanum += 1
print("Caratteri alfanumerici: ",alfanum)
fin.close()