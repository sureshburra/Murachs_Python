# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 10:57:07 2025

@author: suresh.burra
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
 
# Set average rate (lambda)
mu = 5
 
# Range of events (k)
k = np.arange(0, 16)
 
# Compute PMF and CDF
pmf = poisson.pmf(k, mu)
cdf = poisson.cdf(k, mu)
 
# Plot PMF
plt.figure(figsize=(10, 4))
 
plt.subplot(1, 2, 1)
plt.stem(k, pmf, basefmt=' ')
plt.title(f'Poisson Distribution PMF (λ={mu})')
plt.xlabel('Number of Events')
plt.ylabel('P(X = k)')
plt.grid(True)

# Plot CDF
plt.subplot(1, 2, 2)
plt.step(k, cdf, where='post')
plt.title(f'Poisson Distribution CDF (λ={mu})')
plt.xlabel('Number of Events')
plt.ylabel('P(X ≤ k)')
plt.grid(True)
 
plt.tight_layout()
plt.show()