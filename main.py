from pushbullet import Pushbullet
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) # input raindrop sensor 

<<<<<<< HEAD
pb = Pushbullet("hehehehehtokensiniya")
=======

pb = Pushbullet("o.FrAarM58juBkQIN8gj1u8YILbFGuUVCX")
>>>>>>> 134dfb1e015756ed2d605b55b86f5526176e43e4
print(pb.devices)

before = 1
while True:
    i = GPIO.input(11) # raindrop sensor
    if i == 1 and before == 0:
        print "Arep udan, gek ndang balik entas o no jemuran Ibuk"
        before = i
        sleep(1)
    elif i == 0 and before == 1:
        print "Gorong udan, rung waktu e entas jemuran"
        sleep(1)
        before = i
        dev = pb.get_device('Samsung SM-G985F')
        push = dev.push_note("Alert!!", "Someone is in your house")
    
