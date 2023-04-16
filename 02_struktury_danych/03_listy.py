# -*- coding: utf-8 -*-

# listy sa zmienne w przeciwienstwie do tupl
# elementy sa uporzadkowane i moga byc zduplikowane

empty_list = list()
print(empty_list)

# %%
techs = ['python', 'java', 'c++', 'go', 'sql'] # liste definiujemy w nawiasach kwadratowych
#techs[0] = 'python 3.7'  # tak mozna zmienic pierwszy element listy
print(techs)

# %%
numbers = [3, 5, 3, 5, 23]
print(numbers)
print(type(numbers))

# %%
mixed = ['python', 3.7, 4, True] # elementy listy moga byc roznego typu
print(mixed)

# %%
empty_list = [] # tworzy pusta liste
nested = [[1, 2, [3, 'sql']], ['python', 'java', 'go'], 3] # listy mozna zafniezdzac dosyc dowolnie

# %%
first = ['mleko', 'makaron', 'ziemniaki']
second = ['woda', 'jajka']

bucket = [first, second] # inny sposob zagniezdzenia list
len(bucket)
# %%
suma = first + second + ['scala'] # składa kilka list w jedną

# %%
techs += ['javascript'] # dodaje element na koniec listy

print(dir(list)) # drukuje metody dla list

# %%
print(techs.index('python')) # zwraca numer indexu zadanego elementu

      









