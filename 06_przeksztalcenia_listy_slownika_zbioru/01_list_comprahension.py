# -*- coding: utf-8 -*-

results = []

for i in range(100):
    results.append(i**2)
    
print(results)

# %%
results_2 = [i**2 for i in range(100)] # to jest rownowazne z tym co powyzej

# %%
lista = [i * 3 for i in range(100)]


# %%
results_3 = []

for i in range(100):
    if i % 5 == 0:
        results_3.append(i**2)
        
# %%
results_4 = [i**2 for i in range(100) if i  % 5 == 0] # rownowazne z tym co powyzej

# %%

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

results = []
for letter in letters:
    for number in numbers:
        results.append(letter + str(number))
        
# %%
results_2 = [letter + str(number) for letter in letters for number in numbers]


# %%
letters_1 = ['a', 'b', 'c']
letters_2 = ['a', 'b', 'c']

results_3 = [letter_1 + letter_2 for letter_1 in letters_1 
              for letter_2 in letters_2]

# %%
letters_1 = ['a', 'b', 'c']
letters_2 = ['a', 'b', 'c']

results_3 = [letter_1 + letter_2 for letter_1 in letters_1 
              for letter_2 in letters_2 if letter_1 != letter_2]

# %%
[[j for j in range(10)] for i in range(5)]

# %%
[[(i, j) for j in range(10)] for i in range(5)]

# %%
[[i * j for j in range(10)] for i in range(5)]

# %%
results_4 = []
for i in range(5):
    results_posrednie = []
    
    for j in range(10):
        results_posrednie.append(i * j)
   
    results_4 += [results_posrednie]
        
print(results_4)


# %%
[[l1 + l2 for l2 in 'abcde'] for l1 in '12345']

# %%
# TO JEST FUNKCJA ZDEFINIOWANA REKURENCYJNIE
def silnia(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * silnia(n-1)
    
# %%
[silnia(i) for i in range(10)] # tworzy liste wartosci dla danej funkcji w podanym zakresie

#%%
# zadanie: wydrukuj do konsoli liste liczb od 0 do 30 podzielnych przez 4

print([i for i in range(30) if i % 4 == 0])






























