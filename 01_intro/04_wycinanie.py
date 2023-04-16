# -*- coding: utf-8 -*-

 name = 'Python'
 
 # %%
 print(name)
 print(name[0]) # indeksowanie znakow od 0
 print(name[3])
 
 print(name[-1]) # indeksowanie od tylu - to zwraca ostatnia litere
 
 # %%
# name[start:stop] - od ineksu do indeksu, lewostronnie domkniety prawostronnie otwarty
name[1:4]
name[:4]  # od poczatku do indeksu 4
name[2:]  # od 4 do konca

name[:]

# %%
name[-2:] # przedostani element do konca
name[-3:-1]

# %%
full = 'Python Programming'
print(full[7:])
print(full[::2]) # podaje co drugi znak od poczatku do konca
 # name[start:stop:step] od indeksu start do stop co ktorys (step) znak

# %%
sample = '#stop#this#flow'
print(sample[::5])

# %%
numbers = '8,9,7,4'
print(numbers[::2])

# %%
print(name[::-1]) #odwaraca kolejnosc

# %%
name = 'Python'
'Pyth' in name    # sprawdza czy dany podciag jest w ciagy


