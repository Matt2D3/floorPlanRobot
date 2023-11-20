#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 13:55:29 2023

@author: matt2d2
"""

def cordAverager(cordList):
    isolatedCord = cordList
    cx=0
    cy=0
    print(isolatedCord)
    for i in isolatedCord:
        print(i)
        cx += i[0]
        cy += i[1]
    
    cx = cx / len(cordList)
    cy = cy / len(cordList) 
    return([cx,cy])     
def convertGcode(inputFile,compress):
    
    pcl = [[0,0]]
    f = open(inputFile, "r")
    inputGcode = str(f.read())
    print(inputGcode)
    output = []
    
    inputGcode = inputGcode.split('\n')
    #print(inputGcode)
    #print(type(inputGcode))
    prevCord = [0,0]
    if True:
        for i in inputGcode:
            i = i.replace("G02","")
            i = i.replace("G01", "")
            i = i.replace("G1","")
            i = i.replace("G03","")
            i = i.split()
            if not ";" in str(i):
                try:
                    check = 0
                    x = 0
                    y = 0
                    for val in i:
                        print(i)
        
                        if "X" in val:
                            
                            x = float(val.replace("X",""))*10
                            print("found x: ",x)
                            check += 1
                        if "Y" in val:
                            
                            y = float(val.replace("Y",""))*10
                            print("found y: ",y)
                            check += 1
                        penup = 1
                        if "G0 " in val or "G00 " in val:
                            penup = 0
                        
                    #print(x,y)
                    print("check val: ",check)
                    if check >= 2:
                        
                        if abs(x-prevCord[0]) + abs(y-prevCord[1])>=3 or not compress:
                            #print("pcl: ",pcl,"average: ",cordAverager(pcl) )
                            try:
                                output.append(cordAverager(pcl).append(penup))
                            except:
                                output.append(prevCord)
                            prevCord = [x,y,penup]
                            pcl = []
                        else: 
                            prevCord = [x,y,penup]
                            pcl.append(prevCord)
                            print("pcl: ",pcl,"average: ",cordAverager(pcl) )
                            
                except IndexError:
                    print("bruh")
    output2 = []
    firstNonError = False
    done = True
    for i in output:
        if str(i) == "None":
            i = [0,0,0]
        else:
            firstNonError = True
        if firstNonError and done:
            done = False
            i[2]=0
        
        output2.append(i)
    
    return(output2)
if __name__ == "__main__":
    print("final list: ",convertGcode("W COOKIE CUTTER - Elise Kennedy 6-11-14.gcode",True))
