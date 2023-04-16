# -*- coding: utf-8 -*-

# %%
1 / 0

# %%
1 + 'text'


# %%
int('f')

# %%
float('adsa')

# %%
try:
    1 / 0
except:
    print('Nie dzieli sie przez 0')
    
# %%
try:
    1 / 0
except ZeroDivisionError:
    print('Nie dzieli sie przez 0')
except TypeError:
    print('zly typ')

# %%
try:
    4 + '4'
except TypeError:
    print('nie mozna dodawac tekstu do liczby')

# %%
try:
    int('sd')
except ValueError:
    print('zly tekst')

# %%
while True:
    try:
        x = int(input('Podaj liczbe:  '))
        break
    except ValueError:
        print('niepoprawna wartosc')   # petla dziala poki nie poda sie wlasciwej wartosci
        
# %%
try:
    with open('nieistniejacy.txt', 'r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print('plik nie istnieje')

# %%
raise TypeError('Błąd')

# %%
raise ValueError('Błąd wartosci')

# %%
def divide(x, y):
    try:
        x = int(x)
        y = int(y)
        return x / y
    except ZeroDivisionError:
        print('dzielenie przez zero')
    except ValueError:
        print('wprowadz liczbe')

#divide(3,0)

divide('1asasas', 3)

# %%












