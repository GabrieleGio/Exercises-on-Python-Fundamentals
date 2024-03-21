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
# la coppa del mondo e quanti,  
# 10) Conta il numero di persone nella lista worldcup
# 11) conta se ci sono duplicati
   

import json

# Per leggere un file json
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()

#funzione che calcola i calciatori nelle squadre
def conta_calciatori_squadra(elenco, squadre):
    # Inizializziamo un insieme per tenere traccia dei nomi dei calciatori già visti
    giocatori_visti = set()

    # Scansioniamo ogni calciatore nel dataset
    for giocatore in elenco:
        # Estraiamo il nome del calciatore e la nazionalità
        nome_calciatore = giocatore.get('FullName')
        nazionalita = giocatore.get('Team')

        # Controlliamo se il calciatore ha giocato per una delle squadre specificate e se non è già stato conteggiato
        if nazionalita and nazionalita.lower() in [squadra.lower() for squadra in squadre]:
            if nome_calciatore not in giocatori_visti:
                # Aggiungiamo il nome del calciatore all'insieme dei giocatori già visti
                giocatori_visti.add(nome_calciatore)

    # Il numero di calciatori sarà la lunghezza dell'insieme
    numero_calciatori = len(giocatori_visti)

    return numero_calciatori




# 1) Contare quanti calciatori hanno giocato per l'Italia escludere i duplicati
# Inizializziamo un insieme per tenere traccia dei nomi dei calciatori italiani già visti
# Inizializziamo un insieme contenente entrambe le rappresentazioni della nazionalità italiana
italianita = {"Italy", "ITA"}

# Inizializziamo un insieme per tenere traccia dei nomi dei calciatori italiani già visti
giocatori_italiani_visti = set()

# Scansioniamo ogni calciatore nel dataset
for giocatore in worldcup:
    # Estraiamo il nome del calciatore e la nazionalità
    nome_calciatore = giocatore.get('FullName')
    nazionalita = giocatore.get('Team')

    # Controlliamo se il calciatore ha giocato per l'Italia e se non è già stato conteggiato
    if nazionalita in italianita:
        if nome_calciatore not in giocatori_italiani_visti:
            # Aggiungiamo il nome del calciatore all'insieme dei giocatori italiani già visti
            giocatori_italiani_visti.add(nome_calciatore)
 
# Il numero di calciatori italiani sarà la lunghezza dell'insieme
numero_calciatori_italiani = len(giocatori_italiani_visti)

# Stampiamo il risultato
print("Il numero di calciatori che hanno giocato per l'Italia è:", numero_calciatori_italiani)



# Stampiamo ogni nome su una nuova riga
#for nome in giocatori_italiani_visti:
   # print(nome)

# 2) Contare quanti calciatori hanno giocato per il Brasile
brasilianità = {"Brazil", "ITA"}

# Inizializziamo un insieme per tenere traccia dei nomi dei calciatori italiani già visti
giocatori_brasiliani_visti = set()

# Scansioniamo ogni calciatore nel dataset
for giocatore in worldcup:
    # Estraiamo il nome del calciatore e la nazionalità
    nome_calciatore = giocatore.get('FullName')
    nazionalita = giocatore.get('Team')

    # Controlliamo se il calciatore ha giocato per il brasile e se non è già stato conteggiato
    if nazionalita in brasilianità:
        if nome_calciatore not in giocatori_brasiliani_visti:
            # Aggiungiamo il nome del calciatore all'insieme dei giocatori italiani già visti
            giocatori_brasiliani_visti.add(nome_calciatore)

# Il numero di calciatori italiani sarà la lunghezza dell'insieme
numero_calciatori_brasiliani = len(giocatori_brasiliani_visti)

# Stampiamo il risultato
print("Il numero di calciatori che hanno giocato per il brasile è:", numero_calciatori_brasiliani)

# 3) Contare quanti calciatori hanno giocato per l'Argentina
# Utilizzo della funzione per contare i calciatori argentini che fanno parte della squadra Argentina o ARG

# Lista delle squadre da confrontare
squadre_argentine = ['Argentina', 'ARG',]

