# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    a = np.linalg.inv(tx.transpose().dot(tx))
    b = tx.transpose().dot(y)
    w_star = a.dot(b)
    
    e = y - tx.dot(w_star)
    
    mse = np.asarray((e**2).mean())
    return mse, w_star
