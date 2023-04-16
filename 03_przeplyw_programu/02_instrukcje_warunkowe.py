# -*- coding: utf-8 -*-


# %%
version = 3.7

# %%
version > 3 # zwraca true

version <= 3 # zwraca false

# %%
number = 1200

number > 1000 # true
number == 1200 # == to operator porownania, pojedynczy to operator przypisania

number != 1000 # srawdzamy czy wartosc jest rozna od zadanej

# %%
# if [warunek]:
#     [instrukcja]

# %%
if 8 < 10:
    print('tak')

# %%
a = 5
if a > 10:
    print('a > 10')
else:
    print('a<=10')    

# %%
age = 12
if age < 18:
    print('nie masz uprawnien')
else:
    print('masz uprawnienia')

# %%
age = 12
if age == 18:
    print('masz 18 lat')
elif age < 18: # else if ....
    print('nie masz uprawnien')
else:
    print('masz uprawnienia')

# %%
age = 18
if age == 18:
    print('masz 18 lat')
elif age < 18: # else if ....
    print('nie masz uprawnien')
elif age > 18: # to jest o tyle lepsze ze widac w kodzie co konkretnie obsluguje ten trzeci przypadek a nie ze cala reszte
    print('masz uprawnienia')

# %%
age = int(input('podaj swoj wiek:\n'))


if age == 18:
    print('masz 18 lat')
elif age < 18: # else if ....
    print('nie masz uprawnien')
elif age > 18: # to jest o tyle lepsze ze widac w kodzie co konkretnie obsluguje ten trzeci przypadek a nie ze cala reszte
    print('masz uprawnienia')
    
    
# %% zadanie: stworz instr. warunkowa czy zmienna x jest wieksza od 0 , wydrukuj w konsoli
x = int(input('podaj liczbe:\n'))

if x > 0:
    print('x > 0')
else:
    print('x<=0')            