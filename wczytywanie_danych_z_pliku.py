'''plik = open('plik')
dane = plik.read()
print(dane)'''

'''dane = open('plik2')
plik2 = dane.readlines()
print(plik2)

for i in range(len(plik2)):
    plik2[i] = int(plik2[i])
print(plik2)'''

'''dane3 = open('plik3')
plik3 = dane3.readlines()

for i in range(len(plik3)):
    plik3[i] = plik3[i].strip()

print(plik3)'''

'''dane4 = open('plik4')
plik4 = dane4.readlines()

for i in range(len(plik4)):
    plik4[i] = plik4[i].split()

    print(plik4)'''
dane5 = open('plik5')
plik5 = dane5.readlines()

for i in range(len(plik5)):
     plik5[i] = plik5[i].split()
     for j in range(len(plik5[i])):
         plik5[i][j] = int(plik5[i][j])
print(plik5)


plik5prin = [list(map(int, x.split()))for x in open('plik5')]