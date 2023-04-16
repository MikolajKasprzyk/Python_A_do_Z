# -*- coding: utf-8 -*-

def add(x, y):  # w dokumentacji zapis testu funkcji/ przykladu wywolania:
                #>>> nazwa_funkcji(argumenty)
                #oczekiwany_wynik
    """
    Zwraca sume dwoch liczb
    
    >>> add(3, 4)
    7
    
    >>> add(2, 8)
    10
    """
    return x + y

if __name__ == '__main__':
    import doctest
   # doctest.testmod() # tak sie wywoluje sprawdzenie czy przyklady podane w dokumentacji sa poprawne
    doctest.testfile('test.txt') # tak wywolujemy testy z pliku