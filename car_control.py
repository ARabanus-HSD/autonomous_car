# micropython car control

from machine import Pin
import time

def motor(direction=["w", "s"]):
    """
    input is w or s as a string
    returns bool:
        true for forwards
        false for backwards
    """
    if direction == "w":
        engine_status = True
    elif direction == "s":
        engine_status = False
    return engine_status 

def steering(direction=["a", "d"]):
    """
    input is a or d as a string
    returns bool:
        true for left
        false for right
    """
    if direction == "a":
        turning = True
    elif direction == "d":
        turning = False
    return turning

pin_fw = Pin(3, mode=Pin.OUT)
pin_fw = Pin(5, mode=Pin.OUT)
pin_l = Pin(7, mode=Pin.OUT)
pin_r = Pin(11, mode=Pin.OUT)

while True:

    f_b = input("forward or backward?\n")

    if motor(f_b) is True:
        print("going forwards\n")
        pin_fw = Pin(16, mode=Pin.OUT, value=1)
        time.sleep(1)
    elif motor(f_b) is False:
        print("going backwards\n")
        pin_fw = Pin(16, mode=Pin.OUT, value=1)
        time.sleep(1)

    l_r = input("left or right?\n")

    if steering(l_r) is True:
        print("going left\n")
        pin_l = Pin(16, mode=Pin.OUT, value=1)
        time.sleep(1)
    elif steering(l_r) is False:
        print("going right\n")
        pin_r = Pin(16, mode=Pin.OUT, value=1)
        time.sleep(1)
