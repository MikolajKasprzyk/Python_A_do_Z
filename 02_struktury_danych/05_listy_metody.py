# -*- coding: utf-8 -*-


techs = []
print(techs)

# %%
techs.append('python') # dodawanie elementu do listy
print(techs)

techs.append('java')

# %%
techs.append(['hadoop', 'spark']) # dodanie zagniezdzonej listy na koniec listy
print(techs)

# %%
techs.extend(['sql', 'sas']) # dodaje elementy do listy - zamiast zagniezdzonej listy jak .append
print(techs)

# %%
techs.insert(3, 'go') # wstawia obiekt na zadane miejsce
techs.insert(2, 'r')

# %%
techs.pop() # zwraca ostatni element i usuwa go z listy

# %%
techs.pop(3) # zwraca element o zadanym ideksie z listy i usuwa go z listy

# %%
techs = ['python', 'java', 'sql', 'php']

techs.index('java') # zwaraca wartosc indeksu zadanego obiektu

# %%
techs = ['python', 'java', 'sql', 'php', 'python']
techs.count('python') # zwraca liczbe ile razu obiekt wystepuje w liscie, jesli go nie ma zwraca 0

# %%
techs = ['python', 'java', 'sql', 'php', 'r', 'angular']
techs.sort() # sortuje liste, domyslnie alfabetycnie
techs.sort(reverse = True) # sortuje alfabetycznie od tyłu

# %%
techs = ['python', 'java', 'sql', 'php', 'r', 'angular']

techs[::-1] # zwraca liste w odwracononej kolejnosci, nie zmienia listy 
techs.reverse() # odwracanie kolejnosci listy, nadpisuje liste na odwrocona
# %%
techs[1] = 'c++' # nadpisuje obiekt o zadanym indeksie na zadany

# %%
a = [4, 5, 3, 3]
b = [9, 7]
a.extend(b)
print(a)

# %%
# tu to samo co wyzej tyle ze ze zrobieniem nowej listy - pierwotne pozostaja bez zmian
a = [4, 5, 3, 3]
b = [9, 7]

suma_a_b = list(a)
suma_a_b.extend(b)
print(suma_a_b)
# %%
firmy = ['Apple', 'Microsoft', 'samsung']
firmy.extend(['amazon', 'google'])
print(firmy)