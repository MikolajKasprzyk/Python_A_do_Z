# -*- coding: utf-8 -*-

# %%
abs(13) # zwraca modul liczby (wartosc bezwzgledna) tutaj 13
abs(-20) # zwraca 20

# %%
bool()  # zwraca wartosc logiczna danego obiektu
bool([]) # false
bool('abc') # true
bool(True)
bool(False)
bool(12) # dla liczb roznych od zera true

# %%
dir(list) # zwraca wszystkie atrybuty i metody dla danego obiektu
dir(tuple)

# %%
enumerate(['pawel', 'pytho', 'java']) # zwraca liste par tupli z indeksami i wartosciami

# %%
eval('1 + 1') # oblicza dzialania ze zmiennej tekstowej

x = 10
eval('x + 13')

# %%
list(filter(abs, [-2, -1, 0, 1, 2])) # zwraca te pierwotne wartosci ktorych wartosc logiczna po zastosowaniu funkcji jest true

# %%
list(filter(bool, ['python', '', 'java']))

# %%
float(1) # zamienia zadana liczbe/tekst na liczbe z przecinkiem
float('123')
float('3.5')

# %%
type(1) # zwraca typ zmiennej

# %%
help(float) # drukuje do konsoli pomoc

# %%
isinstance(1, int) # zwraca wartosc logiczna czy dany obiekt nalezy do danej klasy
isinstance(1.0, float)
isinstance('tekst', str)
isinstance('', str)

#%%
len('python') # zwraca dlugosc elementow
len('')
len([[1,2],[2, 4, [3, 7, 8]]])

# %%
list('python') # przyjmuje obiekt iterowalny i zwraca liste z pojedynczymi elementami
list(range(10))

# %%
list(map(abs, [-2, -1, 0, 1, 2])) # mapuje zastosowanie funkcji do kazdego elementu obiektu
names = ['pawel' ,'tomek', 'janek']
list(map(str.title, names))

# %%
max([1, 2, 3, 4, 5, 6, 7, 8]) # zwraca maksimum ze danego obiektu
max('pawel') # zwraca litelre najdalsza od poczatku alfabetu

# %%
min([1, 2, 3, 4, 5, 6, 7, 8]) # zwraca min ze danego obiektu
min('pawel') # zwraca litere najblizsza od poczatku alfabetu

# %%
pow(2, 3) # 2 do potegi 3

# %%
list(reversed([5, 1, 9])) # odwraca kolejnosc w zadanym obiekcie
list(reversed('python'))

# %%
round(3.45879687231, 5) # zaokraglenie do 5 miejsca

# %%
str(1) # zamienia wartosci na string

# %%
sum([1, 2, 3, 4, 5, 6]) # podaje sume obiektu iterowalnego

# %%
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

list(zip(lista_1, lista_2)) # zwraca liste tupli par wartosci z obu list

# %%
list(zip('python', 'course')) 


# %%
# zadanie sprawdzic typ zadanych obiektow
lista = [(1,2,3), {1,2,3}, [1,2,3], {1:1, 2:2, 3:3}, '123', 123]
for i in lista:
    print(type(i))



