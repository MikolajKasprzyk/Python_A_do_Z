# -*- coding: utf-8 -*-

# continue pomija jedna wybrana iteracje i praechodzi do kolejnego elementu iterowalnego

# %%
for i in range(10):
    if i == 6:  # taka petla printuje wszystko poza 6
        continue  
    print(i)
    
# %%
for i in range(20):
    if i % 2 == 0:  # pomija liczby parzyste i printuje nieparzyste
        continue
    print(i)
    
# %%
for i in range(20):
    if i % 2 != 0:  # pomija liczby nieparzyste i printuje parzyste
        continue
    print(i)
    
# %%
sample = 'Python Course'
for char in sample:
    if char == ' ':  # printuje do konsoli wsztsko poza spacjami
        continue
    print(char)
    
# %%

hashtags = '#summer#holiday#free'    
result = ''
for char in hashtags:
    if char == '#':
        print(result)   # printujemy slowa bez #
        result = ''
        continue
    result = result + char
print(result)

# %%
# zadanie: podana jest lista, ponizej, wydrukuj wszystkie liczby poza 99
lista = [1, 2, 99, 4, 5]
for i in lista:
    if i == 99:
        continue
    print(i)



