from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import st7567
import RPi.GPIO as GPIO
from pathlib import Path
from PIL import Image
import os
import time
import PIL.ImageOps
from gpiozero import CPUTemperature
import datetime
import Adafruit_DHT
import sys
import pigpio


#LED
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)				# Programmed GPIO using BCM pin numbers. (PIN35 as ‘GPIO19’)
GPIO.setup(12,GPIO.OUT)				# initialize GPIO12 as an output.
GPIO.setup(13,GPIO.OUT)				# initialize GPIO13 as an output.


pi = pigpio.pi() # connect to local Pi

dL = 50
dR = 50

d_cycleL = (dL / 100) * 255 	#converts to percentage for the csv
d_cycleR = (dR / 100) * 255

# dL = 128	# Set duty cycle for LED 1 here range 0 to 255
# dR = 128	# Set duty cycle for LED 2 here range 0 to 255
# 
# d_cycleL = (dL / 255)*100 	#converts to percentage for the csv
# d_cycleR = (dR / 255)*100

# iL=d_cycleL 	# Used in the csv script for led duty cycle
# iR=d_cycleR

iL=dL 	# Used in the csv script for led duty cycle
iR=dR

pi.set_PWM_frequency(12, 8000) 	# Set default freq to 8000
pi.set_PWM_frequency(13, 8000) 	# Set default freq to 8000
pi.set_PWM_dutycycle(12, d_cycleL) 	# Sets gpi 12 duty ccle
pi.set_PWM_dutycycle(13, d_cycleR) 	# Sets gpi 12 duty ccle   

       
#lcd
serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=17)
device = st7567(serial, rotate=0)
lcdFreq = 30	#this is in hertz desired

# def dht():
#     hum,temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 26)
#     if hum is not None and temp is not None:
#         hum = '{:0.1f}'.format(hum)
#         temp = '{:0.1f}'.format(temp)
#     else:
#         hum = '?'
#         temp = '?'
#     time.sleep(1)
#     return hum, temp

def main():
    
    image_directory = "/home/pi/imgs2"
    image_files = [f for f in os.listdir(image_directory) if f.endswith(('.jpg','.jpeg', '.png', '.gif'))]
    image_files.sort()
                   
    while 1:
        
        cpu = CPUTemperature()
        date = datetime.datetime.now()
#         humidity, Temp_C = dht()

#         with open ('/var/www/html/Data2.csv','a') as datafile:
#             datafile.write(str(date) + "," +
#                            str(cpu.temperature) + "," +
#                            str(Temp_C) + "," +
#                            str(humidity) + "," +
#                            str(iR) + "," +
#                            str(iL)+ "," +
#                            str(lcdFreq) + "," +
#                            str(sys.argv) + "\n")

        with open ('/var/www/html/Data2.csv','a') as datafile:
            datafile.write(str(date) + "," + 
                           str(cpu.temperature) + "," +
                           str(iR) + "," +
                           str(iL)+ "," +
                           str(lcdFreq) + "," +
                           str(sys.argv) + "\n")
        
       
        #Loop through each image and display it
        for image_file in image_files:
            image_path = os.path.join(image_directory, image_file)
            temp_img2 = Image.open(image_path)
            new_img = temp_img2.resize((128, 64))
            inverted_image= PIL.ImageOps.invert(new_img)
            inverted_image.save('img.jpg')
            
            temp_img = Image.open('img.jpg') \
                .transform(device.size, Image.AFFINE, (1, 0, 0, 0, 1, 0), Image.BILINEAR) \
                .convert("L") \
                .convert(device.mode)

            # Image display
            
            temp_img=temp_img.transpose(Image.FLIP_TOP_BOTTOM)
            temp_img=temp_img.transpose(Image.FLIP_LEFT_RIGHT)
            device.display(temp_img)
            time.sleep(1 / lcdFreq)

if __name__ == "__main__":
    main()
