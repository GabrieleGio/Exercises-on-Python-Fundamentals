'''
Definire
due variabili (i1, i2) di tipo intero
due variabili (s1, s2) di tipo stringa
due variabili (f1, f2) di tipo float
due variabili (b1, b2) di tipo boolean
stampare
i1+i2
s1+s2
f1+f2
b1+b2
i1+s1
s1+i2
i1+f2
f2+i2
i1+b1
f1+b1
s1+b1
b1+i1
b1+s1
b1+f1
'''
i1=5;
i2=8;
s1="Ciao";
s2="Mondo";
f1=3.14;
f2=2.71;
b1=True;
b2=False;

#5+8 = 13
print(i1+i2);

#"Ciao" + "Mondo" = "CiaoMondo" (per concatenazione di stringhe)
print(s1+s2);

#3.14 + 2.71 = 5.85
print(f1+f2);

#True + False = 1 (perchè sarebbe 1 + 0 dove 1 è True e 0 è False, quindi 1 + 0 = 1)
print(b1+b2);

#5+"Ciao" = Errore (perchè non si possono sommare interi e stringhe)
print(i1+s1);

#"Ciao" + 8
print(s1+i2);

#5 + 2.71
print(i1+f2);

#2.71 + 8
print(f2+i2);

#5+True
print(i1+b1);

#3.14 + True
print(f1+b1);

#Ciao + True
print(s1+b1);

#True + 5
print(b1+i1);

#True + Ciao
print(b1+s1);

#True + 3.14
print(b1+f1);

"""

"""