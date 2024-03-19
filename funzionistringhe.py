# Problema ho la stringa "123", la voglio trasformare in [1,2,3]
# definire una funzione che risolva il problema
s="123"
def TrasformaStringa(s):
    l=list()
    for i in s:
        l.append(int(i))
    return l
print(TrasformaStringa(s))

#oppure con la comprehension

def TrasformaStringa(s):
    return[int(c) for c in s]
print(TrasformaStringa(s))