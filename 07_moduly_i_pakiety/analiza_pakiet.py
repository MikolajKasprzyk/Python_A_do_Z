# -*- coding: utf-8 -*-

import rocket.data  # tak importujemy caly modul

# %%
dir(rocket.data)

# %%
dane = rocket.data.get_data()

# %%
import rocket.algorytmy

dir(rocket.algorytmy)

# %%
rocket.algorytmy.drzewa_decyzyjne()


# %%
from rocket.algorytmy import drzewa_decyzyjne   # importujemy tylko jedna funkcje, mozna ja wywlolac bezposredio

drzewa_decyzyjne()

# %%
from rocket.funkcje.stats import mean   # import funkcji z zagniezdzonego glebiej modulu

mean(dane)

# aby pakiet ladowal sie niezaleznie od lokalizacji trzeba go zainstalowac w srodowisku w ktorym pracujemy






















