# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np

def split_data(x, y, ratio, seed=1):
    """split the dataset based on the split ratio."""
    np.random.seed(seed)
    
    np.random.shuffle(x)
    np.random.shuffle(y)
    
    stop_idx = int(len(x) * ratio)
    return x[:stop_idx], y[:stop_idx], x[stop_idx:], y[stop_idx:]