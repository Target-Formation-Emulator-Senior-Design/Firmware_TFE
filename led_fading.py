from gpiozero import LED
from gpiozero import PWMLED
from time import sleep

led1 = PWMLED(12, 100)
led2 = PWMLED(13, 100)


#led1.value = 1 #LED fully on
#sleep(1)
#led1.value = 0.5 #LED half brightness
#sleep(1)
#led1.value= 0 #LED fully off
#sleep(1)

#led2.value = 1 #LED fully on
#sleep(1)
#led2.value = 0.5 #LED half brightness
#sleep(1)
#led2.value= 0 #LED fully off
#sleep(1)

try:
    #fade in and out forever
    
    while True:
        #fade in
        for duty_cycle in range(1, 100, 1):
            led1.value = duty_cycle/100.0
            led2.value = duty_cycle/100.0
            sleep(0.05)

        #fade out
        for duty_cycle in range(100, 1, -1):
            led1.value = duty_cycle/100.0
            led2.value = duty_cycle/100.0
            sleep(0.05)
            
except KeyboardInterrupt:
    print("Stop the program and turning off the LED")
    led1.value = 0
    led2.value = 0
    pass
