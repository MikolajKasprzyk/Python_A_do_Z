# -*- coding: utf-8 -*-

i = 2
j = i
i = 3

# %%
a = 5

def fun_1():
    a = 4
    print(a)
    
fun_1()    
# po wykonaniu tej funkcji a nadal jest rowne 5 bo zostalo zdefiniowane globalnie, funkcja jej nie napisuje

# %%
def fun_3():
    x = 4
    print(x)

fun_3()
print(x) # to nie zadziala bo x jest zdefiniowany jedynie w srodku funkcji

# %%
tech = 'Python'

def change_tech(new_tech):
    tech = new_tech  # w taki sposob nie zmieni sie zmiennej globalnej w funkcji
    
print(tech)
change_tech('java')
print(tech)

# %%
tech = 'Python'

def change_tech(new_tech):
    global tech             # zeby zmienic zmienna globalna w funkcji trzeba dodac ze to zmienna globalna
    tech = new_tech  
    
print(tech)
change_tech('java')
print(tech)

# %%
level = 0

def f_1():
    level = 1
    
    def f_2():
        level = 2
        print('funkcja f2:  ', level)
    
    f_2()
    print('funkcja f_1', level)

f_1()
print('globalnie:   ', level)
    
    

# %%
level = 0

def f_1():
    level = 1
    
    def f_2():
        nonlocal level  # wyrzuca zmienna poziom wyzej
        level = 2
        print('funkcja f2:  ', level)
    
    f_2()
    print('funkcja f_1', level)

f_1()
print('globalnie:   ', level)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    