# -*- coding: utf-8 -*-

# %%
index = [0, 1, 2, 3, 4, 5] # przy ineksowaniu od lewej zaczynamy od 0
idx_ng = [-6, -5, -4, -3, -2, -1] # jak indeksujemy od prawej zaczynamy od -1

lista = [34, 23, 56,24,23,76]

# %%
#   lista[start:stop] - wycinianie lewostronnie domkniete
#   lista[index] - wycina podany indeks
#   lista[start:] - od podanego indeksu do konca
#   lista[:stop] - od poczatku do podanego indeksu
#   lista[::step] - co ktorys element

lista[0]
lista[1]
lista[-1]

lista[-3]

# %%
lista[1:5]
lista[-5:-1]

lista[::-1] # podaje liste od tyłu

# %%
lista[:4] # elementy o indeksach od 0 do 3 (4 juz nie wchodzi)

lista[3:] # elementy o indeksach od 3 (włącznie) do końca







