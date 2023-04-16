# -*- coding: utf-8 -*-

# zbior to nieuporzadkowany ciag elementow
# wartosci nie sa zduplikowane

empty_set = set()
print(empty_set)
print(type(empty_set))

# %%
techs = {'python', 'java', 'c++', 'sql'} # obiekt typu zbior

 # kolejnosc w zbiorze nie jest istotna
 
print(techs)
print(type(techs))
print(len(techs)) # zwraca wielkosc zbioru

# %%
set('python') # zwraca zbior z literami
set('aaaaaaale') # zwraca zbior z unikatowymi wartosciami tutaj a, l, e

# %%
'python' in techs # sprawdza czy dana wartosc jest w zbiorze true/false

# %%
print(dir(set))

# %%
techs.add('sas')    # dodawanie do zbioru
print(techs)

# %%
techs.remove('sas')     # usuwanie ze zbioru
print(techs)

# %%
techs.pop() # usuwa element ze zbioru (losowy)

# %%
techs.clear()   # czysci caly zbior
print(techs)

# %%
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}

C.issubset(A) # czy zbior C jest podzbiorem A

C.issubset({5, 7}) 

A.issuperset(C) # czy zbior A jest nadzbiorem C

A.union(B) # suma zbiorów, nadal wartosci wystepuja pojedynczo
A.intersection(B)   # zwraca wartosci wystepujace w obu zbiorach
A.symmetric_difference(B)   # zwraca elementy wystepujace tylko w jednym ze zbirow A i B

A.copy(D)  # kopia zbioru

