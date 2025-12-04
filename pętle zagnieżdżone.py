'''for i in range(1, 1000):
    for j in range(1, 1000):
        print(i * j, end = '\t') #\n = jednym wężykiem, \t w kolumnach. #print(f'{i} * {j} = {i * j}')
    print()

     #Trójkąt prostokątny
    n = int(input('wysokość trójkąta = '))
    for x in range(n):
        for y in range(x + 1):
            print('*', end = '')
        print()'''

'''n = int(input('wysokość trójkata = '))
for x in range(n):
    print('*' * (x + 1))'''

n = int(input('wysokość trójkąta = '))
spacje = n - 1
gwiazdki = 1

for i in range(n):
    print(' ' * spacje, end = '')
    print('*' * gwiazdki)
    spacje = spacje - 1
    gwiazdki = gwiazdki + 2

