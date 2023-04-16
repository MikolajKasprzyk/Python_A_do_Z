# -*- coding: utf-8 -*-

i = 0

while i < 5:
    print(i)
    i += 1
    
# %%
n=0
while True:
    print(n)
    if n >= 10:
        break
    n += 1
    
# %%
while True:
    name = input('Podaj swoje imie: ')
    if len(name) >=3 and name.isalpha(): # sprawdzamy czy imie na 3 lub wicej znakow i czy sa to litery 
        break # jesli oba warunki sa spelnione petla sie przerywa i idziemy dalej
print('czesc {}'.format(name))
    
# %%
n = 0
while n < 20:
    n += 1 # ikrementacja na poczatku - przed continue - bo jesli bylby po continue to przy natrafieniu na continue program wracalby do petli nie zmieniajac n , ergo petlilby sie na pierwszej liczbie spelniajacej warunek if
    if n % 2 == 0: # dla liczby parzystej przechodzi do nastepnej iteracji
        continue
    print(n) # jesli warunek if powyzej nie jest spelniony drukuje liczbe
    
    
# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False

idx = 0
while idx < len(lista_do_przeszukania):
    print(lista_do_przeszukania[idx])
    idx += 1


# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 63

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc: # sprawdzamy czy liczba 'wartosc jest w liscie
        flaga = True
        break
    idx += 1
    
if flaga:
    print('elemet {} znaleziono'.format(wartosc))

# %%
lista_do_przeszukania = [12, 53, 13, 53, 34]
flaga = False
wartosc = 55

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc: # sprawdzamy czy iczba 'wartosc jest w liscie
        flaga = True
        break
    idx += 1
    
if flaga:
    print('elemet "{}" znaleziono'.format(wartosc))
else:
    lista_do_przeszukania.append(wartosc) # jesli zadanej liczby nie ma w liscie dodajemy ja do listy
    print('element "{}" dodano do listy'.format(wartosc))
    
    
# %%
numbers = [1, 2, 3, 4, 45, 56, 67, 23,34]
szukana = 23

idx = 0
while idx < len(numbers):
        if numbers[idx] == szukana:
            print('znaleziono')
            break
        idx += 1
else:
    print('nie znaleziono') # najwyrazniej do petli while tez da sie zrobic else
    
# %%
KOD_PIN = '0000' # duzymi literami oznaczamy stałe w programie
pin = input('Podaj kod pin: ')

while pin != kod_pin:
    pin = input('Podaj wlasciwszy kod pin: ')

print('Zalogowano')

# %%
KOD_PIN = '0000' # duzymi literami oznaczamy stałe w programie
pin = input('Podaj kod pin: ')

i = 0
while i < 2 and pin != KOD_PIN:
    i += 1
    pin = input('Podaj wlasciwszy kod pin: ')
    
if pin == KOD_PIN:
    print('zalogowano')
else:
    print('za duzo prob')

# %%
KOD_PIN = '0000' # duzymi literami oznaczamy stałe w programie

pin = ''
i = 0

while i < 3 and pin != KOD_PIN:
    pin = input('Podaj kod pin: ')
    if pin == KOD_PIN:
        print('zalogowano')
        break
    i += 1
else:
    print('za duzo prob')

