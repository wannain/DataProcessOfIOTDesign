#coding:UTF-8

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math as math

distance = [0.3,0.5,1,2,3,4,6,8]#距离种类
Number = [0,0,0,0,0,0,0,0]#对应距离多少数据
i=0#指向距离list的下标
d = []#横坐标
power = []#纵坐标
count = 0#读到的是无用的

with open('D:/1文件\综合课程设计（物联网）/室外测量拟合结果/节点3号/三号节点数据.txt') as f:
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
                    Number[i] = Number[i]+1
                    power.append(number)
                    count = 0
        else:
            line = f.readline()
            #n=n+1
            #print(n)
            if(line):
                i = i+1
            else:
                break


d = [0.3 for i in range(Number[0])]+[0.5 for i in range(Number[1])]+[1 for i in range(Number[2])]+[2 for i in range(Number[3])]+[3 for i in range(Number[4])]+[4 for i in range(Number[5])]+[6 for i in range(Number[6])]+[8 for i in range(Number[7])]

def func(x,a,b):
    y = -4.571428571428571-10*a*(np.log10(x))+b
    return y

plt.scatter(d[:],power[:],1,"black")
#非线性最小二乘法拟合
result = curve_fit(func, d, power)
a = result[0][0]
b = result[0][1]
print(a,b)
#获取popt里面是拟合系数
x = np.arange(0,8,0.01)
y = -4.571428571428571-10*a*(np.log10(x))+b
plt.plot(x,y,"red")
plt.show()
'''
a = popt[0]
b = popt[1]
yvals = func(d,a,b) #拟合y值
print('popt:', popt)
print('系数a:', a)
print('系数b:', b)
print('系数pcov:', pcov)
print('系数yvals:', yvals)
#绘图
plot1 = plt.plot(d, y, 's',label='original values')
plot2 = plt.plot(d, yvals, 'r',label='polyfit values')
plt.xlabel('d')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('curve_fit')
plt.show()
'''
                