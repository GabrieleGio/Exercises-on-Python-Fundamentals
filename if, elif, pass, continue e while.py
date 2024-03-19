# Esempio 1
# Leggere da input una stringa, se minore di "lettera", stampare la stringa "minore", se maggiore di "lettera" e minore di "tocco", stampare "intermedia", se maggiore di "tocco" e minore di "what" stampare "maggiore", altrimenti stampare "massima"

a = 10
b = 20
if a > b:
    print(a - b)
else:
    print(b - a)

# potrei avere
if a > b:
    print("maggiore")


# un if "breve" si può mettere sulla stessa riga. "breve" significa che c'è un solo statement dopo if
if a > b:
    print("maggiore")

# Analogamente se ho sia then, sia else con un solo statement
print(a - b) if a > b else print(b - a)


# Infine, se ho più di un if in sequenza allora posso utilizzare elif come parola chiave
if a > b:
    print(a - b)
elif a == b:
    print("Sono uguali")
elif a < b:
    print(b - a)
else:
    print("non so più cosa scrivere")


def EmettiTicket():
    pass


def EliminaTicket():
    pass


def ModificaTicket():
    pass


def ListaTicket():
    pass


def StampaTicket():
    pass


# Esempio classico di uso di elif
print(
    """MENU
      1) emetti ticket
      2) elimina ticket
      3) modifica ticket
      4) lista i ticket emessi
      5) stampa ticket
      0) termine programma
      """
)
cmd = int(input("Inserire scelta: "))
if cmd == 1:
    EmettiTicket()
elif cmd == 2:
    EliminaTicket()
elif cmd == 3:
    ModificaTicket()
elif cmd == 4:
    ListaTicket()
elif cmd == 5:
    StampaTicket()
elif cmd == 0:
    exit(0)
else:
    print("Comando non riconosciuto")

print("AAAA")
if a > b:
    pass

pass

print("BBBB")

while a > 0:
    print(a)
    a = a - 1
    if a == 7:
        continue  # prosegui il ciclo senza eseguire ulteriori operazioni
    else:
        a = a - 2
        break  # stoppa il ciclo

#In questo caso else si può usare come ultimo comando alla fine del ciclo
a = 10
while a > 0:
    print(a)
    a = a - 1
else:
    print("Ho terminato!")