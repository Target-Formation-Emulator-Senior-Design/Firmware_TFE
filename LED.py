import RPi.GPIO as GPIO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program


#Led
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
GPIO.setup(12,GPIO.OUT)           # initialize GPIO19 as an output.
p = GPIO.PWM(12,100)          #GPIO19 as PWM output, with 100Hz frequency
p.start(0)                              #generate PWM signal with 0% duty cycle


def LED():
    i=0
    duty_cycle = 0
    while 1:
        
        t=input ("press'e' to increase birghtness\npress 'q' to edecrease brightness\npress 's' to set\n")
        
        if t == 'e':        
            duty_cycle = duty_cycle + 10
        
        if t == 'e' and i<100:
            i=i+10
            print("Duty Cycle Set to :%", i)
            p.ChangeDutyCycle(i)			#change duty cycle for varying the brightness of LED."""
        
        elif duty_cycle > 100:
            print ("'Error Duty Cycle cant be more than %100'")
            uty_cycle = duty_cycle - 10
            print("Duty Cycle Set to:%", i)
            
        elif t == 'q':
            duty_cycle = duty_cycle -10
            print("Duty Cycle Set to:%", i)
        if t == 'q' and i>0:
            i = i-10
            print("Duty Cycle Set to :%", i)
            p.ChangeDutyCycle(i)			#change duty cycle for varying the brightness of LED."""
        
        elif duty_cycle < 0:
            print ("'Error Duty Cycle cant be less than %0'")
            print("Duty Cycle Set to :%", i)
            duty_cycle = duty_cycle + 10
        elif t == 's':
            #main()                         # used in other file to display image
            break;

