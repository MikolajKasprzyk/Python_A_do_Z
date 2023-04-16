# -*- coding: utf-8 -*-

class Drzewo:
    
    nazwa = 'sosna'
    wiek = 40
    wysokosc = 25
    
    
drzewo_1 = Drzewo()
drzewo_2 = Drzewo()

# %%
id(drzewo_1)
    
id(drzewo_2)
    
# %%
dir(drzewo_1)
    
# %%
drzewo_1.nazwa
drzewo_1.wiek
drzewo_1.wysokosc


# %%
drzewo_1.stan = 'dobry' # dodatkowy atrybut instancji - przypisuje sie do konkretnej instancji

dir(drzewo_1)
    
# %%
Drzewo.miejsce = 'las' # przy przypisaniu danej klasie nowego atrybutu jest on dodawany do kazdego obiektu tej klasy

dir(drzewo_1)
dir(drzewo_2)
    
# %%
drzewo_2.miejsce = 'twoja dupa' # zmiana wartosci atrybutu 
print(drzewo_2.miejsce)  
    
    
    