# Utilizzo della funzione per contare i calciatori argentini
numero_calciatori_argentini = conta_calciatori_squadra(worldcup, squadre_argentine)

# Stampiamo il risultato
print("Il numero di calciatori che hanno giocato per l'Argentina è:", numero_calciatori_argentini)

# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# funzione che trova icalciatori per squadra e li compapara per vedere se hanno mai giocato nella stessa squadra
def trova_calciatori_comuni_br_it(elenco):
    # Inizializziamo due set per tenere traccia dei calciatori del Brasile e dell'Italia
    calciatori_brasile = set()
    calciatori_italia = set()

    # Scansioniamo ogni calciatore nel dataset
    for giocatore in elenco:
        # Estraiamo il nome del calciatore e la nazionalità
        nome_calciatore = giocatore.get('FullName')
        nazionalita = giocatore.get('Team')

        # Controlliamo se il calciatore ha giocato per il Brasile (BRA) o per l'Italia (ITA)
        if nazionalita:
            if 'BRA' in nazionalita.upper() or 'Brazil' in nazionalita.upper():
                calciatori_brasile.add(nome_calciatore)
            elif 'ITA' in nazionalita.upper() or 'Italy' in nazionalita.upper():
                calciatori_italia.add(nome_calciatore)

    # Troviamo l'intersezione dei due insiemi per trovare i calciatori comuni
    calciatori_comuni = calciatori_brasile.intersection(calciatori_italia)

    return calciatori_comuni

# Utilizzo della funzione
calciatori_comuni = trova_calciatori_comuni_br_it(worldcup)
for calciatore in calciatori_comuni:
 print("I calciatori che hanno giocato sia per il Brasile che per l'Italia sono:", calciatore if calciatore else 'nessun calciatore trovato')


# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia

def trova_calciatori_comuni_arg_it(elenco):
    # Inizializziamo due set per tenere traccia dei calciatori del argentina e dell'Italia
    calciatori_argentina= set()
    calciatori_italia = set()

    # Scansioniamo ogni calciatore nel dataset
    for giocatore in elenco:
        # Estraiamo il nome del calciatore e la nazionalità
        nome_calciatore = giocatore.get('FullName')
        nazionalita = giocatore.get('Team')

        # Controlliamo se il calciatore ha giocato per il argentina o per l'Italia (ITA)
        if nazionalita:
            if 'ARG' in nazionalita.upper() or 'Argentina' in nazionalita.upper():
                calciatori_argentina.add(nome_calciatore)
            elif 'ITA' in nazionalita.upper() or 'Italy' in nazionalita.upper():
                calciatori_italia.add(nome_calciatore)

    # Troviamo l'intersezione dei due insiemi per trovare i calciatori comuni
    calciatori_comuni = calciatori_argentina.intersection(calciatori_italia)

    return calciatori_comuni

# Utilizzo della funzione
calciatori_comuni = trova_calciatori_comuni_arg_it(worldcup)

for calciatore in calciatori_comuni:
    print("I calciatori che hanno giocato sia per il argentina che per l'Italia sono:", calciatore if calciatore else"Nome non disponibile")


# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla Coppa del Mondo
# Inizializziamo le variabili per tenere traccia del calciatore più giovane e della sua età
  # Inizializziamo le variabili per tenere traccia del calciatore più giovane e della sua età
calciatore_piu_giovane = None
eta_piu_giovane = 10000 # Inizializziamo con un valore molto grande

# Iteriamo su ogni giocatore nel dataset
for giocatore in worldcup:
    # Estraiamo l'anno di nascita e l'anno in cui ha iniziato a giocare
    data_nascita = giocatore.get('DateOfBirth', '')
    if data_nascita:
        anno_nascita = int(data_nascita.split('-')[0])
        anno_inizio_giocare = giocatore['Year']

        # Calcoliamo l'età in cui ha iniziato a giocare
        eta = anno_inizio_giocare - anno_nascita

        # Se l'età calcolata è minore dell'età più giovane finora, aggiorniamo il calciatore più giovane
        if eta < eta_piu_giovane:
            eta_piu_giovane = eta
            calciatore_piu_giovane = giocatore['FullName']

