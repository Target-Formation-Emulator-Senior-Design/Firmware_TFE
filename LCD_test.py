"""from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import st7567
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)

serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=17)
device = st7567(serial,rotate=0)


                                            
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill= "black")
    draw.text((30,40), "Hello ASML",fill="white")
    
    """


from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import st7567
import RPi.GPIO as GPIO
from pathlib import Path
import urllib3
from PIL import Image
import os
import time
import cv2
import matplotlib.pyplot as plt
import PIL.ImageOps

GPIO.setwarnings(False)

serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=17)
device = st7567(serial, rotate=0)

import subprocess
from time import sleep

y=0.1
subprocess.Popen (["python", 'led_fading.py'])
sleep(y)

def download_image(url, file_path):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
   
    with open(file_path, 'wb') as f:
        f.write(response.data)

def main():
    #image_url = "https://webstockreview.net/images/png-format-images-3.png"
    #image_path = "image.jpg"  # Change this to the desired path
    
    # Download the image
    #download_image(image_url, image_path)
    image_directory = "/home/echavarin2000/target-images"
    image_files = [f for f in os.listdir(image_directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_files.sort()
    
    # Loop through each image and display it
#    for i in range (10):
#        for image_file in image_files:
#            image_path = os.path.join(image_directory, image_file)
#            temp_img2 = Image.open(image_path)
#            new_img = temp_img2.resize((128, 64))
#            inverted_image= PIL.ImageOps.invert(new_img)
#            inverted_image.save('img.jpg')
#           #new_img.save('img.jpg')
#            #img=cv2.imread(image_path)
#            #cv2.resize(img, (128,64))
#            #img_75 = cv2.resize(img, None, fx = 0.75, fy = 0.75)
#            temp_img = Image.open('img.jpg') \
#                .transform(device.size, Image.AFFINE, (1, 0, 0, 0, 1, 0), Image.BILINEAR) \
#                .convert("L") \
#                .convert(device.mode) 
            
            #temp_img = temp_img.convert("RGB")
        #

#        # Image display
#        
#            temp_img=temp_img.transpose(Image.FLIP_TOP_BOTTOM)
#            img_resized = temp_img.resize((128, 64))
#            device.display(temp_img)
#            time.sleep(0.2)
    
    for image_file in image_files:
            image_path = os.path.join(image_directory, image_file)
            temp_img2 = Image.open(image_path)
            new_img = temp_img2.resize((128, 64))
            inverted_image= PIL.ImageOps.invert(new_img)
            inverted_image.save('img.jpg')
            #new_img.save('img.jpg')
            #img=cv2.imread(image_path)
            #cv2.resize(img, (128,64))
            #img_75 = cv2.resize(img, None, fx = 0.75, fy = 0.75)
            temp_img = Image.open('img.jpg') \
                .transform(device.size, Image.AFFINE, (1, 0, 0, 0, 1, 0), Image.BILINEAR) \
                .convert("L") \
                .convert(device.mode) 
            
            #temp_img = temp_img.convert("RGB")
        

        # Image display
        
            temp_img=temp_img.transpose(Image.FLIP_TOP_BOTTOM)
            temp_img=temp_img.transpose(Image.FLIP_LEFT_RIGHT)
            img_resized = temp_img.resize((128, 64))
            device.display(temp_img)
            time.sleep(1000)
    

if __name__ == "__main__":
    main()
    
