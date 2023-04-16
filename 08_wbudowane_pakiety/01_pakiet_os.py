# -*- coding: utf-8 -*-

import os

dir(os)

# %%
os.getcwd() # zwraca aktualna sciezke folderu roboczego

# %%
os.chdir('..')  # wchodzimy poziom wyzej do katalogu nadrzednego

# %%
os.chdir('D:\\kurs python\\AdoZ\\08_wbudowane_pakiety') 

os.system('mkdir dir1 dir2 dir3')  # tworzy nam 3 katalogi dir1 dir2 i dir3

# %%
os.rmdir('dir1')  # usuwa katalog

# %%
os.listdir()   # zwraca liste z rzeczami w katalogu roboczym

# %%
for item in os.listdir():    # mozna iterowac po liscie plikow
    if item.endswith('.py'):
        print(item)
        
# %%
for root, dirs, files in os.walk(os.getcwd()):  # przydatna funkcja os.walk
    print(root)
    print(dirs)
    print(files)

# %%
os.path.join(r'home\user\bin', 'python')  # łączy sciezki, r przed tekstem mowi ze przekazujemy surowy tekst

 




















