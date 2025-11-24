# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([0,6])
ypoints = np.array([0,250])

#plt.plot(xpoints,ypoints,marker='o')
plt.title("Sports Watch Data")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.plot(xpoints,ypoints,linestyle='dotted')
plt.grid()
# plt.plot(ypoints, marker='o')
plt.show()