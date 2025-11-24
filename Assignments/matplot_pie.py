# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 16:07:21 2025

@author: suresh.burra
"""

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabels=["Bananas","Apples","Grapes","Mangoes"]
myexplode = [0.2,0.1,0.1,0]

plt.pie(y, labels=mylabels,startangle=90,explode=myexplode)
plt.show()