#Instrukcje warunkowe if

#Przykład 1
'''liczba = int(input('podaj liczbe od 1do 3'))

if liczba == 1:
    print('jeden')
if liczba == 2:
    print('dwa')
if liczba == 3:
    print('trzy')

#Przykład 2
liczba = int(input('podaj liczbe od 1do 3'))

if liczba == 1:
    print('jeden')
elif liczba == 2:
    print('dwa')
elif liczba == 3:
    print('trzy')'''

#Przykład 3
liczba = int(input('podaj liczbe całkowitą dodatnią'))

if liczba % 2 == 0:
    print('parzysta')
elif liczba % 3 == 0:
    print('Podzielne przez 3')
elif liczba > 0:
    print('Dodatnia')

#Przykład 4

liczba = int(input('podaj liczbe od 1 do 3'))

if liczba == 1:
    print('jeden')
elif liczba == 2:
    print('dwa')
elif liczba == 3:
    print('trzy')
else:
    print('Czytać nie umiesz?')