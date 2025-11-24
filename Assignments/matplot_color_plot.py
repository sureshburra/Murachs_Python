# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 16:06:05 2025

@author: suresh.burra
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(['a','b','c','d','e','f','g','h','i','j','k','l','m'])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
 
colors = ["red", "green", "blue", "orange", "purple", "cyan",
          "magenta", "yellow", "brown", "pink", "lime", "teal", "gray"]
 
plt.bar(x, y, color=colors, edgecolor="black")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart Example")
 
plt.xticks(rotation=45)
plt.show()