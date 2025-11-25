
lista = [10, 56, 89, 59]


#1. chodzenie bezpośrednio po elementach listy
#do zmiennej b trafiają bezpośrednio elementy listy tzn. 10, 56,89,59
'''for b in lista:
    print(b)'''
#1. chodzenie po liście z użyciem indeksów
#2.1 co to jest indeks?
#lista[2]
#2 - indeks
#lista[2] - element znajdujący się pod indesem 2 = 56

#2.2
for k in range(len(lista)): #range(0, 4)
    print(lista[k])


