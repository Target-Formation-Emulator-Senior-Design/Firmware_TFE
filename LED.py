import RPi.GPIO as GPIO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program


#Led
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)                          #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)                          # initialize GPIO19 as an output.
LED_1 = GPIO.PWM(12,100)
LED_2 = GPIO.PWM(13,100)                        #GPIO19 as PWM output, with 100Hz frequency
LED_1.start(0)                                  #generate PWM signal with 0% duty cycle
LED_2.start(0)

def LED():
    i=0
    duty_cycle = 0
    while 1:					                #controll LED1
        
        t=input ("led_1\n	press'e' to increase birghtness\n	press 'q' to decrease brightness\n	press 's' to set\n")
        
        if t == 'e':        
            duty_cycle = duty_cycle + 10
        
        if t == 'e' and i<100:
            i=i+10
            print("Duty Cycle Set to :%", i)
            LED_1.ChangeDutyCycle(i)			#change duty cycle for varying the brightness of LED."""
        
        elif duty_cycle > 100:
            print ("'Error Duty Cycle cant be more than %100'")
            duty_cycle = duty_cycle - 10
            print("Duty Cycle Set to:%", i)
            
        elif t == 'q':
            duty_cycle = duty_cycle -10
            print("Duty Cycle Set to:%", i)
        if t == 'q' and i>0:
            i = i-10
            print("Duty Cycle Set to :%", i)
            LED_1.ChangeDutyCycle(i)			#change duty cycle for varying the brightness of LED."""
        
        elif duty_cycle < 0:
            print ("'Error Duty Cycle cant be less than %0'")
            print("Duty Cycle Set to :%", i)
            duty_cycle = duty_cycle + 10
        elif t == 's':
            
            break;
    while 1:			                    #CONTROLL Led_2
        t=input ("LED_2\n	press'e' to increase birghtness\n	press 'q' to edecrease brightness\n	press 's' to set\n")
        
        if t == 'e':        
            duty_cycle = duty_cycle + 10
        
        if t == 'e' and i<100:
            i=i+10
            print("Duty Cycle Set to :%", i)
            LED_2.ChangeDutyCycle(i)			#change duty cycle for varying the brightness of LED."""
        
        elif duty_cycle > 100:
            print ("'Error Duty Cycle cant be more than %100'")
            duty_cycle = duty_cycle - 10
            print("Duty Cycle Set to:%", i)
            
        elif t == 'q':
            duty_cycle = duty_cycle -10
            print("Duty Cycle Set to:%", i)
        if t == 'q' and i>0:
            i = i-10
            print("Duty Cycle Set to :%", i)
            LED_2.ChangeDutyCycle(i)			#change duty cycle for varying the brightness of LED."""
        
        elif duty_cycle < 0:
            print ("'Error Duty Cycle cant be less than %0'")
            print("Duty Cycle Set to :%", i)
            duty_cycle = duty_cycle + 10
        elif t == 's':
            #main()                             # used in other file to display image
            break;
LED()                                            #this lin is for testing only. not included in the main code
