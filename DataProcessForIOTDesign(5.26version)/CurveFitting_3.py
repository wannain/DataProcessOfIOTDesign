#coding:UTF-8

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math as math
from sympy.core.tests.test_sympify import numpy

Distance = [0.3,0.5,1,2,3,4,6,8]#距离的种类
Number = [0,0,0,0,0,0,0,0]#每种距离作为横坐标时需要的数量
Power = [[],[],[],[],[],[],[],[]]#计算功率值，按照距离分块存储
PowerAll = []#最终的所有的power，用于拟合曲线
DistanceAll = []#最终所有的距离，用于拟合曲线

#读取文件并计算功率存入list
count = 0#用于标记当前的十六进制是否有效
i = 0
with open('D:/1文件\综合课程设计（物联网）/室外测量拟合结果/节点3号/三号节点数据.txt') as f:
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
                    Number[i] = Number[i]+1#功率对应的距离数加一
                    Power[i].append(number)
                    count = 0
        else:
            line = f.readline()
            #n=n+1
            #print(n)
            if(line):
                i = i+1
            else:
                break
            
#下面开始剔除每一组的坏值
flag = [0,0,0,0,0,0,0,0]#等于零的时候说明一遍循环没有提出任何值，可以退出
while(1):
    Std = []#标准差
    Mean = []#平均值
    i = 0
    while(i != 8):
        Std.append(np.std(Power[i],ddof = 1))
        Mean.append(np.mean(Power[i]))
        i = i+1
    i = 0
    while(i != 8):
        for power in Power[i]:
            if (power<Mean[i]-3*Std[i])|(power>Mean[i]+3*Std[i]):
                Power[i].remove(power)#删除该值
                Number[i] = Number[i]-1
                flag[i] = 1
        i = i+1
    if(flag[0]|flag[1]|flag[2]|flag[3]|flag[4]|flag[5]|flag[6]|flag[7] == 0):#没有删除任何值
        break
    flag = [0,0,0,0,0,0,0,0]

#拟合曲线
P_0 = np.mean(Power[2])
DistanceAll = [0.3 for i in range(Number[0])]+[0.5 for i in range(Number[1])]+[1 for i in range(Number[2])]+[2 for i in range(Number[3])]+[3 for i in range(Number[4])]+[4 for i in range(Number[5])]+[6 for i in range(Number[6])]+[8 for i in range(Number[7])]
PowerAll = Power[0]+Power[1]+Power[2]+Power[3]+Power[4]+Power[5]+Power[6]+Power[7]
def func(x,a,b):
    y = P_0-10*a*(np.log10(x))+b
    return y

plt.scatter(DistanceAll[:],PowerAll[:],1,"black")
#非线性最小二乘法拟合
result = curve_fit(func, DistanceAll, PowerAll)
a = result[0][0]
b = result[0][1]
print(a,b)
#获取popt里面是拟合系数
x = np.arange(-1,10,0.01)
y = P_0-10*a*(np.log10(x))+b
plt.plot(x,y,"red")
plt.show()
print(P_0)