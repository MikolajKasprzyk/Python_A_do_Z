# -*- coding: utf-8 -*-

class Czlowiek:
    
    pochodzenie = 'Ziemia'
    imie = 'Jack'

class Polak:
    
    kraj = 'Polska'
    imie = 'Piotr'


class Pilkarz(Czlowiek, Polak): # wazna jest kolejnosc dziedziczenia - dziedziczy od klasy podanej najpierw
    
    def info(self):
        print(f'utworzony obiekt pochodzi z {self.pochodzenie}.\n'
              f'Kraj pochodzenia {self.kraj}.\n'
              f'Nazwa obiektu {self.imie}.')
        
# %%
pilkarz_1 = Pilkarz()
pilkarz_1.info()

# %%

class A:
    
    def metoda(self):
        print('metoda klasy A')


class B(A):
    
    pass
    # def metoda(self):
    #     print('metoda klasy B')


class C(A):
    
    pass
    # def metoda(self):
    #     print('metoda klasy C')


class D(B, C):
    
    
    pass
    # def metoda(self):
    #     print('metoda klasy D')
        

# %%
d = D()
d.metoda()


















    