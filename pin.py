pincheck = 0
pin = int(input("please set a pin for safety reasons on your device : "))
while pin != pincheck:
    pincheck = int(input("please re-enter the pin to confirm : "))
    if pin == pincheck :
        print ("correct your pin is saved")
    else :
        print ("sorry pin was incorrect")
