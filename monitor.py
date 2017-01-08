import RPi.GPIO as GPIO
import time
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pin 18 controls the LED output.
GPIO.setup(18,GPIO.OUT)

# Pin 21 is an input for a switch.
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Pin 16 is the data input from the DHT22 Temperature Humidity sensor.
# https://www.adafruit.com/products/385
GPIO.setup(16,GPIO.IN)

# This program reads a 
# Inspired by sample code from
# http://razzpisampler.oreilly.com/ch07.html
# https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/simpletest.py
while True:

    input_state = GPIO.input(21)
    if input_state == False:
        print('Button Pressed')
        print "LED on"
        GPIO.output(18,GPIO.HIGH)
    else:
        print "LED off"
        GPIO.output(18,GPIO.LOW)


    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 16)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature * 9/5 + 32, humidity))
        #print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')


    print('\n')
    time.sleep(5)
