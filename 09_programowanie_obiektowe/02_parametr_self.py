# -*- coding: utf-8 -*-

class Drzewo:
    
    def wyswietl_info_o_drzewie(self): # definicja metody dla danej klasy, self - odwoluje sie do obiektu klasy
        self.nazwa = 'Sosna'
        self.wiek = 30                  # przy takim zapisie dopiero po wywolaniu tej funkcji na obiekcie danej klasy zostana mu przypisane atrybuty nazwa i wiek
        print(f'Drzewo {self.nazwa} ma {self.wiek} lat.')

# %%
drzewo_1 = Drzewo()

# %%
drzewo_1.wyswietl_info_o_drzewie() # wywolanie matody zdefiniowanej w klasie na danym obiekcie tej klasy


# %%
Drzewo.wyswietl_info_o_drzewie(drzewo_1) # rownowazne z tym powyzej





















