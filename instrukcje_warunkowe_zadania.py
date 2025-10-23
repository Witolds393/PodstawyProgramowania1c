#Rozwiązanie zadania kwadratowego

'''a = float(input('Podaj liczbe a =/= 0'))
b = float(input('Podaj liczbe b'))
c = float(input('Podaj liczbe c'))

delta = b ** 2-4 * a * c

if delta > 0:
    x1 = (-b - delta ** 0.5) / (2 * a)
    x2 = (-b + delta ** 0.5) / (2 * a)
    print(f'x1 = {x1} v x2 = {x2}')
elif delta == 0:
    x = (-b) / (2 * a)
    print('x1 = x2 = {}'. format(x))
else:
    print('brak rozwiązań')'''

#zadanie 12
pisemny_i_polski = int(input('pisemny polski'))
pisemny_i_obcy = int(input('pisemny obcy'))
pisemny_i_dodatkowy = int(input('pisemny dodatkowy'))
ustny_i_polski = int(input('ustny polski'))
ustny_i_obcy = int(input('ustny obcy'))

if pisemny_i_polski >= 30 and pisemny_i_obcy >=30 and pisemny_i_dodatkowy >=30 and ustny_i_polski >= 30 /
    and ustny_i_obcy >= 30:
    print('zdałeś bez amnestii')
elif (pisemny_i_polski + pisemny_i_obcy + pisemny_i_dodatkowy + ustny_i_polski + ustny_i_obcy) / 5 >= 30:
    print('zdałeś z amnestią')
else:
    print('nie zdałeś')