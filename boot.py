# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

debug = True #ennable for wifi debug, DISSABLE FOR COMPETITION
bootSounds = True #ennable buzzer codes on boot
if debug:
    import network
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid="theTourist", password="gigachad")
    import webrepl
    webrepl.start()

from machine import I2C, Pin
import ssd1306
i2c = I2C(sda=Pin(18), scl=Pin(19))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
display.fill_rect(0, 0, 32, 32, 1)
display.fill_rect(2, 2, 28, 28, 0)
display.vline(9, 8, 22, 1)
display.vline(16, 2, 22, 1)
display.vline(23, 8, 22, 1)
display.fill_rect(26, 24, 2, 4, 1)
display.text('NA:tourist', 40, 0, 1)
display.text('MN:rbtV3', 40, 12, 1)
display.text('MOT:CS42', 40, 24, 1)

display.show()
import buzzer
import time
if bootSounds:
    buzzer.startup()
time.sleep(0.5)
display.text(('debug:'+str(debug)), 40, 36, 1)
if debug:
    display.text("WIFI IS ON", 40,48,1)
display.show()
if debug and bootSounds:
    buzzer.debugMode()


