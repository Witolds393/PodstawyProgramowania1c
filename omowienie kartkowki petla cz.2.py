'''# zadanie 1 gr.A

n = int(input('Podaj liczbę'))

iloczyn = 1

for x in range(n):
    iloczyn = iloczyn * (x + 1)


print(iloczyn)

# zadanie 2 gr.A

lista = [4, 12, 8, 1, 5, 6, 3]
licznik = 0

for x in range(len(lista)):
    for y in range(len(lista)):
        if lista[x] != lista[y] and (lista[x] + lista[y]) % 3 == 0:           #albo if x != y and (x + y) % 3 == 0: #print(lista[x], lista[y]) #print(x, y)
            licznik += 1
 print(licznik)'''

 # zadanie 3 gr. A

n = int(input('Podaj ile bedzie napisów'))
max_napis = ''
for x in range(n):
    napis = input('Podaj napis')
    ile_a = napis.count('a')
    max_ile_a = max_napis.count('a')
    if ile_a > max_ile_a:
        max_napis = napis
print(max_napis)
