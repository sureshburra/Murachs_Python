# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 15:52:08 2025

@author: suresh.burra
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y,width=0.5,color="red")
#plt.barh(x,y) # Draws horizontal chart instead of vertical chart
plt.show()