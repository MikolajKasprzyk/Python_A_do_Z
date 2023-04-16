# -*- coding: utf-8 -*-

class Czlowiek:
    
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        
    def info(self):
        print(f'{self.imie} {self.nazwisko}')
        

class Pilkarz(Czlowiek):  # tak definiujemy dziedziczenie
    
    def __init__(self, imie, nazwisko, klub):
        super().__init__(imie, nazwisko)  # wywolanie konstruktora z klasy z ktorej dziedziczymy
        self.klub = klub
        
    def info_o_zawodniku(self):
        super().info() # uruchamiajac ta metode uzyj metode info z klasy czlowiek, a potem reszte
        print(f'Klub zawodnika: {self.klub}')
        
# %%
pilkarz_1 = Pilkarz('robert', 'lewandowski', 'bayern')
pilkarz_2 = Pilkarz('krzysztof', 'piatek', 'AC Milan')

pilkarz_1.info()

pilkarz_1.info_o_zawodniku()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        