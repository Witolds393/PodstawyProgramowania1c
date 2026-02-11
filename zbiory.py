zbior = {5, 6, 6, 1, 1, 5, 9}
print(zbior)

zbior2 = {'kot', 'pies', 'głab'}
print(len(zbior2))

A = set(range(0, 20, 2))
B = {1, 2, 3, 4, 6, 12}
#suma zbiorów
sumaAB = A.union(B)
print(sumaAB)


print(A)
sumaAB2 = set(list(A) + list(B))
print(sumaAB2)
#części wspólne
iloczynAB = A.intersection(B)
print(iloczynAB)

#różnica
roznicaAB = A.difference(B)
print(roznicaAB)

#dodawanie elemntu do zbioru
C = {1, 7, 4, 5}
C.add(2)
print(C)