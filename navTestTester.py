import navTest
import turtle
import math
import time
import gcodeParser
inst = gcodeParser.convertGcode("hylandz.gcode", False)
print("path: ",inst)
skk = turtle.Turtle()
skk.left(90)
for i in inst: 
    i[0] = float(i[0])*1.5
    i[1] = float(i[1])*1.5
def breakVector(angle, dist):
    x = dist*math.cos(angle*3.14/180)
    y = dist*math.sin(angle*3.14/180)
    return [x,y]
curPos = [0,0]
time.sleep(1)
step = 0
inst.append(inst[1])

negative = 0
for i in inst:
    next = navTest.nextStep(skk.pos(),i)
    #next = navTest.nextStep(curPos,i)
    print(next)
    # 0 is angle
    # 1 i dist
    if next[0] == None:
        next[0] = 0
    if next[1] == None:
        next[1] == 0
    next[0] = round(next[0])
    next[1] = round(next[1])
    
    if(next[2]==1):
        skk.pendown()
        print("penDown")
    if(next[2]==0):
        skk.penup()
        print("penUp")
    skk.setheading((next[0]))
    skk.forward(next[1])

    if next[0] <0:
        print("--------")
        print("negative")
        print("--------")
        negative += 1
    #skk.write(step)
    step+=1
    print(i)
    print(skk.pos())
    curPos = [curPos[0] + breakVector(round(next[0]),round(next[1]))[0],curPos[1] + breakVector(round(next[0]),round(next[1]))[1]]
    print(curPos)
    print("error: ",curPos[0] - skk.pos()[0]+curPos[1] - skk.pos()[1])
    print(breakVector(next[0],next[1]))
    print("")
print("steps: ", step)
print((curPos[0] - inst[1][0])+(curPos[1] - inst[1][1]))
print(negative)
turtle.done()