# -*- coding: utf-8 -*-

import sys


def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)
    

if __name__ == '__main__':              # to sie wykonuje tylko kieyd nasz plik jest uruchamiany bezposrednio
    print(silnia(int(sys.argv[1])))    # liczy silnie dla podanego przy wywolaniu komendy z argumentem
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    