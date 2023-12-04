import RPi.GPIO as GPIO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program


#Led
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)# initialize GPIO19 as an output.
LED_1 = GPIO.PWM(12,100)
LED_2 = GPIO.PWM(13,100)#GPIO19 as PWM output, with 100Hz frequency
LED_1.start(0)                              #generate PWM signal with 0% duty cycle
LED_2.start(0)

def LED():
    i = 0
    while 1:					#controll LED1
        print("Duty Cycle Set to :%", i)
        t=input ("led_1\n	press'e' to increase birghtness\n	press 'q' to decrease brightness\n	press 's' to set\n")
        
        if t == 'e': 
            i=i+10
            if i < 100:
                LED_1.ChangeDutyCycle(i)			#change duty cycle for varying the brightness of LED."""
            else:
                i = 100
                LED_1.ChangeDutyCycle(i)
                print('ERROR Duty Cycle Cant be more than 100')
        
        elif t == 'q':
            i = i-10
            if i > 0:
                LED_1.ChangeDutyCycle(i)			#change duty cycle for varying the brightness of LED."""
            else:
                i = 0
                LED_1.ChangeDutyCycle(i)
                print("ERROR Duty Cycle Cant be less than 0")
        elif t == 's':
            break;
    
    i2=0
    while 1:			#CONTROLL Led_2
        print("Duty Cycle Set to :%", i2)
        t=input ("LED_2\n	press'e' to increase birghtness\n	press 'q' to edecrease brightness\n	press 's' to set\n")
        
        if t == 'e': 
            i2=i2+10
            if i2 < 100:
                LED_2.ChangeDutyCycle(i2)			#change duty cycle for varying the brightness of LED."""
            else:
                i2 = 100
                LED_2.ChangeDutyCycle(i2)
                print('ERROR Duty Cycle Cant be more than 100')
        
        elif t == 'q':
            i2 = i2-10
            if i2 > 0:
                LED_2.ChangeDutyCycle(i2)			#change duty cycle for varying the brightness of LED."""
            else:
                i2 = 0
                LED_2.ChangeDutyCycle(i2)
                print("ERROR Duty Cycle Cant be less than 0")
        elif t == 's':
            main()
LED()