# Stampiamo il risultato
print("Il calciatore più giovane è:", calciatore_piu_giovane)
print("Età in cui ha iniziato a giocare:", eta_piu_giovane, "anni")

# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla Coppa del Mondo
calciatore_piu_anziano = None
eta_piu_anziano = 0

# Iteriamo su ogni giocatore nel dataset
for giocatore in worldcup:
    # Estraiamo l'anno di nascita e l'anno in cui ha iniziato a giocare
    data_nascita = giocatore.get('DateOfBirth')
    if data_nascita:
        anno_nascita = int(data_nascita.split('-')[0])
        anno_inizio_giocare = giocatore['Year']

        # Calcoliamo l'età in cui ha iniziato a giocare
        eta = anno_inizio_giocare - anno_nascita

        # Se l'età calcolata è maggiore dell'età più anziana finora e il nome del giocatore non è vuoto, aggiorniamo il calciatore più anziano
        if eta > eta_piu_anziano and giocatore.get('FullName'):
            eta_piu_anziano = eta
            calciatore_piu_anziano = giocatore['FullName']

# Stampiamo il risultato
print("Il calciatore più anziano è:", calciatore_piu_anziano)
print("Età in cui ha iniziato a giocare:", eta_piu_anziano, "anni")


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
# Inizializziamo un dizionario per tenere traccia del numero di calciatori per squadra
calciatori_per_squadra = {}

# Inizializziamo un set per tenere traccia dei nomi dei calciatori già visti
giocatori_gia_visti = set()

# Scansioniamo ogni calciatore nel dataset
for giocatore in worldcup:
    # Estraiamo il nome del calciatore
    nome_calciatore = giocatore.get('FullName')
    
    # Controlliamo se il nome del calciatore è già stato visto
    if nome_calciatore not in giocatori_gia_visti:
        # Aggiungiamo il nome del calciatore al set dei giocatori già visti
        giocatori_gia_visti.add(nome_calciatore)
        
        # Estraiamo il nome della squadra del calciatore
        squadra = giocatore['Team']
        
        # Aggiorniamo il conteggio dei calciatori per la squadra corrente
        calciatori_per_squadra[squadra] = calciatori_per_squadra.get(squadra, 0) + 1

# Troviamo la squadra che ha fornito più calciatori
squadra_max_calciatori = max(calciatori_per_squadra, key=calciatori_per_squadra.get)
numero_calciatori_squadra_max = calciatori_per_squadra[squadra_max_calciatori]

# Stampiamo il risultato
print("La squadra che ha fornito più calciatori per la Coppa del Mondo è:", squadra_max_calciatori)
print("Numero di calciatori forniti:", numero_calciatori_squadra_max)


# 10) Conta il numero di persone nella lista worldcup
numero_calciatori = len(worldcup)
print("Numero totale di calciatori nella lista:", numero_calciatori)


# 11) conta se ci sono duplicati
# Dizionario per tenere traccia del numero di volte che ogni nome compare nel dataset
# Dizionario per tenere traccia del numero di volte che ogni nome completo compare nel dataset
duplicati_per_nome = {}

# Scansioniamo ogni calciatore nel dataset
for giocatore in worldcup:
    # Estraiamo il nome completo del calciatore
    nome_completo = giocatore.get('FullName')
    
    # Controlliamo se il nome completo del calciatore è disponibile
    if nome_completo:
        # Aggiorniamo il conteggio dei duplicati per il nome completo corrente
        duplicati_per_nome[nome_completo] = duplicati_per_nome.get(nome_completo, 0) + 1

# Contiamo il numero totale di duplicati
numero_duplicati = sum(count - 1 for count in duplicati_per_nome.values() if count > 1)

# Se ci sono duplicati, stampiamo il numero totale di duplicati
if numero_duplicati > 0:
    print("Sono presenti", numero_duplicati, "persone duplicate nel dataset.")
else:
    print("Ogni persona è riportata solo una volta nel dataset.")