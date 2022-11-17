from time import sleep
import RPi.GPIO as gpio

DIR = 20   #pin 38 to TB6560 cw+
STEP = 21  #pin 40 to TB6560 clk+
CW =1
CCW =0
CDIR = None
current_status = 0

gpio.setmode(gpio.BCM)
gpio.setup(DIR, gpio.OUT)
gpio.setup(STEP, gpio.OUT)

# Main body of code
try:
    while True:
        print("Valve Current Status %s '%'" % current_status)
        x = input()
        if x == "C":
            print("Cerrando 100%")
            current_status = current_status - 100
            gpio.output(DIR,CW)
            for x in range(800):
                gpio.output(STEP,gpio.HIGH)
                sleep(.0005)
                gpio.output(STEP,gpio.LOW)
                sleep(.0005)

        if x == "O":
            print("Abriendo 100%")
            current_status = current_status + 100
            gpio.output(DIR,CCW)
            for x in range(800):
                gpio.output(STEP,gpio.HIGH)
                sleep(.0005)
                gpio.output(STEP,gpio.LOW)
                sleep(.0005)

        if x == "MC":
            print("Cerrado 50%")
            current_status = current_status - 50
            gpio.output(DIR,CW)
            for x in range(400):
                gpio.output(STEP,gpio.HIGH)
                sleep(.0005)
                gpio.output(STEP,gpio.LOW)
                sleep(.0005)

        if x == "QC":
            print("Cerrado 25%")
            current_status = current_status - 25
            gpio.output(DIR,CW)
            for x in range(200):
                gpio.output(STEP,gpio.HIGH)
                sleep(.0005)
                gpio.output(STEP,gpio.LOW)
                sleep(.0005)

        if x == "MO":
            print("Abriendo 50%")
            current_status = current_status + 50
            gpio.output(DIR,CCW)
            for x in range(400):
                gpio.output(STEP,gpio.HIGH)
                sleep(.0005)
                gpio.output(STEP,gpio.LOW)
                sleep(.0005)

        if x == "QO":
            print("Abriendo 25%")
            current_status = current_status + 25
            gpio.output(DIR,CCW)
            for x in range(200):
                gpio.output(STEP,gpio.HIGH)
                sleep(.0005)
                gpio.output(STEP,gpio.LOW)
                sleep(.0005)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()
