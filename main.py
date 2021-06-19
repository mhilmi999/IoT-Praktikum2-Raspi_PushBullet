from pushbullet import Pushbullet
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN) # input raindrop sensor 

pb = Pushbullet("o.FrAarM58juBkQIN8gj1u8YILbFGuUVCX")
print(pb.devices)

before = 1
while True:
    i = GPIO.input(11) # raindrop sensor
    if i == 1 and before == 0:
        print("Arep udan, gek ndang balik entas o no jemuran Ibuk")
        before = i
        dev = pb.get_device('Samsung SM-G985F')
        push = dev.push_note("Alert!!", "Arep udan, gek ndang balik entas o no jemuran Ibuk")
        sleep(1)
    elif i == 0 and before == 1:
        print("Gorong udan, rung waktu e entas jemuran")
        before = i
        sleep(1)
