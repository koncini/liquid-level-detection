from time import sleep
import RPi.GPIO as gpio

DIR = 20   #pin 38 to TB6560 cw+
STEP = 21  #pin 40 to TB6560 clk+
CW =1
CCW =0
CDIR = None

gpio.setmode(gpio.BCM)
gpio.setup(DIR, gpio.OUT)
gpio.setup(STEP, gpio.OUT)

# Main body of code
try:
    while True:
        x = input()
        if x == "C":
            print("Cerrando")
            gpio.output(DIR,CCW)
            for x in range(100):
                gpio.output(STEP,gpio.HIGH)
                sleep(.0050)
                gpio.output(STEP,gpio.LOW)
                sleep(.0050)

        if x == "O":
            print("Abriendo")
            gpio.output(DIR,CW)
            for x in range(100):
                gpio.output(STEP,gpio.HIGH)
                sleep(.0050)
                gpio.output(STEP,gpio.LOW)
                sleep(.0050)

        if x == "M":
            print("Cerrado 50%")
            gpio.output(DIR,CCW)
            for x in range(50):
                gpio.output(STEP,gpio.HIGH)
                sleep(.0050)
                gpio.output(STEP,gpio.LOW)
                sleep(.0050)

        if x == "Q":
            print("Cerrado 25%")
            gpio.output(DIR,CCW)
            for x in range(22):
                gpio.output(STEP,gpio.HIGH)
                sleep(.0050)
                gpio.output(STEP,gpio.LOW)
                sleep(.0050)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()
