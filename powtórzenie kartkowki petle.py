lista = [12, 45, 78, 101, 9, -5, 9, 7, 23, 70]


#zadanie 2. grupa B

#sposób 1
for i in range(len(lista)):
    if i % 2 == 1:
        print(lista[i])

#sposób 2
for i in range(1, len(lista), 2):
    print(lista[i])

#sposób3
for i in lista[1::2]: #[45, 101, -5, 7]
    print(i)
#sposób4
i = 1
while i < len(lista):
    print(lista[i])
    i = i + 2




lista3 = [100]

for x in lista3:
    print('xd')
    lista3.append(100000000)
