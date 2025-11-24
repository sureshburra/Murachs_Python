# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 15:39:57 2025

@author: suresh.burra
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x,y)

# Plot 2:
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()
