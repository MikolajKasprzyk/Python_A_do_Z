# -*- coding: utf-8 -*-

def parabola(x):
    return x**2 + 3

print(type(parabola))

print(parabola(30))

# %%
funkcja_1 = parabola # przypisujemy funkcja_1 funkcję parabola, czyli mozemy wywolywac za pomoca tej zmiennej ta funkcje

print(funkcja_1(30))

# %%
#definicja funkcji lambda
lambda x: x**2 + 3  # po uruchomieniu tego zwrocony jest obiekt typu function

f = lambda x: x**2 + 3  # preferowany sposob dla przekazywania funkcji mozliwych do zdefiniowania w 1 linii

print(f(30))

# %%
f_2 = lambda word: word.upper()

f_2('python')

# %%
f_3 = lambda x, y: x + y

f_3(3,5)

# %%
f_4 = lambda word_1, word_2: word_1 + ' ' + word_2

f_4('Hello', 'world')

# %%
lista = ['python', 'java', 'r', 'sql']

list(map(lambda word: word.upper(), lista)) # zamieniamy wszystkie litery na duze w calej liscie

# %%
def make_upper(word):
    return word.upper()

list(map(make_upper, lista)) # to jest rownowazne z tym co powyzej

# %%
list(map(str.upper, lista)) # i to po prawdzie tez jest rownowazne

# %%
list(map(lambda word: word.title(), lista))
# %%
list(map(str.title, lista))

# %%
tuple(map(lambda word: (word, len(word)), lista)) # zwraca tuple tupli slowo, jego dlugosc


#%%
tuple(map(lambda word: [word, len(word)], lista)) # zwraca tuple list slowo, jego dlugosc

# %%
list(map(lambda word: [word, len(word)], lista)) # lista list

# %%
def apply_function(x, function):
    return function(x)

apply_function(5, lambda x: x**2)
apply_function([12, 14], lambda x: sum(x))

# %%
numbers = [2, 5, 8, 9, 3, 12, 45, 666]
sorted(numbers)
# %%
numbers = [-3, -2, -1, 0 , 1, 2 , 3]
sorted(numbers, key=lambda x: abs(x)) # sortowanie po kluczu wartosci bezwzglednej

# %%
lista = [('jeden', 'one'),('dwa', 'two'), ('three', 'trzy')]
sort_pol = sorted(lista) # domyslnie sortuje po 1 elemencie kazdej zagniezdzonej tupli
sort_ang = sorted(lista, key=lambda x: x[1]) # tu zadajemy klucz zeby sortowalo po drugim elemencie tupli (indeksowanie od 0) ergo slowie po angielsku

# %%
# zadanie: utworz liste zawierajaca 3 pierwsze litery miast

cities = ['warsaw', 'berlin', 'london', 'new york']

new_list = list(map(lambda x: x[:3], cities))































