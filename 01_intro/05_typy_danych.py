# -*- coding: utf-8 -*-

string = 'Python'

print(dir(string))  # zwaraca dostepne metody dla danego obiektu

# %%
a = 10

print(dir(a))

# %%
type(a)      # podaje typ zmiennej

# %%
b = 4.5
type(b)     # float liczby z przecinkiem

#%%
d = 3 + 3j
type(d)     # complex liczba zespolona

# %%
# typy logiczne bool True i False sa pisane duzymi literami
type(True)

value = True
print(value)

# %%
x = '1323435'
y = 12334
z = '0'

print('x: {}\ny: {}\nz: {}'.format(type(x), type(y), type(z)))