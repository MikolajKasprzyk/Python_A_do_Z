# -*- coding: utf-8 -*-

"""
Tworzenie testu jednostkowego:
    1. zaimportowanie unittest
    2. zdefiniowanie funkcji do testowania
    3. stworzenie przypadku testowego uzywajac klasy unittest.TestCase
    4. zdefiniowanie testu jako metody klasy TestCase
    5. call assert function
    6. assert function wywola błąd assertionError jezeli otrzymamy bląd
    7. wywolaj funkcje main() z modulu unittest
    
"""

import unittest

def add(x,y):
    return x + y


class SimpleTest(unittest.TestCase):
    
    def test_add(self):         #metody MUSZA zaczynac sie od 'test'
        self.assertEqual(add(3,4), 7, msg = 'powinno byc 7')
        
        
if __name__ == "__main__":
    unittest.main()