# -*- coding: utf-8 -*-

file = open('simple.txt', 'r') # 'r' - od read

for i in file: # domyslnie drukuje nam linijki z pliku co druga linijke
    print(i, end = '') # ta czesc z end = '' - dzieki temu tekst z pliku drukowany co jedną linijke
    
file.close()

# %%
with open('simple.txt', 'r') as file: # to co powyzej tylko krotszy zapis
    for i in file:
        print(i, end='')
        
# 'r' - read otwiera plik do odczytu, zwraca blad jesli plik nie itnieje
# 'a' - append otwiera plik do dopisania, tworzy plik jesli nie isnieje
# 'w' - write otwiera plik do zapisu, tworzy plik jesli nie istnieje


# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    print(line) 
    
# %%
with open('simple.txt', 'r') as file:
    lines = file.readlines() # zwraca liste stringow z linijek pliku
    print(lines) 
    
# %%
with open('simple.txt', 'r') as file:
    lines = file.readlines() # zwraca liste stringow z linijek pliku
    for line in lines:
        print(line, end = '')
    
# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    while line: # warunek zwraca prawda jesli cos jest w linijce linijce (rowniez enter najwyrazniej)
        print(line, end = '')
        line = file.readline()  # ta metoda kolejny raz zastosowana czyta kolejna linijke z pliku
    
        
# %%
with open('simple.txt', 'r') as file:
    lines = file.read()  # odczytuje caly plik
    print(lines)
    
# %%
with open('simple.txt', 'r') as file:
       for i in file: 
           print(i, end = '')
           

# %%
i = 0
with open('simple.txt', 'r') as file:
    lista = file.readlines()
    while i < len(lista): 
        print(lista[i], end = '')
        i += 2
        

                      
           