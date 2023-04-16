# -*- coding: utf-8 -*-

tekst = 'witaj na kursie Pythona.\npython jest wspaniały.'

print(tekst)

# %%
dir(tekst)

help(str.count) # pomoc do danej metody dla danego typu (str)

# %%
tekst.capitalize() # returns a copy of the original string and converts the first character of the string to a capital (uppercase) letter, while making all other characters in the string lowercase letters

# %%
tekst.title() # duze litery na poczatku kazdego wyrazu

# %%
tekst.count('Python') # zwraca liczbe ile razy ten podciąg wystąpił w ciągu, rozroznia wielkosc liter


# %%
tekst.startswith('wi') # podaje wartosc logiczna czy tekst zaczyna sie od podanego ciagu

'python'.startswith('py')

# %%
tekst.endswith('y.') # analogicznie jak wyze tyle ze koniec

# %%
'sample.jpg'.endswith('.jpg') # sprawdzenie typu pliku po rozszerzeniu

# %%
tekst.find('Python') # zwraca nr indeksu od ktorego zaczyna sie zadane slowo w ciagu
tekst[tekst.find('Python'):]

# %%
hashtags = 'sport#gym'
idx = hashtags.find('#')
hashtags[:idx]

# %%
'pawel1234'.isalnum() # sprawdza czy w ciagu sa tylko znaki alfanumeryczne

# %%
'python'.islower() # zwraca bool czy litery sa male

'python'.isupper() # analogicznie duze

# %%
' '.join(['python', '3,7'])
'#'.join(['sport', 'gym', 'dupa'])  # laczy zadane ciagi przy pomocy podanego na poczatku komendy
'AAAA'.join(['sport', 'gym', 'dupa'])

# %%
'#good#time#mood'.replace('#',' ' )

# %%
'column name'.replace(' ', '_')

# %%
'      python    '.strip() # usuwa spacje przed i po ciągu
'      python    '.rstrip() # usuwa spacje po ciągu
'      python    '.lstrip() # usuwa spacje przed ciągu

# %%
'1,2,3,4,5'.split(',') # zwraca liste z elementami rozdzielonymi wg zadanego znaku - tutaj przecinek
'python java php sql sas'.split() # domyslnie dzieli wg spacji

# %%
'12'.zfill(5) # dopisuje zera do zadanej liczby cyfr

#%%
'#'.join(['sport', 'python', 'free', 'time'])

# %%
name = 'python'
version = 3.7
print(name, version)

# %%
name = 'PythOn'
print(name.lower())

# %%
x = 'Programowanie w języku Python - od A do Z'
x = x.lower()
x = x.replace('-','')
x = x.replace(' ','')
x = x.replace('ę','e')

set(x)
print(len(x))

#%%
# usunac spacje i myslnik, zmienic na male litery 
# zrobic zbior z literami i podac wielkosc tego zbioru
x = 'Programowanie w języku - Python od A do Z'
x = x.lower()
x = x.replace('ę','e')
x = x.replace(' ','')
x = x.replace('-','')
     
zbior = set(x)

print(len(zbior))
 
# %%
# wersja skrocona
x = 'Programowanie w języku - Python od A do Z'

x = x.lower().replace(' ', '').replace('-', '').replace('ę', 'e')
print(len(set(x)))
