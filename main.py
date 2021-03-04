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

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(board.GP22)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = Pull.DOWN
btn2 = digitalio.DigitalInOut(board.GP21)
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


button1 = 1 << 0
button2 = 1 << 1
button3 = 1 << 2
button4 = 1 << 3
button5 = 1 << 4
button6 = 1 << 5
button7 = 1 << 6
button8 = 1 << 7

pad = gamepad.GamePad(
    btn1,
    btn2,
    btn3,
    btn4,
    btn5,
    btn6,
    btn7,
    btn8,
)
adc1 = analogio.AnalogIn(board.GP27)
adc2 = analogio.AnalogIn(board.GP26)
led1 = digitalio.DigitalInOut(board.GP13)
led1.direction = digitalio.Direction.OUTPUT
led1.value = True

led2 = digitalio.DigitalInOut(board.GP11)
led2.direction = digitalio.Direction.OUTPUT
led2.value = False

last_monotonic_time = -1
sleep_monotonic_time = 0.01

keyboard.press(Keycode.F19, Keycode.Z)
now_start = time.monotonic()
if now_start >= last_monotonic_time + sleep_monotonic_time:
    keyboard.release(Keycode.F19, Keycode.Z)
    last_monotonic_time = now_start

while True:
    now = time.monotonic()
    led2.value = False
    buttons = pad.get_pressed()
    if buttons & button1:
        led2.value = True
        keyboard.press(Keycode.F19, Keycode.A)
        if now >= last_monotonic_time + sleep_monotonic_time:
            keyboard.release(Keycode.F19, Keycode.A)
            last_monotonic_time = now
    elif buttons & button2:
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
    time.sleep(0.05)
    adc1_converted = math.floor(adc1.value / 64)
    adc2_converted = math.floor(adc2.value / 64)
    print(str(adc1_converted) + "|" + str(adc2_converted))
    while buttons:
        buttons = pad.get_pressed()
        time.sleep(0.05)