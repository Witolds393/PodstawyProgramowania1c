plik = open('prostokaty.txt')
dane = plik.readlines()


prostokaty = []
for x in dane:
    para = x.split()
    prostokat = (int(para[0]), int(para[1]))
    prostokaty.append(prostokat)
print(prostokaty)


'''prostokaty.sort(key = lambda y: y[0] * y[1])
p_min = prostokaty[0]
p_max = prostokaty[-1]

print(p_min[0] * p_min[1], p_max[0] * p_max[1])'''

obwody = []
for i in prostokaty:
    o = 2*i[0] + 2*i[1]
    obwody.append(o)
rozne = set(obwody)
print(len(rozne))

