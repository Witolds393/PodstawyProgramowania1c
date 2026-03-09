'''slowo = 'aksmsncajcnecjebv'
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
print(liczby_niezalezne([12, 7, 3, 6, 21, 74]))'''

#2.4, 2.5, 2.6, 2.7, 2.8
def ile_cyfr(liczba):
    licznik = 0
    while liczba > 0:
        liczba += liczba // 10
        licznik += 1
    return licznik


print(ile_cyfr(127))

def unikatowe_elementy(l1, l2):
    zbior = set()
    l = l1 + l2
    for x in l:
        if l.count(x) == 1:
            zbior.add(x)
    return zbior

print(unikatowe_elementy([1, 2, 6, 4, 5], [8, 4, 5, 2]))
