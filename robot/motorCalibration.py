import stepperDriver as st
import time
global maxAccel
global maxVel
global maxStartVel
maxAccel = 0.19
maxDecel = 0.125
maxVel = 250
maxStartVel = 5
mode = 1
stepsPerMM=6.45
stepsPerDegree = 11.685
while True:
    if mode == 1:
        
        print("spd: "+str(stepsPerDegree))
        stepsPerDegree = float(input("spd: "))

        steps = (stepsPerDegree*360)*1
        st.init(12, 13, 27, 14, 22)
        st.ennableMotors(1)
        st.setDir(1,0)
        st.stepSteps(round(steps),maxAccel,maxDecel,maxVel,maxStartVel/2)
        time.sleep(3)
        st.setDir(0,1)
        st.stepSteps(round(steps),maxAccel,maxDecel,maxVel,maxStartVel/2)
        time.sleep(3)
        st.ennableMotors(0)

    if mode == 2:
        print("spm: "+str(stepsPerMM))
        stepsPerMM=float(input("spm: "))
        steps = stepsPerMM*1000
        st.init(12, 13, 27, 14, 22)
        st.ennableMotors(1)
        st.setDir(1,1)
        st.stepSteps(round(steps),maxAccel,maxDecel,maxVel,maxStartVel/2)
        time.sleep(3)
        st.setDir(0,0)
        st.stepSteps(round(steps),maxAccel,maxDecel,maxVel,maxStartVel/2)
        time.sleep(3)
        st.ennableMotors(0)
