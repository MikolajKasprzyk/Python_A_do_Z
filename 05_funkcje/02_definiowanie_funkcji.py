# -*- coding: utf-8 -*-

def funkcja_1():
    print('Pierwsza funkcja uruchumiona')
    
funkcja_1()
    
# %%
def funkcja_2(x, y):
    print('podane argumenty to: {0}, {1}.'.format(x, y))    
    
funkcja_2(3, 10)

# %%
def funkcja_2(x, y = 10): # przy takim zapisie domyslnie y=10, nie trzeba go podawac , ale mozna podac inne
    print('podane argumenty to: {0}, {1}.'.format(x, y))    
    
funkcja_2(2)

# %%
def funkcja_2(x = 2, y = 10): # przy takim zapisie domyslnie y=10,x=2, nie trzeba go podawac , ale mozna podac inne
    print('podane argumenty to: {0}, {1}.'.format(x, y))    
    
funkcja_2() # jak wszystkie argumenty sa domyslne mozna wywolac funkcje bez zadnych
funkcja_2(y=1, x=4) # takie wywolanie tez jest mozliwe z inna kolejnoscia argumentow


# %%
import math # import biblioteki math, w ktorej jest funkcja pierwiastka

math.sqrt(2) # wywolanie funkcji z biblioteki math

math.exp(2) # funkcja eksponencjalna

math.sin(0)

#%%
def funkcja_3():
    print('uruchomiono')
funkcja_3()

# %%
def add(x, y):
    return x + y # tak definiujemy wartosc ktora funkcja ma zwrocic

reslt = add(2, 4)

# %%
def substract(x: int, y: int):
    """
    odejmuje od siebie 2 liczby
    """
    return x - y

substract(10,5)

# %%
def print_menu():
    print('Strat programu...')
    print('*' * 30)
    print("""Wybierz jedna z podanych opcji
          0 - logowanie
          1 - wyjscie""")
    print('*' * 30)
    print('Koniec programu')
    
print_menu()

# %%
def srednia(x, y, z):
    return (x + y + z)/3

srednia(1,2,3)

# %%
def print_even(maximum):
    for i in range(maximum + 1): # liczba 'maximum' tez jest w iteracji
        if i % 2 == 0:
            print(i)

print_even(20)
# %%
def print_even(maximum):
    even = []
    for i in range(maximum + 1): # liczba 'maximum' tez jest w iteracji
        if i % 2 == 0:
            even.append(i)
    return even

lista = print_even(20)

# %%
def text_to_file(): # funkcja w zadanym pliku dopisuje kolejne linijki tekstu
    file_name = input('Podaj nazwe pliku:  ')
    with open('{}.txt'.format(file_name), 'a') as my_file: # tu mozna wpisac open(file_name, 'a') tez dziala jak rozumiem domyslnie tworzy plik typu "file"
        #string = input('Podaj tekst do pliku:  ')
        my_file.writelines(string + '\n') # lub: print(string, file = my_file)
        
text_to_file()
    
# %%
def text_to_file(file_name): # funkcja w zadanym pliku dopisuje kolejne linijki tekstu
    with open(file_name, 'w') as my_file:
        print('Podaj tekst do pliku, 3 linijki:  ')
        line_1 = input()
        line_2 = input()
        line_3 = input()
        my_file.writelines([line_1 + '\n', line_2 + '\n', line_3 + '\n'])
        
text_to_file('3linijki')

# %%
def lines_till_z(file_name):
    i = ' '
    with open(file_name, 'w') as lines:  # zapisuje kolejne linijki do pliku poki nie wpiszemy 'z'
        while i not in 'z':
            i = input()
            lines.write(i + '\n') 
            
lines_till_z('lines_till_z.txt')

# %%
def lines_till_z(file_name):
    i = ' '
    with open(file_name, 'w') as lines: # tu podobnie tyle ze nie wpisuje do pliku 'z' konczacego program
        while i not in 'z':
            i = input()
            if i not in 'z':
                lines.write(i + '\n')
                
            
lines_till_z('lines_till_z.txt')

# %%
def lokata_zysk(stopa = 0.02, okresy = 1, kwota = 100): # podane domyslne wartosci, mozna nie trzeba ich podawac
    return kwota*(1+stopa)**okresy - kwota

lokata_zysk(okresy = 12) # tak wywolujemy funkcje z domyslnymi argumentami jesli chcemy zmienic tylko jeden
    
# %%
#zadanie napisz funkcje drukujaca liczby nieparzyste od 0 do 20

def uneven(maximum):
    lista = []    
    for i in range(maximum):
        if i % 2:
            lista.append(i)
    return lista

print(uneven(20))
nieparzyste = uneven(20)
    