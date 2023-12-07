# Firmware_TFE
Setup to use SSH:
1) Activate SSH on the Rapberry Pi.
   1. Click the raspberry logo at the top-left corner.
   2. Select Preferences > Raspberry Pi Configuration.
   3. Navigate to the Interfaces tab in the configuration window.
   4. Enable SSH in the second line.
2) Get the IP Adress of the RapberryPi
   1. Go into the terminal and type
       " hostname -I "
   2. note: the IP is up to 4 decimal values
        ex:)  192.168.1.1
3)  Go to  your laptop/PC and open terminal
4)  type SSH pi@IP
    1. where pi is the username
    2. IP is the IP if your pi
5) you know have full acsess on the PI terminal
6) to execute a script on the PI by using your pc
    1. in the terminal type "Python2 tst.py"
    2. where tst.py is the file name
   
