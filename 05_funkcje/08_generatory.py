# -*- coding: utf-8 -*-

def generator():
    
    yield 4             # ta komenda robi nam generator
    yield 5
    
gen = generator()

# %%
next(gen) wywoluje kolejny element w generatorze

# %%
def generator_2 (word):
    letters = list(word)
    for letter in letters:
        yield letter
        
gen_2 = generator_2('python')

# %%
next(gen_2)

# %%

for item in generator_2('predator'):
    print(item)
    
# %%
files = ['script_1.py', 'script_2.py', 'text.txt']

def gen_files(lista):
    for item in lista:
        if item.endswith('.py'):
            yield item
            
gen = gen_files(files)

# %%
next(gen)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
