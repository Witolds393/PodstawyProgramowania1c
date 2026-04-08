'''lista = []
plik =  open('przyklad.txt')
dane = plik.readlines()
for x in range(len(dane)):
    dane[x] = dane[x].strip()
for x in dane:
    if int(x[::-1]) % 17 == 0:
        lista.append(x[::-1])'''
'''lista = []
lista2 = []
plik = open('liczby.txt')
dane = plik.readlines()

for x in range(len(dane)):
    dane[x] = dane[x].strip()
for x in dane:
    x = int(x)
print(f'{len(set(dane))}')
for x in set(dane):
    if dane.count(x) == 2:
        lista.append(x)
for x in set(dane):
    if dane.count(x) == 3:
        lista2.append(x)'''
plik =  open('ruch.txt')
dane = plik.readlines()
print(dane)
for i in range(len(dane)):
    dane[i] = dane[i].split()
    dane[i] = [float(dane[i][0]), float(dane[i][1])]
wynik = []
def t(i):
    return (i - 1) / 100
def v_sr(rk, rp, dt):
    return[(rk[0] - rp[0]) / dt, (rk[1] - rp[1]) / dt]
def szyb_sr(v_sr):
    return(v_sr[0] ** 2 + v_sr[1]**2) ** 0.5

for i in range(1, len(dane)):
    rp = dane[0]
    rk = dane[i]
    czas = t(i + 1)
    pr_sr = v_sr(rk, rp,czas)
    szybk_sr = szyb_sr(pr_sr)
    wynik.append(czas, szybk_sr)
print(wynik)
