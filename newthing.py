#/usr/bin/env python
"""This is a new file"""
"""my favorite line of python"""

import numpy as np
import matplotlib.pyplot as plt
plt.ion()
data=np.loadtxt('data/data.txt')

xx = np.arange(0,1,0.1)
plt.scatter(data[:,0],data[:,1],'*')
plt.plot(xx,xx,lw=2)
