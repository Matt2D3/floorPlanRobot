print("rbtv3 main")
from machine import Pin, I2C
import time
import ssd1306
import buzzer
import stepperDriver as st
import navTest as nt

#list of points
cordsList = [[500,0],[0,500],[500,500],[0,0],[250,250],[0,0]]

#motor config
global maxAccel
global maxVel
global maxStartVel
maxAccel = 0.25
maxDecel = 0.125
maxVel = 500
maxStartVel = 5

startSwitch = Pin(26, Pin.IN, Pin.PULL_UP)
i2c = I2C(sda=Pin(18), scl=Pin(19))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

st.init(12, 13, 27, 14, 22)
st.ennableMotors(0)

global curAngle
curAngle = 0

def setHeading(heading):
    global curAngle
    error = heading - curAngle
    print(error, heading, curAngle)
    stepsPerDegree = 6.65 #number of steps taken to rotate 1 degree
    dir = 1
    stepsToTake = error*stepsPerDegree
    st.setDir(1,0)
    if stepsToTake <0:
        dir = 0
        st.setDir(0,1)
        stepsToTake *= -1
    st.stepSteps(round(stepsToTake),maxAccel/2,maxDecel,maxVel,maxStartVel/2)
    st.setDir(1,1)
    curAngle = heading
def moveMM(dist):
    stepsPerMM = 6.45
    st.setDir(1,1)
    st.stepSteps(round(dist*stepsPerMM),maxAccel,maxDecel,maxVel,maxStartVel)
    
# render path
xMax = 0
yMax = 0
xMin = 0
yMin = 0
for rCord in cordsList:
    print(rCord)
    if rCord[0] < xMin:
        xMin = rCord[0]
    if rCord[1] < yMin:
        yMin = rCord[1]
    if rCord[0] > xMax:
        xMax = rCord[0]
    if rCord[1] > yMax:
        yMax = rCord[1]
print(xMax,yMax,xMin,yMin) 
xCenter = (xMax+(xMin*-1))/2
yCenter = (yMax+(yMin*-1))/2
xScale = (xMax+xMin*-1)/63
yScale = (yMax+yMin*-1)/63
xTranslate = 64+(xCenter/2)
yTranslate = -32+(yCenter/2) 
#xTranslate = xMin*-1
#yTranslate = yMin*-1
print("center: ",xCenter, yCenter," translate: ",xTranslate,yTranslate)
curCord = [0,0]
display.fill(0)
print()
for rCord in cordsList:
    renderX = (rCord[0]+xTranslate)/xScale
    renderY = (rCord[1]+yTranslate)/yScale
    #renderCords.append([renderX,renderY])
    display.line(round(curCord[0]),round(curCord[1]),round(renderX),round(renderY),1)
    print(round(curCord[0]),round(curCord[1]))
    curCord = [renderX,renderY]
    display.show()
    time.sleep(0.1)
#print(renderCords)
print()
display.show()

    
stepList = nt.genPath(cordsList)
st.ennableMotors(1)
for curStep in stepList:
    setHeading(curStep[0])
    time.sleep(0.5)
    moveMM(curStep[1])
    time.sleep(0.5)
setHeading(0)
print("done")
time.sleep(3)
st.ennableMotors(0)



