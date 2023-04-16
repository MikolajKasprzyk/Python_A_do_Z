# -*- coding: utf-8 -*-

"""
assertListEqual - sprawdza czy listy sa rowne
assertTupleEqual - sprawdza czy tuple sa rowne
assertSetEqual - sprawdza czy zbiory sa rowne
assertDictEqual - sprawdza czy slowniki sa rowne

"""

import unittest


class SimpleTest(unittest.TestCase):
    
    def test_1(self):
        self.assertListEqual([1, 2, 4], [1, 2, 3])  


    def test_2(self):
        self.assertTupleEqual((1, 2), (1, 3)) 


    def test_3(self):
        self.assertSetEqual({4, 5}, {5, 4}) 


    def test_4(self):
        self.assertDictEqual({'a': 1, 'b': 2}, {'a': 1, 'b': 2}) 


if __name__ == '__main__':
    unittest.main()



















































