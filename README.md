# picopad
This is a repository where i store files for my macropad made using Raspberry Pi Pico\
The picopad has 8 buttons and two knobs.\
The buttons send signal to Autohotkey which then proceeds to do significant macros.\
It also runs an application called deej which allows the knobs to be treated with absolute values for master and mic volume.

Installing CircuitPython on the pi pico:

You can get the latest release at https://circuitpython.org/board/raspberry_pi_pico/ \
I have put the file that i used for my picopad in the folder circuitpython incase this version gets deleted or something\
Press and hold the bootsel button and plug in the pico into the pc using a micro usb cable.\
Leave the bootsel button after it gets detected in windows as a flash drive.\
Drag and drop the circuitpython file in it. \
Pico should now restart. \
Put the file main.py in the main directory. \
Put the folder adafruit_hid in lib folder. \
PS: If the folder lib doesn't exist create it.


Assembly:

The following are connections for buttons, potentiometers and leds. To find out the locations of the pins refer to pico_pinout.png \
Buttons: \
1 - GP22 \
2 - GP21 \
3 - GP20 \
4 - GP14 \
5 - GP19 \
6 - GP18 \
7 - GP17 \
8 - GP16 \
Potentiometers: \
1 - GP27 \
2 - GP26 \
Leds: \
1 - GP13 \
2 - GP11 \
PS: The pins i chose are because i had damaged some of my pins. The leds and buttons can be connected to any GPIO(pin names starting with GP) and potentiometers work with GP26, GP27 and GP28 

Software:

Install Autohotkey from https://www.autohotkey.com or use the installer in the folder AutoHotKey. \
Right click the file pico.ahk and click on Send to>Desktop (create shortcut). \
Open run by using win+r or searching for run in windows search. \
Type(Preferrably copy) shell:startup and click OK. \
A folder opens up called Startup. \
Cut and paste the shortcut to the folder which is just opened.
