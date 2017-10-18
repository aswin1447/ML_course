# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""
    lambda_prime = lambda_ / (2*tx.shape[0])
    a = np.linalg.inv(tx.transpose().dot(tx) + lambda_*np.eye(tx.shape[1]))
    
    b = tx.transpose().dot(y)
    w_star = a.dot(b)
    
    e = y - tx.dot(w_star)
    
    mse = np.asarray((e**2).mean())
    return mse, w_star
