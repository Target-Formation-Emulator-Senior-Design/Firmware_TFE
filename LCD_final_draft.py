from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import st7567
import RPi.GPIO as GPIO
from pathlib import Path
import urllib3
from PIL import Image
import os
import time
import matplotlib.pyplot as plt
import PIL.ImageOps
import keyboard
#Led
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)         	#we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
GPIO.setup(12,GPIO.OUT)           	# initialize GPIO19 as an output.
GPIO.setup(13,GPIO.OUT)				# initialize GPIO19 as an output.
LED_1 = GPIO.PWM(12,100)          		#GPIO19 as PWM output, with 100Hz frequency
LED_2 = GPIO.PWM(13,100)			#GPIO19 as PWM output, with 100Hz frequency
LED_1.start(0)                          #generate PWM signal with 0% duty cycle                             
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
                print('ERROR Duty Cycle Cant be more than 100', i)
        
        elif t == 'q':
            i = i-10
            if i > 0:
                LED_1.ChangeDutyCycle(i)			#change duty cycle for varying the brightness of LED."""
            else:
                i = 0
                LED_1.ChangeDutyCycle(i)
                print("ERROR Duty Cycle Cant be less than 0", i)
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
                print('ERROR Duty Cycle Cant be more than 100', i2)
        
        elif t == 'q':
            i2 = i2-10
            if i2 > 0:
                LED_2.ChangeDutyCycle(i2)			#change duty cycle for varying the brightness of LED."""
            else:
                i2 = 0
                LED_2.ChangeDutyCycle(i2)
                print("ERROR Duty Cycle Cant be less than 0", i2)
        elif t == 's':
            main()                       
            

       
#lcd
serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=17)
device = st7567(serial, rotate=0)



def main():
    image_directory = "/home/pi/imgs2"
    image_files = [f for f in os.listdir(image_directory) if f.endswith(('.jpg','.jpeg', '.png', '.gif'))]
    image_files.sort()
    
    while 1:
        
        try:#Loop through each image and display it
            image_directory = "/home/pi/imgs2"
            image_files = [f for f in os.listdir(image_directory) if f.endswith(('.jpg','.jpeg', '.png', '.gif'))]
            image_files.sort()
            for image_file in image_files:
                image_path = os.path.join(image_directory, image_file)
                temp_img2 = Image.open(image_path)
                new_img = temp_img2.resize((128, 64))
                inverted_image= PIL.ImageOps.invert(new_img)
                inverted_image.save('img.jpg')
                #new_img.save('img.jpg')
                
                temp_img = Image.open('img.jpg') \
                    .transform(device.size, Image.AFFINE, (1, 0, 0, 0, 1, 0), Image.BILINEAR) \
                    .convert("L") \
                    .convert(device.mode) 
            
                #temp_img = temp_img.convert("RGB")

        # Image display
                
                temp_img=temp_img.transpose(Image.FLIP_TOP_BOTTOM)
                img_resized = temp_img.resize((128, 64))
                device.display(temp_img)
                time.sleep(0.2)
                #if keyboard.is_pressed('o'):
                 #   LED()
        except KeyboardInterrupt:
             LED()
        
    
    
    
if __name__ == "__main__":
    
    main()
   

