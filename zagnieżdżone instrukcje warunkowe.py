a = float(input('Podaj liczbe rzeczywistą a różną od 0'))
b = float(input('Podaj liczbe rzeczywistą b '))
c = float(input('Podaj liczbe rzeczywistą c'))

if b == 0 and c == 0 :
    print('Równanie = 0')
if b == 0 and c != 0:
   if - c / a > 0:
    x1 = (-c / a) ** 0.5
    x2 = -(-c / a) ** 0.5
    print(f'x1 == {x1} v x2 == {x2}')
   if - c / a < 0:
       print('Nie ma rozwiazań')
if c == 0 and b != 0: