oceny = {'matematyka': 3, 'fizyka': 2,'jezyk polski': 4}
#klucze to matematyka fizyka i jezyk polski a ich wartosci to 3, 2, 4
#1 dostawanie sie do wartosci pod danym kluczem
print(oceny['fizyka'])#pobieramy wartosc przypisaną o=do klucza fizyka, czyli 2

# Modyfikacja wartosci pod danym kluczem
oceny['jezyk polski'] = 5
print(oceny['jezyk polski'])

from zbiory import zbior
#3 dodawanie klucza do słownika
oceny['geografia'] = 6
print(oceny)

#4 sklejanie słownika z listy kluczy i listy wartosci
klucze = ['bitwa pod grunwaldem', 'chrzest polski', 'III rozbiór polski']
wartosci = [1410, 966, 1795]

#for k, w in zip(klucze, wartosci)
   # print(k, w)
#for i in range(len(klucze)):
   # print(klucze[i], wartosci[i])
    #slownik[klucze[i]] = wartosci[i]


slownik = dict(zip(klucze, wartosci))
print(slownik)

slownik3 = dict(janusz = 21, alejzy = 99, bronislawa = 67)
print(slownik3)

#usuwanie klucza ze słownika

del oceny['fizyka']
print(oceny)

for k in oceny:
    print(k, oceny[k])

for i in oceny.items():
    print(i)


















