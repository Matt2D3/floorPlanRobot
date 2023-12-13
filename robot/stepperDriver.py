#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:24:09 2023

@author: matt2d2
"""

print("stepper driver v2")
import utime
def smsSleep(slpTime):
    utime.sleep_us(int(slpTime*1000000))
        
def init(step1d, dir1d, step2d, dir2d, enabled):
    try:
        from machine import Pin
        global step1
        global step2
        global dir1
        global dir2
        global enable
        step1 = Pin(step1d, Pin.OUT) #left
        dir1 = Pin(dir1d, Pin.OUT)
        step2 = Pin(step2d, Pin.OUT) #right
        dir2 = Pin(dir2d, Pin.OUT)
        enable = Pin(enabled, Pin.OUT)
        enable.value(0)
        dir1.value(1)
        dir2.value(1)
        step1.value(0)
        step2.value(0)
        print("successfully initialized steppers")
    except:
        print("PIN INIT FAIL: test mode not implimented")
def setDir(Ldir, Rdir):
    dir1.value(Ldir)
    dir2.value(Rdir)
def ennableMotors(val):
    enable.value(val)
def step(hz):
    step1.value(1)
    step2.value(1)
    smsSleep((1/hz)/2)
    step1.value(0)
    step2.value(0)
    smsSleep((1/hz)/2)
def stepSteps(steps, acceli, deceli, maxVel, vi):
    #get accel decel steps
    realSteps = steps
    steps -= 1
    curVel = vi
    stepsDone = 0
    global curX
    curX = -(steps/2)
    
    
    first = ((deceli)/(acceli+deceli))
    print("first half: ",first)
    
    mid = first*steps-1
    # constant acceleration in a triangle patern, clamp velocity 
    midStep = mid

    #check which side of the triangle we are on

    while stepsDone <= steps:
        if curVel < vi:
            curVel = vi
        if stepsDone <= midStep:
            #first half
            dir = 1
            accel = acceli
        if stepsDone >= midStep:
            dir = -1
            accel = deceli
            
        if curVel >= maxVel:
            step(maxVel)
            stepsDone+=1
            #step(curVel)
            #print("maxvel")
            
        if curVel < maxVel:
            step(curVel)
            stepsDone+=1 
            

            
        
        curVel += accel*dir
        
    if stepsDone < steps: 
        for i in range(steps-stepsDone):
            step(vi)
    print(stepsDone, realSteps) 
                   
                    
                
            
        
