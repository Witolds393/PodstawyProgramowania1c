slowo = 'aksmsncajcnecjebv'
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
slowo2 = ''.join([x for x in list(slowo) if x not in samogloski])
print(slowo2)

#zad2
zagniezdzona = (lista2[5][1:4])
print(zagniezdzona)
#zad 3
lista_liczb = list(map(int, liczby))
print(sum(lista_liczb))
#zad4
#zad5
#b
def liczby_niezalezne(lista):
    wynik = []
    for i in lista:
        dzielniki = []
        for j in lista:
            if i % j == 0:
                dzielniki.append(j)
        if len(dzielniki) == 1:
            wynik.append(i)
    return wynik
print(liczby_niezalezne([12, 7, 3, 6, 21, 74]))