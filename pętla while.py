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

print(licznik)'''


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


