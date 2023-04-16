# -*- coding: utf-8 -*-

import datetime
import time

def log(message): # funkcja zwaraca nam wiadomosc z domyslnym timestam, data i czas pozyskane ponizej
    print(datetime.datetime.utcnow().strftime("%d/%m/%Y, %H:%M:%S"), message)  # strftime - robi sformato wg zyczen string z podanego czasu, tu uzyte zeby pozbyc sie mikrosekund
    
log('uruchomienie systemu')

# %%
def logi(*args):
    for command in args:
        log(command)
        time.sleep(1) # czeka 1 s imitujac ze program cos robi
        
        
logi('uruchomienie systemu', 'logowanie', 'restart', 'wylogowanie', 'wysranie',
     'wyjebanie')








    
    