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
#Led
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)         	#we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
GPIO.setup(12,GPIO.OUT)           	# initialize GPIO19 as an output.
GPIO.setup(13,GPIO.OUT)				# initialize GPIO19 as an output.
LED_1 = GPIO.PWM(12,10000)          		#GPIO19 as PWM output, with 10000Hz frequency
LED_2 = GPIO.PWM(13,10000)			#GPIO19 as PWM output, with 10000Hz frequency


i =50
i2=50
#         
LED_1.start(i)                          #generate PWM signal with 0% duty cycle                             
LED_2.start(i2)                      
       
#lcd
serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=17)
device = st7567(serial, rotate=0)
lcdFreq = 5

def main():
   
   #instead of processing all files with each loop, we're going pre-process the images and save it in a new folder
   try:
    #maybe make these image directories global
    image_directory = "/home/pi/sign_off_imgs"
    image_dest = "/home/pi/processed_imgs"
    if not os.path.exists(image_dest):
        os.mkdir(image_dest)
    image_files = [f for f in os.listdir(image_directory) if f.endswith(('.jpg','.jpeg', '.png', '.gif'))]
    for image_file in image_files:
        image_path = os.path.join(image_directory, image_file)
        destination_path = os.path.join(image_dest, image_file)
        temp_img2 = Image.open(image_path)
        new_img = temp_img2.resize((128, 64))
        inverted_image= PIL.ImageOps.invert(new_img)
        inverted_image.save('img.jpg')
        temp_img = Image.open('img.jpg') \
            .transform(device.size, Image.AFFINE, (1, 0, 0, 0, 1, 0), Image.BILINEAR) \
            .convert("L") \
            .convert(device.mode) 

        temp_img=temp_img.transpose(Image.FLIP_TOP_BOTTOM)
        temp_img=temp_img.transpose(Image.FLIP_LEFT_RIGHT)
        temp_img.save(new_path)
               
    while 1:
        # import time
        start_time = time.time()
        
        cpu = CPUTemperature()
        date = datetime.datetime.now()
       #Opening and saving to this file might slow down the loop. The file size grows linearly and probably adds a delay
        with open ('/var/www/html/CPUTemp.csv','a') as datafile:
            datafile.write(str(cpu.temperature)+"\n")
        with open ('/var/www/html/Data2.csv','a') as datafile:
            datafile.write(str(date) + "," +
                           str(cpu.temperature) + "," +
                           str(i2) + "," +
                           str(i)+ "," +
                           str(lcdFreq) + "," +
                           str(sys.argv) + "\n")

        try:#Loop through each image and display it
            image_processed = "/home/pi/processed_imgs"
            image_files = [f for f in os.listdir(image_processed) if f.endswith(('.jpg','.jpeg', '.png', '.gif'))]
            image_files.sort()


            for image_file in image_files:
                #this catch will reset the time each loop so the time.sleep function can properly subtrack
                if start_time == 0:
                    start_time = time.time()
                image_path = os.path.join(image_directory, image_file)
                img = Image.open(image_path)
                device.display(img)

                time.sleep(1 / lcdFreq - (time.time()-start_time))
                start_time=0


        except KeyboardInterrupt:
            break

