# -*- coding: utf-8 -*-

val_1 = True
val_2 = False

# %% 
print(val_1)
print(type(val_1))

# %% koninkcja
True and True # true
True and False # false
False and True # false
False and False # false

# %% alternatywa
True or True # true
True or False # true
False or True # true
False or False # false

# %% negacja zwraca wartosc przeciwna
not True
not False

# %%
bool('python') # tekst zawierajacy chociaz jeden znak zwraca true
bool('') # dla pustego stringa zwraca false
bool(0) # dla 0 zwraca false
bool(2) # dla liczby innej niz 0 zwraca true
bool({}) # pusty slownik zwraca false
bool(set()) # pusty zbior false
bool(tuple()) # pusta tupla rowniez false

bool({'key':'val'}) # jak w slowniku cos sie znajduje zwraca true

# %%
# zadanie: wydrukuj do konsoli wartosci logiczne poszczegolnych obiektow
print(bool(' '),'\n', bool(''),'\n',bool('1'),'\n', bool(list['','']))

