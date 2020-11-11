#Zad 1
imie = 'Magda'
moje2imie = 'Magda'
mojedrugie_imie = 'Magda'
#nie mozna zaczynac zmiennych od liczb, nazywac zmienne z myslnikami lub kropkami

#Zad 2
print(2>3) #False bo 2 nie jest wieksze od 3
print('b' < 'c') #True bo znaki kodowane sa standardem Unicode i porownywane sa wartosci Unicode
#print(10>'10') #False bo porownujemy liczbe z kodem unicode stringa
print(bool(33)) #True bo rzutujemy liczbe rozna od zera na typ logiczny
print(bool('False')) #True bo rzutujemy string rozny od zera na typ logiczny
print(bool('')) #False bo pusty string

#Zad3
print(10//3) #dzielenie z ominieciem reszty z ulamka
print(10 ** 3) #podnoszenie do potegi
y = 3; y +=1; print(y) #zwiekszenie zmiennej o 1

#Zad4
e=2
f=2.5
P = 0.5 * e * f
print('Pole rombu o przekatnych ' + str(e) + ' i ' + str(f) + ' wynosi ' + str(P) )

#Zad5
linia1 = 'ATOM 1 C AMFBA 1 39.272 30.272 53.968 1.00 0.00 C'
linia2 = 'ATOM 2 O AMFBA 1 42.771 29.112 54.038 1.00 0.00 O'
x1 = linia1[17:23]
y1 = linia1[24:30]
z1 = linia1[31:37]
x2 = linia2[17:23]
y2 = linia2[24:30]
z2 = linia2[31:37]
dr = ((float(x1)-float(x2))**2 + (float(y1)-float(y2))**2 + (float(z1)-float(z2))**2)**0.5
print('Odleglosc atomu wegla o wspolrzednych ' + str(x1) + ' , ' + str(y1) + ' i ' + str(z1) + ' od atomu tlenu o wspolrzednych ' + str(x2) + ' , ' + str(y2) + ' i ' + str(z2) + ' wynosi ' + str(dr))

#Zad6
#dodawanie
s = 'Semestr'
z = ' Zimowy'
print(s + z)
print(4*'+'+8*'-'+4*'+'+8*'-'+4*'+')
