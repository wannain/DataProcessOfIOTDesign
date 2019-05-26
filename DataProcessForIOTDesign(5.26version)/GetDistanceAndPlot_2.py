#coding:UTF-8

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math as math

Power = [[],[],[]]#三个节点各自的Power列表
Distance = []#三个节点各自的距离计算值
DistanceTrue = [1.65,1.05,1.85]#三个节点各自的距离实际值

#下面读取文件
count = 0
with open('D:/1文件\综合课程设计（物联网）/室外三点定位数据/第二组1号1.65m.txt') as f:
    line = f.readline()
    while(1):
        line = f.readline()
        if(len(line.strip())):
            if(line.strip().split()[0][0] == '0'):#读到了有值的行
                if(count == 0):
                    count = 1
                else:
                    number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
                    number = ''.join(number)
                    number = int(number,16)
                    if(number>127):
                        number = -(255-number)#计算出功率值
                    Power[0].append(number)
                    count = 0
        else:
            break

count = 0
with open('D:/1文件\综合课程设计（物联网）/室外三点定位数据/第二组2号1.05m.txt') as f:
    line = f.readline()
    while(1):
        line = f.readline()
        if(len(line.strip())):
            if(line.strip().split()[0][0] == '0'):#读到了有值的行
                if(count == 0):
                    count = 1
                else:
                    number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
                    number = ''.join(number)
                    number = int(number,16)
                    if(number>127):
                        number = -(255-number)#计算出功率值
                    Power[1].append(number)
                    count = 0
        else:
            break
        
count = 0
with open('D:/1文件\综合课程设计（物联网）/室外三点定位数据/第二组3号1.85m.txt') as f:
    line = f.readline()
    while(1):
        line = f.readline()
        if(len(line.strip())):
            if(line.strip().split()[0][0] == '0'):#读到了有值的行
                if(count == 0):
                    count = 1
                else:
                    number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
                    number = ''.join(number)
                    number = int(number,16)
                    if(number>127):
                        number = -(255-number)#计算出功率值
                    Power[2].append(number)
                    count = 0
        else:
            break


#剔除坏值
flag = [0,0,0]#等于零的时候说明一遍循环没有提出任何值，可以退出
while(1):
    Std = []#标准差
    Mean = []#平均值
    i = 0
    while(i != 3):
        Std.append(np.std(Power[i],ddof = 1))
        Mean.append(np.mean(Power[i]))
        i = i+1
    i = 0
    while(i != 3):
        for power in Power[i]:
            if (power<Mean[i]-3*Std[i])|(power>Mean[i]+3*Std[i]):
                Power[i].remove(power)#删除该值
                flag[i] = 1
        i = i+1
    if(flag[0]|flag[1]|flag[2] == 0):#没有删除任何值
        break
    flag = [0,0,0,0,0,0,0]

#计算距离
Mean = [np.mean(Power[0]),np.mean(Power[1]),np.mean(Power[2])]
def f_1(y):
    return math.pow(10, ((-(y-0.6666666-1.8211950340938086)*0.1)/1.9528489050015256))
def f_2(y):
    return math.pow(10, ((-(y-2.388888888889+0.0809106069311949)*0.1)/2.116688918504656))
def f_3(y):
    return math.pow(10, ((-(y-3.7333333333333334+13.005376454596494)*0.1)/4.711102193110631))

Distance = [f_1(Mean[0]),f_2(Mean[1]),f_3(Mean[2])]

#画图
point = [[0,0],[2.5,0],[1.046,2.21548]]#三个点坐标


axes = plt.gca()
axes.cla()

plt.scatter(point[0][0],point[0][1],10,"black")
plt.scatter(point[1][0],point[1][1],10,"black")
plt.scatter(point[2][0],point[2][1],10,"black")

circle1 = plt.Circle(point[0],Distance[0],color ='red',fill=False)
circle2 = plt.Circle(point[1],Distance[1],color ='red',fill=False)
circle3 = plt.Circle(point[2],Distance[2],color ='red',fill=False)
circle4 = plt.Circle(point[0],DistanceTrue[0],color ='black',fill=False)
circle5 = plt.Circle(point[1],DistanceTrue[1],color ='black',fill=False)
circle6 = plt.Circle(point[2],DistanceTrue[2],color ='black',fill=False)


axes.add_artist(circle1)
axes.add_artist(circle2)
axes.add_artist(circle3)
axes.add_artist(circle4)
axes.add_artist(circle5)
axes.add_artist(circle6)
plt.xticks(np.arange(-4,5))
plt.yticks(np.arange(-4,6))

plt.show()