#coding:UTF-8

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sympy import *
from scipy.optimize import fsolve
import math as math

count = 0
power = []

with open('D:/1文件/综合课程设计（物联网）/室外三点定位数据/第四组3号4.6m.txt') as f:
    line = f.readline()
    #n = 1
    while(1):
        line = f.readline()
        #n=n+1
        #print(n)
        if(len(line.strip())):
            if(line.strip().split()[0][0] == '0'):#读到了有值的行
                if(count == 0):
                    count = 1
                else:
                    number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
                    number = ''.join(number)
                    number = int(number,16)
                    if(number>127):
                        number = -(255-number)
                    power.append(number)
                    count = 0
        else:
            break

Power = np.mean(power)
print(Power)


