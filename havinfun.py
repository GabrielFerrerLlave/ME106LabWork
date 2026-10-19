#Fidget.py
import time
from machine import Pin, PWM
import machine, time

PIN_BUZZER = 18

REST = const(0)
C3   = const(131)
CS3  = const(139)
D3   = const(147)
DS3  = const(156)
E3   = const(165)
F3   = const(175)
FS3  = const(185)
G3   = const(196)
GS3  = const(208)
A3   = const(220)
AS3  = const(233)
B3   = const(247)
C4   = const(262)
D4 = const(294)
E4 = const(330)
G4 = const(392)
F4 = const(349)
PIN_20 = 20
PIN_21 = 21
PIN_22 = 22

buttons = [Pin(PIN_20,Pin.IN),Pin(PIN_21,Pin.IN), Pin(PIN_22,Pin.IN)]
BUZZER_DUTY = int((2**16-1)/5)
buzzerPWM = PWM(Pin(PIN_BUZZER))

while True:
    if not buttons[0].value() and buttons[1].value() and buttons[2].value():
        buzzerPWM.freq(C3)
        buzzerPWM.duty_u16(BUZZER_DUTY)
    if buttons[0].value and not buttons[1].value() and buttons[2].value():
        buzzerPWM.freq(F3)
        buzzerPWM.duty_u16(BUZZER_DUTY)
    if buttons[0].value and buttons[1].value() and not buttons[2].value():
        buzzerPWM.freq(A3)
        buzzerPWM.duty_u16(BUZZER_DUTY)
    buzzerPWM.deinit()
