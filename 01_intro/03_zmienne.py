# -*- coding: utf-8 -*-


# konwencja nazywania zmiennych

imie = 'Pawel'
_imie = 'Olek' # zmienna wewnetrzna - nie powinno sie ruszac, nie pokazuje sie w variable explorer

3imie = 'Pawel' # zmienna nie moze zaczynac sie od cyfry ale moiz sie nia konczyc
imie3 = 'Pawel' # to dziala

# %%
a = 8
b = 20
c = a * b
print(c)

# %%
przepracowane_godziny = 8 # dobrze nazywac zmienne tak zeby wiadomo bylo opisuja
stawka_godzinowa = 20

dzienna_pensja =  przepracowane_godziny * stawka_godzinowa
print(dzienna_pensja)


# %%
camelCase = 'python' # konwencje nazywania zmiennych
PascalCase = 'python'
snake_case = 'python' # metody i zmienne, polecane
kebab-case = 'python'
UPPER = 'python'       #stałe 

# sa tez nazwy zarezrwowane dla srodowiska np. print - tego raczej nie nalezy uzywac tego jako nazw zmiennych
# import keyword, keyword.kwlist - wypluwa wszystkie takie nazwy