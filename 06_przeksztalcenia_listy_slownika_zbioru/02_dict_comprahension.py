# -*- coding: utf-8 -*-

stock = {'AMZN' : 'Amazon.comn Inc', 'APPL.US' : 'Apple Inc', 
         'GOOGL.US' : 'Alphabet Inc', 'MSFT.US' : 'Microsoft Corp',
         'UBER.US' : 'Uber Technologies Inc'}

# %%
stock.keys() # zwraca klucze slownika
stock.values() # zwraca wartosci
stock.items()   # zwraca liste tupli z parami (klucz, wartosc)

for key, value in stock.items():
    print('{:8} : {}'.format(key, value)) # {:8} rezerwuje 8 miejsc dla tekstu, w przypadku jakby klucze mialy rozne dlugosci dzieki temu dwukropki ustawiaja sie w jednej linii przy printowaniu

# %%
stocks_dict = {key:value for (key, value) in stock.items()}

# %%
stocks_set = {(key,value) for (key, value) in stock.items()}

# %%
stocks_invert = {value:key for (key, value) in stock.items()}

# przy takiej akcji na;ezy pamietac ze slownik musie miec unikalne klucze - czyli w teki sposob da sie odwrocic slownik majacy unikalne wartosci ktore staja sie kluczami po odwroceniu

# %%
stocks_lower = {key.lower():value for (key, value ) in stock.items()}

# %%
# zostawiamy klucze w wartosci dajemy dlugosc nazwy elementu
stocks_length = {key:len(value) for (key, value) in stock.items()}

# %%
stocks_length = {key:value + ' : ' + str(len(value)) 
                 for (key, value) in stock.items()}

# %%
def replace_corp_inc(name):
    name = name.replace('Corp', '0')
    name = name.replace ('Inc', '1')
    return name

stocks_flag = {k:replace_corp_inc(v) for (k, v) in stock.items()}

# %%
# wydobyc spolki ktore maja 'corp'
stocks_corp = {k:v for (k,v) in stock.items() if 'Corp' in v}

stocks_inc = {k:v for (k,v) in stock.items() if 'Inc' in v}

# %%
stocks_A = {key:val for (key, val) in stock.items() if val.startswith('A')}

# %%

stocks_A_less13 = {key:val for (key, val) in stock.items() 
                   if val.startswith('A') if len(val) < 13}

# %%
{key: 'Corp' if 'Corp' in val else 'Inc' for (key, val) in stock.items()}

# %%
numbers = range(20)
number_dict = {}

for number in numbers:
    if number % 2 == 0:
        number_dict[number] = number ** 2
        
    


# %%

numb_dict_2 = {key:key**2 for key in numbers if key % 2 == 0 }

# %%
nested_dict = {'001': {'price': 100}, 
               '002': {'price': 40}, 
               '003': {'price': 60}}

for key, val in nested_dict.items():
    print(key, val)

# %%
{key:val['price'] for (key, val) in nested_dict.items()}

# %%
nested_dict_2 = {'001': {'price': 100, 'items': 4}, 
               '002': {'price': 40, 'items': 9}, 
               '003': {'price': 60, 'items': 8}}


for key, val in nested_dict_2.items():
    print(key, val)


{key:val['price'] for (key, val) in nested_dict_2.items()}
{key:val['price'] * val['items'] for (key, val) in nested_dict_2.items()}






