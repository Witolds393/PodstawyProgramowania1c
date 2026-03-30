#zadanie1.1
lista = [4, 10, 12, 9, 5]
potegi = [(x, x**2, x**3, x**4)for x in lista]
#zdaanie1.2
potegi2 = list(map(lambda x: (x, x ** 2, x ** 3,x ** 4), lista))
#1.3
listad = ['20241101', '20231223', '20220711', '20230503']
listads = list(map(lambda x: {'rok': int(x[:4]), 'miesiac': int(x[4:6]), 'dzien': int(x[:6])}, lista))
#2
class Galeria:
    def __init__(self, kraj,miasto,  lokale_handlowe):
        self.kraj = kraj
        self.miasto = miasto
        self.lokale_handlowe = lokale_handlowe

g1 = Galeria('PL', 'Gdańsk', [(4, 6), (6, 16), (11, 9)])

print(g1.kraj, g1.miasto, g1.lokale_handlowe[1][1])
#zadanie 2.2
plik = open('galerie.txt')
dane = plik.readlines()

for x in dane:
    x = x.split()
    print(x)
    kraj = x[0]
    miasto = x[1]
    lokale_handlowe = [(d, s) for  d, s in zip(x[2::2], x[3::2]) ]
    galerie.append(Galeria(kraj, miasto, lokale_handlowe)
for g in galerie:
    print(g.kraj, g.miasto, g.lokale_handlowe)