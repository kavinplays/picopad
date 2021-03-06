import time
import gamepad
import math
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import analogio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
#imported all the libraries we are going to use

keyboard = Keyboard(usb_hid.devices) #Connected to the pc as a keyboard. Now the pc detects that a keyboard is attached.

btn1 = digitalio.DigitalInOut(board.GP22) #btn1 is initialized, i.e. it has given a variable name and told the pico where to find the button via GPIO(22 in this case)
btn1.direction = digitalio.Direction.INPUT #it is stating that the button is input only which helps the pico understand that it is a button or switch that gives one of two values - 0 and 1
btn1.pull = Pull.DOWN #the button is pulled down via code so that it doesn't debounce, i.e. act like it is pressed multiple times when it is actually pressed only ones
btn2 = digitalio.DigitalInOut(board.GP21) #and the same is done for the rest of the buttons
btn2.direction = digitalio.Direction.INPUT
btn2.pull = Pull.DOWN
btn3 = digitalio.DigitalInOut(board.GP20)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = Pull.DOWN
btn4 = digitalio.DigitalInOut(board.GP14)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = Pull.DOWN
btn5 = digitalio.DigitalInOut(board.GP19)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = Pull.DOWN
btn6 = digitalio.DigitalInOut(board.GP18)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = Pull.DOWN
btn7 = digitalio.DigitalInOut(board.GP17)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = Pull.DOWN
btn8 = digitalio.DigitalInOut(board.GP16)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = Pull.DOWN


button1 = 1 << 0 #the buttons are configured for the gamepad
button2 = 1 << 1 #0 states that the first input in the gamepad is the first button and so on
button3 = 1 << 2
button4 = 1 << 3
button5 = 1 << 4
button6 = 1 << 5
button7 = 1 << 6
button8 = 1 << 7

pad = gamepad.GamePad( #Gamepad is initialized
    btn1, # buttons are given in a order here you can swap button variable names if you connect say the third button to the pin of the fourth one
    btn2,
    btn3,
    btn4,
    btn5,
    btn6,
    btn7,
    btn8,
)
adc1 = analogio.AnalogIn(board.GP27) #one of the two potentiometers is initialized and is pointed to GP27
adc2 = analogio.AnalogIn(board.GP26) #PS potentiometers and other analogio only works on the pins GP26, GP27 and GP28
led1 = digitalio.DigitalInOut(board.GP13) #the power led is initialized and is pointed to GP12
led1.direction = digitalio.Direction.OUTPUT #it is stated that the led is output device for the pico
led1.value = True #the led is turned on, this is a power led it indicates that the code on pico is running

led2 = digitalio.DigitalInOut(board.GP11)
led2.direction = digitalio.Direction.OUTPUT
led2.value = False #indicator led is turned off as if a program is stopped when it was on, then it wouldn't turn off until a button is pressed

last_monotonic_time = -1 #this is supposed to be the value used to store last time
sleep_monotonic_time = 0.01 #this is the value between when the keys are pressed and released. it is 10 miliseconds (0.01 seconds)

keyboard.press(Keycode.F19, Keycode.Z) #it presses the keys f19 and z
now_start = time.monotonic() #it sets ongoing time as a variable
if now_start >= last_monotonic_time + sleep_monotonic_time: #checks if ongoing time is equal to last time + sleep time
    keyboard.release(Keycode.F19, Keycode.Z) #it releases the keys
    last_monotonic_time = now_start #it changes the value of last time to that of current ongoing time

while True:
    now = time.monotonic() #it sets ongoing time as a variable
    led2.value = False #it turns the led off.This is part of blink on key click. The led turns on when a key is pressed and is then turned off when the loop is rerun
    buttons = pad.get_pressed() #activates the gamepad
    if buttons & button1: #it detects if the first button is pressed
        led2.value = True #it turns the led off.This is part of blink on key click. The led turns on when a key is pressed and is then turned off when the loop is rerun
        keyboard.press(Keycode.F19, Keycode.A) #it presses the keys f19 and a
        if now >= last_monotonic_time + sleep_monotonic_time: #checks if ongoing time is equal to last time + sleep time
            keyboard.release(Keycode.F19, Keycode.A) #it releases the keys
            last_monotonic_time = now #it changes the value of last time to that of current ongoing time
    elif buttons & button2: #the same thing is done for the rest of the keys
        led2.value = True
        keyboard.press(Keycode.F19, Keycode.B)
        if now >= last_monotonic_time + sleep_monotonic_time:
            keyboard.release(Keycode.F19, Keycode.B)
            last_monotonic_time = now
    elif buttons & button3:
        led2.value = True
        keyboard.press(Keycode.F19, Keycode.C)
        if now >= last_monotonic_time + sleep_monotonic_time:
            keyboard.release(Keycode.F19, Keycode.C)
            last_monotonic_time = now
    elif buttons & button4:
        led2.value = True
        keyboard.press(Keycode.F19, Keycode.D)
        if now >= last_monotonic_time + sleep_monotonic_time:
            keyboard.release(Keycode.F19, Keycode.D)
            last_monotonic_time = now
    elif buttons & button5:
        led2.value = True
        keyboard.press(Keycode.F19, Keycode.E)
        if now >= last_monotonic_time + sleep_monotonic_time:
            keyboard.release(Keycode.F19, Keycode.E)
            last_monotonic_time = now
    elif buttons & button6:
        led2.value = True
        keyboard.press(Keycode.F19, Keycode.F)
        if now >= last_monotonic_time + sleep_monotonic_time:
            keyboard.release(Keycode.F19, Keycode.F)
            last_monotonic_time = now
    elif buttons & button7:
        led2.value = True
        keyboard.press(Keycode.F19, Keycode.G)
        if now >= last_monotonic_time + sleep_monotonic_time:
            keyboard.release(Keycode.F19, Keycode.G)
            last_monotonic_time = now
    elif buttons & button8:
        led2.value = True
        keyboard.press(Keycode.F19, Keycode.H)
        if now >= last_monotonic_time + sleep_monotonic_time:
            keyboard.release(Keycode.F19, Keycode.H)
            last_monotonic_time = now
    time.sleep(0.05) #this is time between two runs of the main loop
    adc1_converted = math.floor(adc1.value / 64) #this converts the value of first potentiometer such that it is useable by deej
    adc2_converted = math.floor(adc2.value / 64) #this converts the value of second potentiometer such that it is useable by deej
    print(str(adc1_converted) + "|" + str(adc2_converted)) #this prints the values of both the potentiometers to the serial monitor which is then read by deej
    while buttons: #this is time for buttons to get clicked and also prevents debouncing of the keys
        buttons = pad.get_pressed()
        time.sleep(0.05)
