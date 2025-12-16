#Pętle while - przykłady

'''liczba = 120
licznik = 0

while liczba > 0:# tak długo jak warunek się spełnia, pętla się wykonuje
    liczba = liczba // 2
    licznik = licznik + 1


print(licznik)

# zadanie 1

licznik = 0
x = input('Podaj liczbe lub q aby zakonczyc')
while x != 'q':
    liczba = int(x)# zamieniamy na liczbe i jesli to jest q to warunek sie nie spelni i program zakonczy
    if liczba < 2:
        licznik = licznik + 1# zliczanie !
    x = input('Podaj liczbe lub q aby zakonczyc ')

print(licznik)


# zadanie 2
poprawne_haslo = 'informatyka'
haslo = input('podaj haslo')
proba = 0

while haslo != poprawne_haslo:
    print('błedne hasło, Podaj raz jeszcze!')
    haslo = input('Podaj haslo')
    proba = proba + 1
    if proba == 5:
        print('wyczerpano limit prob')
        break
    elif haslo == poprawne_haslo:
        print('Witaj')
from random import randint
from time import sleep
# zadanie 6

wynik1 = 0
wynik2 = 0
wynik3 = 0
akcja = 0

while not ((wynik1 >= 21 or wynik2 >= 21 or wynik3 >= 21) and abs (wynik1 - wynik2 or wynik3 - wynik2 or wynik3 - wynik1 or wynik2 - wynik1 or wynik1 - wynik3) >= 2):
    akcja += 1
    print(f'akcja {akcja}')
   # druzna = int(input('Podaj numer drużyny przeciwnej która wygrała akcje'))
    druzna = randint(1, 3)
    if druzna == 1:
        wynik1 += 1
    elif druzna == 2:
        wynik2 += 1
    else:
        wynik3 += 1
    print(f'wynik {wynik1} : {wynik2} : {wynik3}')
    sleep(0.1)
    if wynik1 > wynik2 and wynik1 > wynik3:
        print('wygrała drużyna 1')
    elif wynik2 > wynik1 and wynik2 > wynik3:
        print('wygrała drużyna 2')
    else:
        print('wygrała drużyna 3')

#  zadanie 7

liczba = int(input('podaj liczbę'))

while liczba > 0:
    cyfra = liczba % 10
    liczba = liczba // 10
    print(cyfra, end = '')'''

# zadanie 8 PODZIĄŁ NA CZYNNIKI PIERWSZE

liczba = int(input('podaj liczbe'))
d = 2
ile_czyn = 0
ile_r_czyn = 0
while liczba > 1:
    if liczba % d == 0:
      ile_r_czyn += 1
    while liczba % d == 0:
        liczba = liczba // d
        ile_czyn += 1
    d += 1
print(ile_czyn)
print(ile_r_czyn)
