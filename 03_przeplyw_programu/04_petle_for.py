# -*- coding: utf-8 -*-

# %%
name = 'python'

for i in name:
    print(i)

# %%

name = 'python'
index = 0
for i in name:
    print(index, i)
    index += 1
    
# %%
for index in range(10): # range zwraca obiekt iterowalny z liczby - np list(range(10)) zwroci liste od 0 do 9
    print(index)

# %%
for index in range(len(name)):
    print('Nr indeksu: ', index, 'Litera', name[index])
    
# %%
for i in enumerate(name):  # enumerate zwraca tuple z numerem indeksu i przypisanym mi stringiem
    print(i)
    
# %%
name = 'python'
for index, character in enumerate(name): # enumerate jest preferowana metoda przy obiektach iterowalnych
    print(index, character)
    
# %%
for i in [4, 5, 6, 8, 6]:
    print(i)
    
# %%
for i, value in enumerate([4, 5, 6, 8, 6,]):
    print(i, value)
    
# %%
for i in range(10):
    print(i)
    
# %%
for i in range(10,20): # range tworzy iterator od 10 do 19
    print(i)
    
#%%
for i in range(10,20,2): # range tworzy iterator od 10 do 20 co 2
    print(i)
    
# %%
for i in range(10,-1,-1):
    print(i)

    
# %%
for i in range(10,100,10):
    print(i)
    
# %%
techs = 'java'

for i in range(len(techs)):
    print(i, techs[i])

# %%
string = 'Python Course'

for char in string:
    print(char)

# %%
# chcemy wyciac do 6 indeksu


string = 'Python Course'

for char in string[:6]:
    print(char)
    
# %%
# co drugi znak


string = 'Python Course'

for char in string[::2]:
    print(char)
    
# %%
# od konca


string = 'Python Course'

for char in string[::-1]:
    print(char)

# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    print(char)

# %% drukuje wszystkie znaki poza '#'
hashtags = '#sport#gym#fitness'
for char in hashtags:
    if char != '#': 
        print(char)
         
# %% drukuje wszystkie znaki poza '#'
hashtags = '#sport#gym#fitness'
for char in hashtags:
    if char not in '#': 
        print(char)
    
# %%
for char, number in zip('abcde', '12345'): # zwraca tuple z parami znakow z obu stringow, obcina do najkrotszego
    print(char, number)
    
# %% wypisuje slowa bez hashtagow po koleji
hashtags = '#sport#gym#fitness'
result = ''

for char in hashtags:
    if char != '#':
        result = result + char
    else:
        print(result)
        result = '' # ostatnie slowo fitness nie jest printowane bo nie ma znaku # na koncu, stad ten print na koniec poza petla

print(result)        

# %%
# zadanie: korzystajac z petli wydrukuj do konsoli liczby od 0 do 20 wlacznie
for i in range(21):
    print(i)
    
#%%
hashtags = '#weekend#good#time'
slowo = ''
for char in hashtags:
    if char != '#':
        slowo = slowo + char
    else:
        print(slowo)
        slowo = ''

print(slowo)
