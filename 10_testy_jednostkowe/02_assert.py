# -*- coding: utf-8 -*-

assert 1 == 1

# %%
assert 1 == 2

# %%
def test_sum():
    assert sum([1, 2, 3]) == 6
    
test_sum()

# %%
def test_sum():
    assert sum([1, 2, 3]) == 6, 'informacja o bledzie'
    
test_sum()

# %%
def test_min():
    assert min([1, 2, 3]) == 1 , 'informmacja o bledzie'
    
# %%
if __name__ == '__main__':
    test_sum()
    test_min()
    print('Wszystko ok')




















