#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:33:00 2023

@author: matt2d2
"""


cordList = [[10,5,1]]


import trig

def quadCheck(p1):
    if(p1[0] >= 0 and p1[1] >=0):
        return 1
    if(p1[0] <= 0 and p1[1] >=0):
        return 2
    if(p1[0] <= 0 and p1[1] <=0):
        return 3
    if(p1[0] >= 0 and p1[1] <=0):
        return 4
def genPath(cordList):
    output = []
    curCord = [0,0]
    for i in cordList:
        distToNext = ((i[0]-curCord[0])**2+(i[1]-curCord[1])**2)**(1/2)
        ydif = i[1] - curCord[1]
        xdif = i[0] - curCord[0]
        try:
            if quadCheck([i[0]-curCord[0],i[1]-curCord[1]]) == 1:
                angleToNext = trig.SSS(abs(ydif),distToNext,abs(xdif))
                angleToNext = angleToNext[3]
            if quadCheck([i[0]-curCord[0],i[1]-curCord[1]]) == 3:
                angleToNext = trig.SSS(abs(ydif),distToNext,abs(xdif))
                angleToNext = angleToNext[3] +180
            if quadCheck([i[0]-curCord[0],i[1]-curCord[1]]) == 2:
                angleToNext = trig.SSS(abs(xdif),distToNext,abs(ydif))
                angleToNext = angleToNext[3] +90
            if quadCheck([i[0]-curCord[0],i[1]-curCord[1]]) == 4:
                angleToNext = trig.SSS(abs(xdif),distToNext,abs(ydif))
                angleToNext = angleToNext[3] +270
        except:
            if xdif != 0:
                if xdif > 0:
                    angleToNext =  0
                if xdif < 0:
                    angleToNext = 180
            if ydif != 0:
                if ydif > 0:
                    angleToNext = 90
                if ydif < 0:
                    angleToNext = 270
        try:
            output.append([angleToNext, distToNext,i[2]])
        except:
            output.append([angleToNext, distToNext])
        curCord = i
        
    return output
def nextStep(curCord, target):
    distToNext = ((target[0]-curCord[0])**2+(target[1]-curCord[1])**2)**(1/2)
    ydif = target[1] - curCord[1]
    xdif = target[0] - curCord[0]
    try:
        if quadCheck([target[0]-curCord[0],target[1]-curCord[1]]) == 1:
            angleToNext = trig.SSS(abs(ydif),distToNext,abs(xdif))
            angleToNext = angleToNext[3]
        if quadCheck([target[0]-curCord[0],target[1]-curCord[1]]) == 3:
            angleToNext = trig.SSS(abs(ydif),distToNext,abs(xdif))
            angleToNext = angleToNext[3] +180
        if quadCheck([target[0]-curCord[0],target[1]-curCord[1]]) == 2:
            angleToNext = trig.SSS(abs(xdif),distToNext,abs(ydif))
            angleToNext = angleToNext[3] +90
        if quadCheck([target[0]-curCord[0],target[1]-curCord[1]]) == 4:
            angleToNext = trig.SSS(abs(xdif),distToNext,abs(ydif))
            angleToNext = angleToNext[3] +270
    except:
        if xdif != 0:
            if xdif > 0:
                angleToNext =  0
            if xdif < 0:
                angleToNext = 180
        if ydif != 0:
            if ydif > 0:
                angleToNext = 90
            if ydif < 0:
                angleToNext = 270
  
    try:
        output=([angleToNext, distToNext,target[2]])
    except:
        output=([angleToNext, distToNext])
        
    return output

if __name__ == "__main__":
    print(genPath(cordList))
