# -*- coding: utf-8 -*-

# %%
raw_data = '345!23!3234!43434'
data = ''
for char in raw_data:
    if char == '!':
        data += ','
        continue
    data += char
print(data)

#%%
raw_data = '345!23!3234!43434'
data = ''
for char in raw_data:
    if char != '!':
        data += char
    else:
        data += ','
print(data)

#%%
raw_data = '345!23!3234!43434'
data = raw_data.replace('!', ',')
print(data)

#%%
# sumowanie elementow
suma = 0
for i in range(10):
    suma += i
print(suma)

#%%
saldo = 450
print('saldo poczatkowe: {}'.format(saldo))
for kwota in range(10, 60, 10):  # range od 10 do 60 co 10 (10,20,30,40,50)
    print(' wyplacona kwota {}'.format(kwota))
    saldo -= kwota
    print('saldo: {}'.format(saldo))
print('saldo koncowe: {}'.format(saldo))    
     
# %%
# sprawdzenie czy podany kod pin jest cyframi
pin = '1234678'
for char in pin:
    if char.isdigit() == False:
        print('zly znak')
        break
else:
    print('poprawny')
    
# %%
#sprawdzenie czy pin sa cyframi
nick = 'aaaa' # input('podaj nick: ')
pin = input('podaj 4- cyfrowy PIN, {}: '.format(nick))

if len(pin) == 4:    
    for char in pin:
        if char not in '0123456789':
            print('nieporawny pin - maja byc same cyfry')
            break
    else:
        print('pin poprawny')
else:
    print('zla dlugosc kodu')




