# -*- coding: utf-8 -*-

print('Program uruchomiony.')
print("""Włam się do systemu zgadujac dwucyfrowy kod pin.
Numer pin sklada sie z cyfr: 0, 1, 2.""")

pin = input('Wprowadz pin:\n')

if pin == '21':
    print('brawo trafiles')
elif pin == '20':
    print('byles blisko')
else:
    print('nie zgadles')
    
# %%

print('Program uruchomiony.')
print("""Włam się do systemu zgadujac dwucyfrowy kod pin.
Numer pin sklada sie z cyfr: 0, 1, 2.""")

pin = int(input('Wprowadz pin:\n'))

if pin == 21:
    print('brawo trafiles')
elif pin == 20:
    print('byles blisko')
else:
    print('nie zgadles')
    
# %%
string = 'asasas'

if string: # jezeli jest to prawda czyli jezeli cokolwiek jest w tym stringu
    print('niepusty ciag znakow')
else:
    print('pusty ciag znakow')
    
# %%
number = 1

if number: # zero zwraca bool false, inne liczby zwracaja true
    print('rozna od zera')
else:
    print('zero')

# %%
default_flag = True

if default_flag:
    print('doszlo do zdarzenia default')
else:
    print('nie doszlo do zdarzenia default')

# %%
default_flag = True

if not default_flag:     # if not w sumie samowyjasnijace
    print('nie doszlo do zdarzenia default')
else:
    print('doszlo do zdarzenia default')
    
# %%
# zadanie: v = 55 oznacza predkosc. jesli v > 50 wydrukuj 'zwolnij' jesli mniejrowno wydrukuj 'tak trzymaj'

v = 45

if v > 50:
    print('Zwolnij')
else:
    print('tak trzymaj')


# %%

# sprawdzamy czy klient banku jest zweryfikowany zeby dac mu kredyt

saldo = -10000
klient_zweryfikowany = True

if saldo > 0 and klient_zweryfikowany:
    print('mozesz wyplacic gotowke')
else:
    print('nie mozesz wyplacic')
    

# %%

# sprawdzamy czy klient banku jest zweryfikowany zeby dac mu kredyt

saldo = 10000
klient_zweryfikowany = True

amount = int(input('ile chcesz gotowki'))

if saldo >= amount and klient_zweryfikowany:
    print('mozesz wyplacic gotowke')
else:
    print('nie mozesz wyplacic')
    

# %%

# sprawdzamy czy klient banku jest zweryfikowany zeby dac mu kredyt

saldo = 10000
klient_zweryfikowany = True

amount = int(input('ile chcesz gotowki:   '))

if saldo > 0 and klient_zweryfikowany and saldo >=amount:
    print('mozesz wyplacic gotowke')
else:
    print('nie mozesz wyplacic.\n'
          'Brak kwoty {}'.format(amount - saldo))    
    
# %%
#zadanie podana jest zmienna tekstowa 
# fakt = 'python jest latwy i przyjemny'
# stworz liste znakow ze zmienej 'fakt' a potem unikalny zbior znakow z listy
# instr. warunkowa ktora sprawdzi czy dlugosc otrzymanego zbioru jest mniejsza od 20 i wydrukuje 'mniej' lub 'wiecej'

fakt = 'python jest latwy i przyjemny'

if len(set(list(fakt))) < 20:
    print('mniej')
else:
    print('wiecej')


# %%
# sprawdzenie czy dany znak wystepuje w zbiorze/stringu
# 'p' in 'python' # czy p wystepuje w python - zwraca true

name = 'python'

if 'p' in name:
    print('znaleziono p')
else:
    print('nie znaleziono p')

# %%    
# zapisywanie instrukcji w jednej linijce
tech = 'python' 
if tech == 'python':
    flag = 'dobry wybor'
else:
    flag = 'poszukaj dalej'
    
print(flag)

# %%
# to jest rownowazne z tym powyzej
tech = 'python'

flag = 'dobry wybor' if tech == 'python' else 'poszukaj dalej'

# %%
'dobry wybor' if tech == 'python' else 'poszukaj dalej' # zwraca string bez przypisania go do zmiennej

# %%
# zadanie: sprawdz czy zmienna tekstowa zawiera daną litere
zadany_znak = input('podaj szukany znak:  ')
text = 'alamakotaakottoidiota'
print('zawiera') if zadany_znak in text else print('nie zawiera')












