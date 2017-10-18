# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    manifold = lambda x, degree: [x**j for j in range(0,degree)]
    poly = [manifold(val, degree) for val in x]
    return np.asarray(poly)
    
