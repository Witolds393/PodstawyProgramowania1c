''''#1) listy a napisy

napis = 'informatyka'
lista = []
for l in napis:
    lista.append(l)
lista = list(napis)
print(lista)

#zakres i lista
zakres = range(3, 10, 2)

#3)

lista3 = ['osa', 99, 3.14, [5, 7, 8, 9]]
print(lista3[1:3])#wycinanie fragementu listy
print(lista3[3][2])#obsługa listy zagnieżdżonej
print(lista3[3][::2])#obsługa listy zagnieżdżonej

#4) powielanie listy
#dodawanie list
lista4 = ['a', 45, 78]
lista5 = [[4, 8], 56, 12]
lista6 = lista5 + lista4
print(lista6)

#dodawanie list 2
lista7 = ['a', 45, 78]
lista8 = [[4, 8], 56, 12]
lista7.extend(lista8)
print(lista7)

#"mnożenie" listy przez liczbę
lista9 = [0] * 1000
lista10 = lista9 * 1000
print(lista10)'''

#5)Sortowanie i odwracanie listy
lista11 = [4, -1, 0, 5, 2, 9, 3]
lista11.sort()#.reverse
print(lista11)

#6)wyrażenia listowe
lista = list(range(1, 11))
listakwadraty = [x ** 2 for x in lista]
print(listakwadraty)

#Usuwanie z listy

lista12 =  [4, 7, 8, 4, 2, 1, 3]
while 4 in lista12:
    lista12.remove(4)
print(lista12)

lista13 = [5, 3, 4, 2, 1]
del lista13[2]
print(lista13)