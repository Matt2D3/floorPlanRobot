from machine import PWM, Pin
import utime
def beep(freq):
    beeper = PWM(Pin(5, Pin.OUT), freq=freq, duty=512)
    utime.sleep(0.1)
    beeper.deinit()
def startup():
    beep(440)
    beep(880)
    beep(1320)
def shutdown():
    beep(1320)
    beep(880)
    beep(440)
def start():
    beep(440)
    beep(880)
def end():
    beep(880)
    beep(440)
def debugMode():
    beep(440)
    beep(500)   
    beep(440)