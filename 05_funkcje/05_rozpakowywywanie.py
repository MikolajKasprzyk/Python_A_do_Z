# -*- coding: utf-8 -*-

def test_args(x, *args): # zdefiniowany 1 argument, reszta argumentow w dowolnej liczbie, mozna po nich iterowac
    print('argument nr: 1   -  ', x)
    i =2
    for arg in args:
        print('argument nr: {}   -  '.format(i), arg)
        i += 1
        
        
test_args(1, 2, 3, 4, 'dupa') # piewszy argument jest obowiazkowy reszta opcjonalna  

# %%
def funkcja_1(x, y, *args):
    print('x=', x, '\n', 'y=', y, '\n', '*args=', args)
    
funkcja_1(1, 2, 3, 4, 5, 6, 7, 8) # tworzy tuple z reszta argumentow

# %%
def suma(x, y):     # to dziala tylko dla 2 argumentow
    return x + y

suma(1,2)
    
# %%
def suma(*args):    # to dziala dla dowolnej liczby argumentow
    return sum(args)

suma(1,2,3,4,5,6,7)    

# %%
def srednia(*args):
    return sum(args)/len(args)
    
srednia(1,2)

# %%
# argumenty z nazwa
def funkcja_2(**kwargs):
    for kwarg in kwargs:
        print(kwarg)

funkcja_2(**{'a': 1, 'b': 2})
    
# %%
def fun(**kwargs):
    print(kwargs)

fun(a=1, b=2)
fun(x1=10, x2=20, x3=30)
    
# %%
def fun_2(*args, **kwargs):
    print(args)
    print(kwargs)
    
fun_2(1, 2, 3, a=10, b=12)
    
# %%
def fun_3(*args, **kwargs):
    print(sum(args))
    print(kwargs.values())
    
fun_3(1, 2, 3, a=10, b=12)
    
# %%
# zadanie: napisz funkcje ktora zwroci ilosc podanych argumentow
    
def policz_kwargs(*args,**kwargs):
    return len(kwargs)
    
policz_kwargs(10, a=10, b=20, c=40, d=30)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    