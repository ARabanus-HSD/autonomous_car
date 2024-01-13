# micropython car control
import RPi.GPIO as GPIO
import time

def motor(direction=["w", "s", "x"]):
    """
    input is w or s as a string
    returns bool:
        False for forwards
        True for backwards
    """
    if direction == "w":
        engine_status = 1
    elif direction == "s":
        engine_status = -1
    else:
        engine_status = 0
    return engine_status 

def steering(direction=["a", "d", "x"]):
    """
    input is a or d as a string
    returns bool:
        False for left
        True for right
    """
    if direction == "a":
        turning = 1
    elif direction == "d":
        turning = -1
    else:
        turning = 0
    return turning


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
    GPIO.output(17, True)
    GPIO.output(27, True)
    GPIO.output(23, True)
    GPIO.output(24, True)
    # collect use input on where you want to go
    f_b = input("forward (w) or backward (s) or none (x)?\n")
    l_r = input("left (a) or right (d) or none (x)?\n")
    

    # check if steering is left
    if steering(l_r) == 1:
        print("going left\n")
        GPIO.output(23, False)
        # check if forwards, backwards or none
        if motor(f_b) == 1:
            print("going forwards\n")
            GPIO.output(17, False)
            time.sleep(1)
            GPIO.output(17, True)
        elif motor(f_b) == -1:
            print("going backwards\n")
            GPIO.output(27, False)
            time.sleep(1)
            GPIO.output(27, True)
        elif motor(f_b) == 0:
            print("doing nothing")
            time.sleep(1)
        GPIO.output(23, True)

    # check if steering is right
    elif steering(l_r) == -1:
        print("going right\n")
        GPIO.output(24, False)
        # check if forwards, backwards or none
        if motor(f_b) == 1:
            print("going forwards\n")
            GPIO.output(17, False)
            time.sleep(1)
            GPIO.output(17, True)
        elif motor(f_b) == -1:
            print("going backwards\n")
            GPIO.output(27, False)
            time.sleep(1)
            GPIO.output(27, True)
        elif motor(f_b) == 0:
            print("doing nothing")
            time.sleep(1)
        GPIO.output(24, True)

    # check if steering is none
    elif steering(l_r) == 0:
        print("not steering\n")
        # check if forwards, backwards or none
        if motor(f_b) == 1:
            print("going forwards\n")
            GPIO.output(17, False)
            time.sleep(1)
            GPIO.output(17, True)
        elif motor(f_b) == -1:
            print("going backwards\n")
            GPIO.output(27, False)
            time.sleep(1)
            GPIO.output(27, True)
        elif motor(f_b) == 0:
            print("doing nothing")
            time.sleep(1)
