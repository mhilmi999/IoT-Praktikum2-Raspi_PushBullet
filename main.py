from pushbullet import Pushbullet
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) # input raindrop sensor 


pb = Pushbullet("hehehehehtokensiniya")
print(pb.devices)


while True:
    i = GPIO.input(11) # raindrop sensor
    if i == 0:
        print "Gorong udan, rung waktu e entas jemuran"
        sleep(1)
    elif i == 1:
        print "Arep udan, gek ndang balik entas o no jemuran Ibuk"

        dev = pb.get_device('Samsung SM-G985F')
        push = dev.push_note("Alert!!", "Someone is in your house")
        sleep(1)
