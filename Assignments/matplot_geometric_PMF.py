# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 10:38:43 2025

@author: suresh.burra
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom
 
# Parameters
p = 0.3   # success probability
x = np.arange(1, 15)  # support of geometric distribution (starts from 1)
 
# PMF and CDF
pmf = geom.pmf(x, p)
cdf = geom.cdf(x, p)
 
# Plotting
plt.figure(figsize=(12, 5))
 
# PMF
plt.subplot(1, 2, 1)
plt.stem(x, pmf)
plt.title(f'Geometric PMF (p={p})')
plt.xlabel('x')
plt.ylabel('P(X=x)')
 
# CDF
plt.subplot(1, 2, 2)
plt.step(x, cdf, where='post')
plt.title(f'Geometric CDF (p={p})')
plt.xlabel('x')
plt.ylabel('P(X ≤ x)')
 
plt.tight_layout()
plt.show()