# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:37:38 2019

@author: SWEI
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(3., 7., 0.2)
plt.plot(x, -2+6*x-4*x**2+0.5*x*x*x,"r--", x, 0/x, "g--")
plt.show()