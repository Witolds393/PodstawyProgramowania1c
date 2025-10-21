#symbole logiczne

#koniunkcja
print(2 == 3 and 3 > 1)

#alternatywa
login = 'qwerty'
haslo = ('uiop')
print(login == 'admin' or haslo == 'uiop')

#zaprzeczenie
print(not(login == 'admin' or haslo == 'uiop'))

#Alternatywa wykluczająca
fryzjer = True
murarz = True

print(fryzjer == False ^ murarz == True)

#Priorytety operatorów logicznych
print(2 == 3 and 3 < 1 or 2 < 6)

# Operatory standardowe
print(2+3)
print(2-3)
print(2*3)
print(2/3)

#Potęgowanie
print(36**0.5)
print(125 ** (1/3))

#Dzielenie całkowite (div) - dzielimy i zaokrąglamy zawsze w dół do liczby całkowitej
print(12 // 5)

#reszta z dzielenia liczby a przez liczbe b
print(12 % 5)