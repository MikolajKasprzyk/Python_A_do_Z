# -*- coding: utf-8 -*-

# public: zmienna - dostepna z poziomu klasy, jej pochodnych i wszedzie poza klasa pochodna
# protected: _zmienna - dostepna z poziomu klasy i klasy pochodnej
# private: __zmienna - dostepna tylko z poziomu definiowanej klasy

# %%

class Spolka:
    
    def __init__(self, rodzaj, rynek, gielda):
        self.rodzaj = rodzaj
        self._rynek = rynek
        self.__gielda = gielda
        
    
class KGHM(Spolka):
    
    def __init__(self, rodzaj, rynek, gielda, nazwa):
        super().__init__(rodzaj, rynek, gielda)
        self.nazwa = nazwa
        print(f'Atrybut publiczny: {self.rodzaj}')
        print(f'Atrybut chroniony: {self._rynek}')
        #print(f'Atrybut prywatny: {self.__gielda}') # atrybutu prywatnego nie wyciagniemy w taki sposob
        
# %%
spolka = Spolka('Spolka Akcyjna', 'Główny', 'GPW w Warszawie')
print(f'Atrybut publiczny: {spolka.rodzaj}')
print(f'Atrybut chroniony: {spolka._rynek}')
# print(f'Atrybut prywatny: {spolka.__gielda}') # tu zwroci blad ze niby nie ma zmiennej 

# %%
kghm = KGHM('Spolka Akcyjna', 'Główny', 'GPW w Warszawie', 'KGHM')

print(f'Atrybut prywatny: {kghm._Spolka__gielda}')  # to jest sposob na dostanie do zmiennej prywatnej


























