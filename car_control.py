# micropython car control

from machine import Pin
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



pin_fw = Pin(3, mode=Pin.OUT)
pin_bw = Pin(5, mode=Pin.OUT)
pin_l = Pin(7, mode=Pin.OUT)
pin_r = Pin(11, mode=Pin.OUT)

while True:

    # collect use input on where you want to go
    f_b = input("forward (w) or backward (s) or none (x)?\n")
    l_r = input("left (a) or right (d) or none (x)?\n")


    # check if steering is left
    if steering(l_r) == 1:
        print("going left\n")
        pin_l.high()
        # check if forwards, backwards or none
        if motor(f_b) == 1:
            print("going forwards\n")
            pin_fw.high()
            time.sleep(1)
        elif motor(f_b) == -1:
            print("going backwards\n")
            pin_bw.high()
            time.sleep(1)
        elif motor(f_b) == 0:
            print("doing nothing")
            time.sleep(1)

    # check if steering is right
    elif steering(l_r) == -1:
        print("going right\n")
        pin_r.high()
        # check if forwards, backwards or none
        if motor(f_b) == 1:
            print("going forwards\n")
            pin_fw.high()
            time.sleep(1)
        elif motor(f_b) == -1:
            print("going backwards\n")
            pin_bw.high()
            time.sleep(1)
        elif motor(f_b) == 0:
            print("doing nothing")
            time.sleep(1)

    # check if steering is none
    elif steering(l_r) == 0:
        print("going right\n")
        pin_r.high()
        # check if forwards, backwards or none
        if motor(f_b) == 1:
            print("going forwards\n")
            pin_fw.high()
            time.sleep(1)
        elif motor(f_b) == -1:
            print("going backwards\n")
            pin_bw.high()
            time.sleep(1)
        elif motor(f_b) == 0:
            print("doing nothing")
            time.sleep(1)
