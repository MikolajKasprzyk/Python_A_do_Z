# -*- coding: utf-8 -*-

empty_dict = dict()
print(empty_dict)

d = {} # definicja pustego slownika

e = set() # dla przypomnienia definicja zbioru
print(e)

# %%
# slownik jest nieuporzadkowany i zawiera pary: klucz - wartosc
# klucze nie moga sie powtarzac
pol_to_eng = {'jeden':'one', 'dwa':'two', 'trzy':'three'} # trzy pary klucz - wartosc gdzie kluczami sa jeden, dwa, trzy

# wydobywamy dane za pomoca klucza tak jak w liscie indeksy

name_to_digit = {'jeden':1, 'dwa':2, 'trzy':3} # porzadek nie ma tu znaczenia

# %%

name_to_digit = {0:1, 1:2, 2:3} # porzadek nie ma tu znaczenia

len(name_to_digit) # zwraca ilosc par klucz wartosc slownika

# dict = {'key1':'value', 'key2':'value2'}

# %%
pol_to_eng['cztery'] = 'four' # dodawanie wartosci do slownika

# %%
pol_to_eng.clear() # czysci slownik do zera

# %%
pol_to_eng_copied = pol_to_eng.copy() # kopia slownika

# %%
lista_kluczy = list(pol_to_eng.keys()) # zrobienie listy z kluczami zadanego slownika

# %%
lista_wartosci = list(pol_to_eng.values()) # zrobnienie listy z wartosciami ze slownika

# %%
lista_par = list(pol_to_eng.items()) # zwraca liste tupli z parami klucz - wartosc

# %%
pol_to_eng['jeden'] # zwraca wartosc dla zadanego klucza, jak klucza nie ma dostajemy error


pol_to_eng.get('zero', 'NaN') # na drugim parametrze podajemy co w przypadku jesli klucza nie ma w slowniku

# %%
pol_to_eng.pop('dwa') # klucz musi byc podany, zwaraca wartosc wg zadanego klucza i usuwa daną pare ze slownika

# %%
pol_to_eng.popitem() # zwroci dowolna pare ze slownika i ja usunie, nie zadaje sie argumentu

# %%
pol_to_eng.update({'jeden':1}) # do klucza jeden zostaje nadpisana wartosc: 1

# %%
# utworz slownik ktory zmapuje pierwsze piec licz naturalnych z ich kwadratami i wydrukj go w konsoli
kwadrat = {1:1*1, 2:2*2, 3:3*3, 4:4*4, 5:5*5}
print(kwadrat)

# %%
# podany jest slownik 
capitals = {'Polska':'Warszawa', 'Niemcy':'Berlin', 'Czechy':'Praga'}
# dodaj kolejny element do slownika Włochy:Rzym
capitals['Wlochy'] = 'Rzym'
# nastepnie utworz liste i przypisz do nie posortowane alfabetycznie nazwy stolic
lista_stolic = sorted(list(capitals.values()))



