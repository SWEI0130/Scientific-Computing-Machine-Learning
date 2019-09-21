# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 08:25:52 2019

@author: SWEI
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import numpy as np
x = np.arange(-5., 5., 0.2)
plt.plot(x, (np.sin(x)-x**2), "r--", x, 0/x, "g--")
plt.show()
