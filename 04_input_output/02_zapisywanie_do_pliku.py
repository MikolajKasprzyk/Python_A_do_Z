# -*- coding: utf-8 -*-

techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'w') as plik: # w czyli write, jesli pliku nie ma zostaje stworzony
    for tech in techs:
        print(tech, file = plik)
        
# %%
even_nuber = list(range(100))[::2]

with open('even_numbers.txt', 'w') as plik:
    for number in even_nuber:
        plik.write(str(number) + '\n')
        
# %%
techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'a') as plik: # a czyli append, czyli dopisuje do pliku a nie nadpisuje, jesli pliku nie ma zostaje stworzony
    for tech in techs:
        print(tech, file = plik) 
        
        
# %%
technologies = []
with open('techs.txt', 'r') as file:
    for line in file:
        technologies.append(line)
print(technologies)



# %%
technologies = []
with open('techs.txt', 'r') as file:
    for line in file:
        technologies.append(line[:-1]) # nawias kwadratowy usuwa znak przejscia do kolejnej linii z listy
print(technologies)
        
# %%
lista = ['ale', 'mele', 'dupa', 'sraka']
with open('elemele.txt', 'w') as plik:
    for i in lista:
        plik.write(i + '\n')
        
# %%
# polaczenie petli for z formatowaniem tekstu - cel zbudowac dwa trojkaty z gwiazdek

with open('trojkaty.txt', 'w') as plik:
    for j in range(2):
        for i in range(10):
            print('{:>9}'.format('*' * i), end = '', file = plik) # {:>9} tekst drukowany od prawej strony od 9 miejsca
            print('{}'.format('*' * i), file = plik)
            
            
