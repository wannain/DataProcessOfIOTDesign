#coding:UTF-8

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math as math
from numpy.core._multiarray_umath import power

with open('D:/1文件/综合课程设计（物联网）/0.3m基准.txt') as f:
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()#第一个有效的RSSI
    number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
    number = ''.join(number)
    number = int(number,16)
    if(number>127):
        number = -(255-number)
    #转成10进制字符串
    #print(number)
    ListOfPower_0_3 = [number]
    while line:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        if(line):
            number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
            number = ''.join(number)
            number = int(number,16)
            if(number>127):
                number = -(255-number)
            ListOfPower_0_3.append(number)
    len_0_3 = len(ListOfPower_0_3)
            

with open('D:/1文件/综合课程设计（物联网）/0.5m基准.txt') as f:
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()#第一个有效的RSSI
    number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
    number = ''.join(number)
    number = int(number,16)
    if(number>127):
        number = -(255-number)
    #转成10进制字符串
    #print(number)
    ListOfPower_0_5 = [number]
    while line:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        if(line):
            number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
            number = ''.join(number)
            number = int(number,16)
            if(number>127):
                number = -(255-number)
            ListOfPower_0_5.append(number)
    len_0_5 = len(ListOfPower_0_5)
            
with open('D:/1文件/综合课程设计（物联网）/1m基准.txt') as f:
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()#第一个有效的RSSI
    number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
    number = ''.join(number)
    number = int(number,16)
    if(number>127):
        number = -(255-number)
    #转成10进制字符串
    #print(number)
    ListOfPower_1 = [number]
    while line:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        if(line):
            number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
            number = ''.join(number)
            number = int(number,16)
            if(number>127):
                number = -(255-number)
            ListOfPower_1.append(number)
    len_1 = len(ListOfPower_1)

with open('D:/1文件/综合课程设计（物联网）/2m基准.txt') as f:
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()#第一个有效的RSSI
    number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
    number = ''.join(number)
    number = int(number,16)
    if(number>127):
        number = -(255-number)
    #转成10进制字符串
    #print(number)
    ListOfPower_2 = [number]
    while line:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        if(line):
            number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
            number = ''.join(number)
            number = int(number,16)
            if(number>127):
                number = -(255-number)
            ListOfPower_2.append(number)
    len_2 = len(ListOfPower_2)

with open('D:/1文件/综合课程设计（物联网）/3m基准.txt') as f:
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()#第一个有效的RSSI
    number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
    number = ''.join(number)
    number = int(number,16)
    if(number>127):
        number = -(255-number)
    #转成10进制字符串
    #print(number)
    ListOfPower_3 = [number]
    while line:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        if(line):
            number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
            number = ''.join(number)
            number = int(number,16)
            if(number>127):
                number = -(255-number)
            ListOfPower_3.append(number)
    len_3 = len(ListOfPower_3)

with open('D:/1文件/综合课程设计（物联网）/4m基准.txt') as f:
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()#第一个有效的RSSI
    number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
    number = ''.join(number)
    number = int(number,16)
    if(number>127):
        number = -(255-number)
    #转成10进制字符串
    #print(number)
    ListOfPower_4 = [number]
    while line:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        if(line):
            number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
            number = ''.join(number)
            number = int(number,16)
            if(number>127):
                number = -(255-number)
            ListOfPower_4.append(number)
    len_4 = len(ListOfPower_4)
            
with open('D:/1文件/综合课程设计（物联网）/6m基准.txt') as f:
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()#第一个有效的RSSI
    number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
    number = ''.join(number)
    number = int(number,16)
    if(number>127):
        number = -(255-number)
    #转成10进制字符串
    #print(number)
    ListOfPower_6 = [number]
    while line:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        if(line):
            number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
            number = ''.join(number)
            number = int(number,16)
            if(number>127):
                number = -(255-number)
            ListOfPower_6.append(number)
    len_6 = len(ListOfPower_6)

power = ListOfPower_0_3+ListOfPower_0_5+ListOfPower_1+ListOfPower_2+ListOfPower_3+ListOfPower_4+ListOfPower_6#所有数据汇总

#设置自变量
d = [0.3 for i in range(len(ListOfPower_0_3))]+[0.5 for i in range(len(ListOfPower_0_5))]+[1 for i in range(len(ListOfPower_1))]+[2 for i in range(len(ListOfPower_2))]+[3 for i in range(len(ListOfPower_3))]+[4 for i in range(len(ListOfPower_4))]+[6 for i in range(len(ListOfPower_6))]


#定义函数
def func(x,a,b):
    y = -4.571428571428571-10*a*(np.log10(x))+b
    return y

plt.scatter(d[:],power[:],25,"black")
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
