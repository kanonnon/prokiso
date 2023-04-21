import time
import RPi.GPIO

while True:
    sw_status = RPi.GPIO.input(18)
    if sw_status != 0:
        exec(open("./video.py").read())
    time.sleep(0.3)        