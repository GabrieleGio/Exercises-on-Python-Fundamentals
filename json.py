import json

#Per leggere un file json 
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()

print(len(worldcup))

print(worldcup[1200])
print(worldcup[1200]['DateOfBirth'])

# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!!
# 1) contare quanti calciatori hanno giocato per l'Italia
# 2) contare quanti calciatori hanno giocato per il Brasile
# 3) contare quanti calciatori hanno giocato per l'Argentina
# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per
# la coppa del mondo e quanti, quale squadra francese, ...

# 10) Conta il numero di persone nella lista worldcup

import json

#Per leggere un file json 
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()

# 1) Contare quanti calciatori hanno giocato per l'Italia
# Inizializziamo il contatore dei calciatori italiani
conteggio_italiani = 0

# Scansioniamo ogni calciatore nel dataset
for giocatore in worldcup:
    # Controlliamo se il calciatore ha giocato per l'Italia
    if giocatore.get('Team') == 'Italy':
        # Incrementiamo il contatore dei calciatori italiani
        conteggio_italiani += 1

# Stampiamo il risultato
print("Il numero di calciatori che hanno giocato per l'Italia è:", conteggio_italiani)


# 2) Contare quanti calciatori hanno giocato per il Brasile
# Inizializziamo il contatore dei calciatori brasiliani
conteggio_brasiliani = 0

# Scansioniamo ogni calciatore nel dataset
for giocatore in worldcup:
    # Controlliamo se il calciatore ha giocato per il Brasile
    if giocatore.get('Team') == 'Brazil':
        # Incrementiamo il contatore dei calciatori brasiliani
        conteggio_brasiliani += 1

# Stampiamo il risultato
print("Il numero di calciatori che hanno giocato per il Brasile è:", conteggio_brasiliani)

# 3) Contare quanti calciatori hanno giocato per l'Argentina
# Inizializziamo il contatore dei calciatori argentini
conteggio_argentini = 0

# Scansioniamo ogni calciatore nel dataset
for giocatore in worldcup:
    # Controlliamo se il calciatore ha giocato per l'Argentina
    if giocatore.get('Team') == 'Argentina':
        # Incrementiamo il contatore dei calciatori argentini
        conteggio_argentini += 1

# Stampiamo il risultato
print("Il numero di calciatori che hanno giocato per l'Argentina è:", conteggio_argentini)


# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
calciatori_brasile_italia = []

for giocatore in worldcup:
    if giocatore['Team'] == 'Brazil' and giocatore['Team'] == 'Italy':
        calciatori_brasile_italia.append(giocatore['FullName'])

if calciatori_brasile_italia:
    print("Calciatori che hanno giocato sia per il Brasile che per l'Italia:")
    for calciatore in calciatori_brasile_italia:
        print(calciatore)
else:
    print("Nessun calciatore trovato che ha giocato sia per il Brasile che per l'Italia.")


# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
calciatori_argentina_italia = []

for giocatore in worldcup:
    if giocatore['Team'] == 'Argentina' and giocatore['Team'] == 'Italy':
        calciatori_argentina_italia.append(giocatore['FullName'])

if calciatori_argentina_italia:
    print("Calciatori che hanno giocato sia per l'Argentina che per l'Italia:")
    for calciatore in calciatori_argentina_italia:
        print(calciatore)
else:
    print("Nessun calciatore trovato che ha giocato sia per l'Argentina che per l'Italia.")


# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla Coppa del Mondo
calciatore_piu_giovane = None
eta_piu_giovane = float('inf')

for giocatore in worldcup:
    data_di_nascita = giocatore.get('DateOfBirth')
    if data_di_nascita:
        anno_di_nascita = int(data_di_nascita.split('-')[0])
        eta = 2024 - anno_di_nascita
        
        if eta < eta_piu_giovane:
            eta_piu_giovane = eta
            calciatore_piu_giovane = giocatore['FullName']

print("Il calciatore più giovane è:", calciatore_piu_giovane if calciatore_piu_giovane else "Nome non disponibile")
print("Età:", eta_piu_giovane)

# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla Coppa del Mondo
calciatore_piu_anziano = None
eta_piu_anziana = 0

for giocatore in worldcup:
    data_di_nascita = giocatore.get('DateOfBirth')
    if data_di_nascita:
        anno_di_nascita = int(data_di_nascita.split('-')[0])
        eta = 2024 - anno_di_nascita
        
        if eta > eta_piu_anziana:
            eta_piu_anziana = eta
            calciatore_piu_anziano = giocatore['FullName']

print("Il calciatore più anziano è:", calciatore_piu_anziano if calciatore_piu_anziano else "Nome non disponibile")
print("Età:", eta_piu_anziana)

# 8) Trovare quale calciatore ha partecipato a più edizioni della Coppa del Mondo
# Inizializziamo un dizionario per tenere traccia del numero di partecipazioni per ciascun calciatore
partecipazioni_per_calciatore = {}

# Scansioniamo ogni calciatore nel dataset
for giocatore in worldcup:
    # Estraiamo il nome del calciatore
    nome_calciatore = giocatore.get('FullName')
    
    # Controlliamo se il nome del calciatore è disponibile
    if nome_calciatore:
        # Aggiorniamo il conteggio delle partecipazioni per il calciatore corrente
        partecipazioni_per_calciatore[nome_calciatore] = partecipazioni_per_calciatore.get(nome_calciatore, 0) + 1

# Troviamo il calciatore con il maggior numero di partecipazioni
calciatore_max_partecipazioni = max(partecipazioni_per_calciatore, key=partecipazioni_per_calciatore.get)
numero_max_partecipazioni = partecipazioni_per_calciatore[calciatore_max_partecipazioni]

# Stampiamo il risultato
print("Il calciatore che ha partecipato al maggior numero di edizioni della Coppa del Mondo è:", calciatore_max_partecipazioni)
print("Numero di edizioni in cui ha partecipato:", numero_max_partecipazioni)
print("Numero totale di persone lette:", len(worldcup))


# 9) Trovare quale squadra di calcio ha fornito più calciatori per la Coppa del Mondo
# Inizializziamo un dizionario per tenere traccia del numero di calciatori per squadra
calciatori_per_squadra = {}

# Scansioniamo ogni calciatore nel dataset
for giocatore in worldcup:
    # Estraiamo il nome della squadra del calciatore
    squadra = giocatore['Team']
    
    # Aggiorniamo il conteggio dei calciatori per la squadra corrente
    if squadra in calciatori_per_squadra:
        calciatori_per_squadra[squadra] += 1
    else:
        calciatori_per_squadra[squadra] = 1

# Troviamo la squadra che ha fornito più calciatori
squadra_max_calciatori = max(calciatori_per_squadra, key=calciatori_per_squadra.get)
numero_calciatori_squadra_max = calciatori_per_squadra[squadra_max_calciatori]

# Stampiamo il risultato
print("La squadra che ha fornito più calciatori per la Coppa del Mondo è:", squadra_max_calciatori)
print("Numero di calciatori forniti:", numero_calciatori_squadra_max)



# 10) Conta il numero di persone nella lista worldcup
numero_calciatori = len(worldcup)
print("Numero totale di calciatori nella lista:", numero_calciatori)