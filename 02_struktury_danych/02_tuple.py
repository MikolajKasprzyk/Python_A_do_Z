# -*- coding: utf-8 -*-

empty_tuple = tuple() # tuple raz zdefiniowane nie dają sie zmieniać

print(empty_tuple)

# %%
amazon = ('Amazon', 'USA', 'Technology', 1) # przykład definicji tupli, można łączyć różne typy danych
google = ('Google', 'USA', 'Technology', 2)

# %%
name = google[0]

# %%
data = (amazon, google) # tupla złożona z dwoch innych tupli - mozna zagnieżdzać
print(data)

# %%
a = ('Mikołaj', 'Kasprzyk')


# %%
imie, nazwisko, id_user = ('Mikolaj', 'Kasprzyk', '001')  # przypisanie kilku zmiennych na raz

# %%
amazon_name, country, sector, rank = amazon # przypisanie wartosci ze zdefiniowanej wczesniej tupli

# %%
stocks = 'Amazon', 'Apple', 'IBM' # mozna tez zdefiniowac bez nawiasow

print(type(stocks))

# %%
nested = 'Europa', 'Polska', ('Warszawa', 'Krakow', 'Wroclaw') # zagnieżdzona tupla

print(nested)

# %% 
# zamiana wartoci tych dwoch zmiennych z dodatkowa zmienna
a = 12
b = 14

c = b
b = a
a = c
print(a, b)

# %%
# zmiana wartosci dwoch zmiennych przy uzyciu tupli - bez trzeciej zmiennej
x, y = 10, 15

x, y = y, x
print(x, y)


