# micropython car control

# from machine import Pin

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

while True:

    f_b = input("forward or backward?\n")

    if motor(f_b) is True:
        print("going forwards\n")
    elif motor(f_b) is False:
        print("going backwards\n")

    l_r = input("left or right?\n")

    if steering(l_r) is True:
        print("going forwards\n")
    elif steering(l_r) is False:
        print("going backwards\n")