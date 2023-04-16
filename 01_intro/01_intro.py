# -*- coding: utf-8 -*-
# komentarz

# %%
print(2 + 2)

# %%
print(3 * 3)

# %%
print(3 + 2 *2 )
4 - 2 * 2

#%%
10 / 3

# %%
7 // 6

# %%
2 ** 5

# %%
10 % 3
12 % 5

# %%
(10 - 2 ** 3) * 10
 
# %%
a = 10
b = 20

c = a * b
print(c)

# %%
print('love python')
"love python"

# %%
# "It's the best"
'It\'s the best'

# %%
print('Python 3.7')
print('Python\n3.7')


# %%
print("""Python
      3.7""")

# %%
print('\tPython')      
print('\t\t\tPython')
# print('C:\path\to\something\new')
print('C:\path\\to\something\\new') # bacslash przed znakiem 'usuwa'jegodzialanie i jest printowany jako litera/znak a nie robi nowa linie itp
print(r'C:\path\to\something\new')   # litera r przed nazwa informuje ze to sam tekt (backslashe uznawane za litery a nie znaki nowej linii itp)


# %%
import os  # biblioteka wbudowana 
os.getcwd() # zwaraca sciezke do folderu domowego

# %%
print("""
Instrukcja uruchamiania pliku przyklad.py:

        --file [nazwa pliku]
            zapisuje output do pliku
        
        --quiet
            wycisza logi w konsoli
            
Koniec.""")
      
# %%
text = 'I love Python. '
print(text)
print(text * 3)      
print('hau...'*10)
print('*' * 20)

'Python'
'Py' 'thon'

# %%
url = 'https://www.anaconda.com/products/distribution/installation-successhttps://www.anaconda.com/products/distribution/installation-success'      
url = ('https://www.anaconda.com/products/distribution/installation-success'    # lamanie linijki zeby nie byla za dluga w kodzie
       'https://www.anaconda.com/products/distribution/installation-success')
print(url) 
     

# %%
name = 'Python'
print(name + '3.7')
print(name, '3.7')  # dodaje spacje

# %%
age = 27
imie = 'Paweł'

# print(imie + wiek) # to nie dziala bo nie dodaje sie stringa z liczba
#print(imie, str(age))   #zamiana liczby na string
print(imie, age)
print('{} ma {} lat.'.format(imie, age))
print('{1} ma {0} lat.'.format(imie, age))


# %%
saldo = 40
saldo = saldo + 30
saldo += 20
saldo -= 10
print(saldo)
      
# %%
lokata = 1000
czynnik_akumulacyjny = 1 + 0.04
lokata_po_roku = lokata * czynnik_akumulacyjny  
print(lokata_po_roku)    

# %%
pixel = 150
pixel = pixel / 255 # ustandaryzowana wartosc pixela
pixel /= 255
print(pixel)    

# %%
x = 103
x %= 10
print(x)

# %%
imie = 'Pawel'
nazwisko = 'Krakowiak'
nazwa = imie + nazwisko
print(nazwa)

imie += nazwisko
print(imie)

# %%
name = 'Ptyhon '
wersja = '3.7'
name += wersja
print(name)

# %%

    
    
      
      
      
      
      
      
      
      
      