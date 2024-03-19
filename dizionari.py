# Leggere da un file (persone.txt) i nomi, cognomi e eta di un gruppo di persone. organizzarli in un dizionario la cui chiave è il cognome e il cui valore è una t-upla contenente i tre valori letti.

# Per prima cosa leggere il file persone.csv e stampare, riga per riga:
# Nome: xxx, Cognome: xxxx, Eta: xxx
# esempio: Nome: Mario, Cognome: Rossi, Eta: 35
prima = [
    "Mario,Rossi,35",
    "Giulio,Bianchi,27",
]
uscita = [
    ["Mario", "Rossi", "35"],
    ["Giulio", "Bianchi", "27"],
]

# Note di progetto
## Il file persone.csv è un file csv. Tante righe e, per ogni riga, i dati separati da virgole
##
# Inizio leggendo il file in una lista dove ogni elemento corriposnde a una riga del file
file = open("persone.csv", "r")
elencoPersone = file.readlines()
file.close()

# Ora elencoPersone è una lista di stringhe dove ogni stringa è una riga del file
print(elencoPersone)

## Mi sono accorto che ogni elemento della lista termina con un carattere "\n", lo voglio togliere.
## Mi ricordo che data una stringa, il metodo/funzione strip() elimina dalla testa e dalla coda della stringa tutti i caratteri bianchi (blank, tab e eoln)
## Quindi costruisco una nuova lista dove i suoi elementi sono stringhe senza \n in fodno

elencoPersoneSenzaEol = []
# per ogni elemento della lista elencoPersone devo togliere \n e appenderlo alla nuova lista
for l in elencoPersone:
    elencoPersoneSenzaEol.append(l.strip())

# Se ora stampo  elencoPersoneSenzaEol, ho una lista di stringhe dove le stringhe non terminano più per \n
print(elencoPersoneSenzaEol)

## Ok, ora ho una lista di stringhe dove ogni stringa contiene nome, cognome ed età separati da ,
## Mi sovviene che in python c'è un comando per le stringhe (split(c)) che decompone una stringa e la trasforma in una lista usando come delimitatore il caratter c passato come parametro alla split()
# QUindi se separo ogni stringa che contiene nome, cognome e età con la split, ottengo una listina che al primo poso ha nome, al secondo ha cognome e la terzo ha eta
# Per verificare se quello che sto dicendo è vero, lo provo

# Provo a splittare una delle stringhe: 'Pier Silvio,Berlu Sconi,45'
# vediamo cosa ne viene fuori
print("Pier Silvio,Berlu Sconi,45".split(","))
# Ottimo, ho ottenuto: ['Pier Silvio', 'Berlu Sconi', '45'], che è proprio quello che voleva il problema
# Ora quest'operazione di split devo farla per tutte le righe del file, cioè per tutti gli elementi della lista elencoPersoneSenzaEol
#
# Come posso operare su tutti gli elementi di una lista? Sempre con il for v in...
for v in elencoPersoneSenzaEol:
    persona = v.split(",")
    print("Nome: ", persona[0], ", Cognome: ", persona[1], ", Eta: ", persona[2])

# Ora costruiamo il dizionario
dizionario = dict()
for v in elencoPersoneSenzaEol:
    persona = v.split(",")
    dizionario[persona[1]] = (persona[0], persona[1], persona[2])

print(dizionario)


# Come posso stampare/gestire singolarmente tutti gli elementi di un dizionario?
# Cosa farebbe un pythonista?
for e in dizionario:
    print("Key: ", e, "Value: ", dizionario[e])