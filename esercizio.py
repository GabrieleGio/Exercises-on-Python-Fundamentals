var = 10
nome=0
numero="Altro"

ottimo=[1,2,3,4,5]
esempio=("uno", nome, var)

diz={"nome": var, "Cognome": numero, "ottimo": ottimo}

doz= [diz, 1,2,3]

for i in range (7,700,7):
    print(i)

for i in range(9,9999,2):
    print(ottimo[i % len(ottimo)])

infine = [x for x in ottimo]
infine1 = [y*y for x in ottimo for y in range(y, 10 * y, 1)]