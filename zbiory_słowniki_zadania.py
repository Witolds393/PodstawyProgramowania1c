'''zbior = set() #pusty zbiór
lista2d = [
[5, 2, 8, 5, 1],
[3, 8, 2, 9, 5],
[1, 4, 4, 2, 7],
[6, 3, 9, 1, 4],
[8, 2, 5, 6, 3]]

for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        zbior.add(element)

print(zbior)


zbior_caly = set()
for x in lista2d:
    zbior2 = set(x)
    zbior_caly = zbior_caly.union(zbior2)'''



slowa = [
"LETTER",
"BALLOON",
"SUCCESS",
"HAPPY",
"COFFEE",
"BOOKKEEPER",
"ASSESS",
"MISSISSIPPI",
"ADDRESS",
"TOOLBOX"
]

slowo = 'LETTER'
slowo_zbior = set(slowo)
print(len(slowo_zbior))
#print(f'{i} {len(i_zbior)}')
max_x = ''
max_l_r_l = 0
for i in slowa:
    i_zbior = set(i)
    l_r_l = len(i_zbior)
    if l_r_l > max_l_r_l:
        max_l_r_l = l_r_l
        max_x = i
print(max_x)

#sposob 2
max_slowo = max(slowa, key = lambda x: len(set(x)))
print(max_slowo)

#sposob2.2
zbior = set()
for x in slowa:
     for y in x:
         zbior.add(y)
print(zbior)


for l in zbior:
    lista = []
    for s in slowa:
        if l in s:
            lista.append(s)
    print(f'{l}:{lista}')























