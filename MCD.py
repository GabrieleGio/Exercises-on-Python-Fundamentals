#Ricordando che il MCD tra due numeri e il più grande numero che divide

#i due numeri dati, scrivere un programma che calcola il MCD tra due numeri

#letti da input

#Rcordate!!! dati A e B, se esiste un numero M che li divide, allora lo stesso

#numero dividerà A-B e B oppure B-A e A a seconda che A sia maggiore di #


#Bo che B sia maggiore di A

#Questa definizione, insieme alla considerazione che MCD(A,A)=A,

#ci consente di definire una soluzione che converge,

#garantendo la terminazione dell'algoritmo

# esempio
"""
MCD(38, 24)=

MCD(38-24, 24)=

MCD(14, 24)=

MCD(14, 24-14)=

MCD(14, 10)=

MCD(14-10, 10)=
"""
#Programma
A = int(input("Inserisci il primo numero: "))
B = int(input("Inserisci il secondo numero: "))
MCD = 0

while A != B:
    if A>B:
        A=A-B
    if B>A:
        B=B-A
MCD = A
print(MCD)

#Funziona ma non è ottimizzato per i numeri grandi