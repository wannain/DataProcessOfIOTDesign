#coding:UTF-8

from sympy import*
import numpy as np
import math as math
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


r1 = 5.7
r2 = 8.1
a1 = 0
b1 = 0
a2 = 3
b2 = 0
x1 = np.arange(a1-r1,a1+r1,0.01)
y1 = b1+np.sqrt(r1**2 - (x1-a1)**2)
x2 = np.arange(a2-r2,a2+r2,0.01)
y2 = b2+np.sqrt(r2**2 - (x2-a2)**2)

fig = plt.figure() 
axes = fig.add_subplot(111) 
axes.plot(x1, y1) # 上半部
axes.plot(x1, -y1) # 下半部
axes.plot(x2, y2) # 上半部
axes.plot(x2, -y2) # 下半部

plt.axis('equal')
circle1 = plt.Circle((0,0),0.9,color = 'black',fill =false)
circle2 = plt.Circle((1.2,0),1.6,color = 'black',fill = False)
axes.add_artist(circle1)
axes.add_artist(circle2)
plt.show()
