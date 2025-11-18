'''#Jak nie programować wielokrotnie powtarzalnych czynności


a = float(input('podaj pierwszą liczbe'))
b = float(input('podaj drugą liczbe'))
c = float(input('podaj trzecią liczbe'))
d = float(input('podaj czwartą liczbe'))
e = float(input('podaj piątą liczbe'))

suma = (a + b + c + d + e)

print(suma)

liczba = 0
suma = 0

for i in range(5):
    liczba = float(input('Podaj liczbe'))
    suma = suma + liczba

    print(suma)


    #1). Listy
    lista = ['qwerty', 56 , [6, 7], 4.56, [[5,8], 1]]
    print(lista[2][1])
    print(lista[4][0][1])

    #2). listy pętle
    lista2 = ['kot', 'pies', 'owca', 'lama']

    for z in lista2:
        print(z)

    # Pętla for:
    #-> wyciaga dane z listy (jedna po drugiej)
    #-> wykonuje się tyle razy ile elementów ma lista
    for z in lista2:
        print(z)

    #Pętla, która wykona się 3 razy
    lista3 = [1410, 15, 7]

    for i in lista3:
        print('OK')

    lista4 = [0] * 10
    for i in lista4:
        print('Cześć')

    #3. Generatory i pętle
    przedzial = range(1, 10)#{1,2,3,4,5,6,7,8,9}

    for i in przedzial:
        print(i)

    #4. pętla \która wykona się 10 razy
    for i in range(10):
        print(i)'''

lista = [0]

for i in lista:
    print('cześć')
    lista.append(0)

#4. Petle while

liczba = 5

while liczba > 0:
    print(liczba)
    liczba = liczba - 1
