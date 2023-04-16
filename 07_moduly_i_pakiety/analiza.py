# -*- coding: utf-8 -*-

import rocket_science # importuje caly modul


# %%
dir(rocket_science)

# %%
rocket_science.calculate_mean([3, 4])


rocket_science.calculate_min([1, 34, 56, 32, 12])

# %%

from rocket_science import calculate_mean  # importuje tylko potrzebna funkcje, rekomendowany sposob

calculate_mean([1, 2, 3, 5])       # jak imporujemy pojedyncza funkcje mozna ja wywolywac bez podawania nazwy modulu z ktorego pochodzi


# %%
from rocket_science import *   # to importuje nam wszystkie definicje z modułu, mozna je wywolywac bezposrednio

# %%
from rocket_science import calculate_mean, calculate_max # importuje kilka funkcji z danego modulu


































