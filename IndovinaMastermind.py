import copy
import random


# Genera una lista che contiene M numeri casuali tra 1 e N
def GeneraLista(N, M):
    lista = []
    for i in range(M):
        v = random.randint(1, N)
        lista.append(v)
    return lista


def ContaUgualiInStessoEInAltro(ls, lsCheck):
    ls = ls.copy()
    lsCheck = lsCheck.copy()
    # Conteggio e elimino gli elementi nello stesso posto
    stessoPosto = 0
    for i in range(len(lsCheck)):
        if lsCheck[i] == ls[i]:
            stessoPosto += 1
            ls[i] = None
            lsCheck[i] = None

    # Conteggio e elimino gli elementi in posto differente
    altroPosto = 0
    for v in lsCheck:
        if v != None and v in ls:
            altroPosto += 1
            ls.remove(v)
    return stessoPosto, altroPosto


def ConvertiStringaDigitInListaNumeri(sd):
    return [int(x) for x in list(sd)]


def base_repr(x: int, base: int, length: int):
    from numpy import base_repr
    from math import log, ceil

    l = 0
    if x != 0:
        l = ceil(log(x, base))
    s = base_repr(x, base, length - l)
    while len(s) > length:
        s = s[1:]
    return s


N = int(input("Inserire il numero di simboli: "))
M = int(input("Inserire la lunghezza della lista: "))

# per semplificarmi la vita, genero tutte le possibili
# combinazioni con ripetizione di N digit in M posizioni
# devo contare in base N per N^M volte e considero che lo 0 non esista, quindi da 1 a N
# In questo modo non mostro la strategia al giocatore master
tuttiICasi = [[1 + int(i) for i in list(base_repr(x, N, M))] for x in range(N**M)]
random.shuffle(tuttiICasi)
#
# Quale proposta è la prossima?
casoCorrente = 0
#
# lista dei tentativi
# è una lista che contiene (tentativo, strike, ball)
tentativi = []

while len(tentativi) == 0 or tentativi[-1][1] != M:
    # Genera il prossimo tentativo
    prossima = tuttiICasi[casoCorrente]
    casoCorrente += 1  # vado al prossimo!
    #
    # Devo verificare che sia coerente con le risposte precedenti
    coerente = True
    for prec in tentativi:
        strike, ball = ContaUgualiInStessoEInAltro(prossima, prec[0])
        if strike != prec[1] or ball != prec[2]:
            coerente = False
            break
    if coerente:
        # faccio la proposta
        print("Proposta:", prossima)
        strike = int(input("Strike? "))
        ball = int(input("Ball? "))
        if strike == M:
            print("Ho vinto, fine")
            exit(0)
        tentativi.append((prossima, strike, ball))