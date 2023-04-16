# -*- coding: utf-8 -*-
# %%
text = 'Python jest wspaniały. python jest elastyczny. Python rządzi.'

words = text.lower().replace('.', '').split()

unique_words = {word for word in words}  # tworzy wzor, czyli oddaje tylko unikalne wartosci
print(unique_words)

unique_words_gt_4 = {word for word in words if len(word) > 4} # unikatowe wartosci, tylko slowa dluzsze niz 4 znaki

# %%
{word.capitalize() if word.startswith('pyt') else word for word in words}  # robi duza litere jesli slowow zaczyna sie od 'pyt'

# %%
# zadanie: z podanego tekstu stworz zbior zawierajacy unikalne znaki bez spacji, wydrukuj liczbe unikalnych znakow

text = 'python jest popularny w uczeniu maszynowym'

print(len({char for char in text if char != ' '}))



































