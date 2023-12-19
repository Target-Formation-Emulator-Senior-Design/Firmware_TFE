from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import st7567
import RPi.GPIO as GPIO
from pathlib import Path
#import urllib3
from PIL import Image
import os
import time
#import matplotlib.pyplot as plt
import PIL.ImageOps
from gpiozero import CPUTemperature
import datetime
import Adafruit_DHT
import sys
import pigpio


#Led
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)         	#we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
GPIO.setup(12,GPIO.OUT)           	# initialize GPIO19 as an output.
GPIO.setup(13,GPIO.OUT)				# initialize GPIO19 as an output.


pi = pigpio.pi() # connect to local Pi

d1 = 255    #Set duty cycle for LED 1 here range 0 to 255
d2 = 255    #Set duty cycle for LED 2 here range 0 to 255

d_cycle1 = (d1 / 255)*100 #converts t percentage for the csv
d_cycle2 = (d2 / 255)*100

i1=d_cycle1 #used in the csv script for led duty cycle
i2=d_cycle2

pi.set_PWM_dutycycle(12, d1) #sets gpi 12 duty ccle
pi.set_PWM_dutycycle(13, d2) #sets gpi 12 duty ccle   

       
#lcd
serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=17)
device = st7567(serial, rotate=0)
lcdFreq = 5 #this is in hertz desired

def main():
    
    
   
                   
    while 1:
        
#         cpu = CPUTemperature()
#         date = datetime.datetime.now()
#         humidity,Temp_C = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 26)
#         if humidity is not None and Temp_C is not None:
#             humidity = '{:0.1f}'.format(humidity)
#             Temp_C = '{:0.1f}'.format(Temp_C)
#         else:
#             humidity = '?'
#             Temp_C = '?'
# 
#         with open ('/var/www/html/Data2.csv','a') as datafile:
#             datafile.write(str(date) + "," +
#                            str(cpu.temperature) + "," +
#                            str(Temp_C) + "," +
#                            str(humidity) + "," +
#                            str(i2) + "," +
#                            str(i)+ "," +
#                            str(lcdFreq) + "," +
#                            str(sys.argv) + "\n")
#         LED_1.start(i)#generate PWM signal with 0% duty cycle                             
#         LED_2.start(i2)
        cpu = CPUTemperature()
        date = datetime.datetime.now()
        #with open ('/var/www/html/CPUTemp.csv','a') as datafile:
            #datafile.write(str(cpu.temperature)+"\n")
        with open ('/var/www/html/Data2.csv','a') as datafile:
            datafile.write(str(date) + "," + 
                           str(cpu.temperature) + "," +
                           str(i2) + "," +
                           str(i1)+ "," +
                           str(lcdFreq) + "," +
                           str(sys.argv) + "\n")
        
       
        try:#Loop through each image and display it
            image_directory = "/home/pi/sign_off_imgs"
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
            
                

        # Image display
                
                temp_img=temp_img.transpose(Image.FLIP_TOP_BOTTOM)
                temp_img=temp_img.transpose(Image.FLIP_LEFT_RIGHT)
                #img_resized = temp_img.resize((128, 64))
                device.display(temp_img)
                time.sleep(1 / lcdFreq)
                #time.sleep(1)
        except KeyboardInterrupt:
            break
                



if __name__ == "__main__":
    main()
    
    



