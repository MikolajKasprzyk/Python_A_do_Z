# -*- coding: utf-8 -*-

# konstruktor to metoda ktora uruchami sie przy utworzeniu obiektu danej klasy,
# pozwala nam przekazac atrybuty podczas twiorzenia obiektu


class Drzewo:

    def __init__ (self, nazwa, wiek, wysokosc): #tak zawsze definiuje sie konstruktor
        self.nazwa = nazwa
        self.wiek = wiek
        self.wysokosc = wysokosc
        
    def czy_chronione(self):
        if self.wiek >= 20 and self.wysokosc >= 20:
            print(f'Drzewo o nazwie {self.nazwa} jest pod ochroną.')
        else:
            print(f'Drzewo o nazwie {self.nazwa} nie jest chronione.')

    def postarz_o_rok(self):
        self.wiek +=1
        
# %%
drzewo_1 = Drzewo('sosna', 120, 35) # przy tworzeniu obiektu musimy podac atrybuty, jesli nie ma podanych domyslnych w konstruktorze klasy
drzewo_2 = Drzewo('brzoza', 21, 10)

drzewo_1.czy_chronione()
drzewo_2.czy_chronione()

drzewo_1.postarz_o_rok()



# %%
class Drzewo_def:

    def __init__ (self, nazwa = 'sosna', wiek = 10, wysokosc = 10): # mozna podac wartosci domyslne dla atrybutow
        self.nazwa = nazwa
        self.wiek = wiek
        self.wysokosc = wysokosc
        
# %%
drzewo_def__2 = Drzewo_def() # jesli w konstruktorze klasy mamy podane domyslne atrybuty mie musimy ich podawac przy tworzeniu obiektu


















    