# micropython car control
import RPi.GPIO as GPIO
import time

def motor(direction=["w", "s", "x"]):
    """
    input is w or s as a string
    returns bool:
        true for forwards
        false for backwards
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
        true for left
        false for right
    """
    if direction == "a":
        turning = 1
    elif direction == "d":
        turning = -1
    else:
        turning = 0
    return turning


GPIO.setmode(GPIO.BOARD)
pin_fw = GPIO.setup(2, GPIO.OUT)
pin_bw = GPIO.setup(3, GPIO.OUT)
pin_l = GPIO.setup(4, GPIO.OUT)
pin_r = GPIO.setup(17, GPIO.OUT)

while True:

    # collect use input on where you want to go
    f_b = input("forward (w) or backward (s) or none (x)?\n")
    l_r = input("left (a) or right (d) or none (x)?\n")


    # check if steering is left
    if steering(l_r) == 1:
        print("going left\n")
        GPIO.output(4, True)
        # check if forwards, backwards or none
        if motor(f_b) == 1:
            print("going forwards\n")
            GPIO.output(2, True)
            time.sleep(1)
            GPIO.output(2, False)
        elif motor(f_b) == -1:
            print("going backwards\n")
            GPIO.output(3, True)
            time.sleep(1)
            GPIO.output(3, False)
        elif motor(f_b) == 0:
            print("doing nothing")
            time.sleep(1)
        GPIO.output(4, False)

    # check if steering is right
    elif steering(l_r) == -1:
        print("going right\n")
        GPIO.output(17, True)
        # check if forwards, backwards or none
        if motor(f_b) == 1:
            print("going forwards\n")
            GPIO.output(2, True)
            time.sleep(1)
            GPIO.output(2, False)
        elif motor(f_b) == -1:
            print("going backwards\n")
            GPIO.output(3, True)
            time.sleep(1)
            GPIO.output(3, False)
        elif motor(f_b) == 0:
            print("doing nothing")
            time.sleep(1)
        GPIO.output(17, False)

    # check if steering is none
    elif steering(l_r) == 0:
        print("not steering\n")
        # check if forwards, backwards or none
        if motor(f_b) == 1:
            print("going forwards\n")
            GPIO.output(2, True)
            time.sleep(1)
            GPIO.output(2, False)
        elif motor(f_b) == -1:
            print("going backwards\n")
            GPIO.output(3, True)
            time.sleep(1)
            GPIO.output(3, False)
        elif motor(f_b) == 0:
            print("doing nothing")
            time.sleep(1)
