


'''def hurra():
    print('hurra\n' * 50)
hurra()
#hurra2 to nazwa funkcji a n to parametr funkci, a 6 to argument funkcji
#hurra2(6) to wywołanie funkcji dla argumentu 6

def hurra2(n):
    print('hurra\n' * n)

hurra2(6)
#funkcja wersji yeti
def hurra3(n = 10):
    print('hurra\n' * n)

hurra3()


#jezeli funkcja wykonuje po prostu jakąś czynność i nie możemy wykorzystać dalej jej efektów pracy to jest to procedura

#Pole całkowite graniastosłupa prawidłowego trójkątnego
def p_tr(a):
    return a ** 2 * (3 ** 0.5) / 4
pp = p_tr(3 ** 0.25)

print(pp)

def p_prst(a, b):
    return a * 5
psb = p_prst(5, 4)



def p_gran_praw_trn(a, b):
    return 2 * p_tr(a) + 4 * p_prst(a, b)
pg = p_gran_praw_trn(7, 4)
print(pg)
u = [2, 7, 3]
v = [-1, 0, 4]


lista3 = []
#Zadania

#0.3
def suma_v(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        w.append(suma)
    return w
wynik = suma_v(u, v)
print(wynik)

def iloczyn_v(u, v):
    iloczyn2 = 0
    for i in range(len(u)):
        iloczyn = u[i] * v[i]
        iloczyn2 += iloczyn
    return iloczyn2
u = [2, 7, 3]
v = [-1, 0, 4]
wynik = io
print(wynik)'''

#zadanie 2.1
def czy_anagramy(s1, s2):
    '''if sorted(s1) == sorted(s2):
        return True
    else:
        return False'''
    return sorted(s1) == sorted(s2)

#print(czy_anagramy('nosek', 'keson'))

'''s1 = 'nosek'
s2 = 'keson'
print(sorted(s1) == sorted(s2))'''

#2.2
def jaki_trójkąt(a, b, c):
    if a + b + c > 2 + max([a, b, c]) ** 2:
    if a ** 2 + b ** 2 + c ** 2 == 2 * max([a, b, c]) ** 2:
        print('prostokątny')
    if a ** 2 + b ** 2 + c ** 2 > 2 * max([a, b, c]) ** 2:
        print('ostrokątny')
    if a ** 2 + b ** 2 + c ** 2 < 2 * max([a, b, c]) ** 2:
        print('rozwartokątny')

jaki_trójkąt(13, 5, 12)


