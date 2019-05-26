#coding:UTF-8

import numpy as np

with open('D:/1文件/综合课程设计（物联网）/1m基准.txt') as f:
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    number = ['0x',line.strip().split()[0][2],line.strip().split()[0][3]]
    number = ''.join(number)
    number = int(number,16)
    if(number>127):
        number = -(255-number)
    ListOfPower = [number]
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
            ListOfPower.append(number)
print(ListOfPower)
print(np.mean(ListOfPower))