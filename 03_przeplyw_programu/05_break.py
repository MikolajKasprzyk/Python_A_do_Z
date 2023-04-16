# -*- coding: utf-8 -*-


# %%
for i in '0123456789':
    i = int(i)
    if i == 6:    
        print(i, type(i))
        break  # przerywa dzialanie petli
        
# %%
for i in '0123456789':
    i = int(i)
    if i == 6:    
        break  # przerywa dzialanie petli
    else:
        print(i, type(i))

print('koniec')
        
# %% printujemy znaki do napotkania spacji
sample = 'Python Course'

for char in sample:
    if char != ' ':
        print(char)
    else:
        break
# %%
sample = 'Python Course'

for char in sample:
    if char == ' ':
        break
    print(char)
    
print('Koniec')

# %%

for char in 'kowalskij@gmail.com':
    if char == '@':
        print('mail jest poprawny')
        break
else:
   print('adres niepoprawny')
    
# %%
# zadanie; sprawdic czy haslo ma powyzej 10 znakow, jest conajmniej 1 znak '!'

ps = 'jnhvs@svd'

if len(ps) >= 10: 
    for char in ps:
        if char == '!':
            print('haslo poprawne')
            break
    else:
        print('brakuje @')
else:
    print('haslo za krotkie')
    
#%%
ps = 'jnhvssva@sasasasd'

if len(ps) >=10:
    if '@' in ps:
        print('haslo poprawne')
    else:
        print('brakuje @')
else:
    print('haslo za krotkie')


