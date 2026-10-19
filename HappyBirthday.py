#HappyBirthday.py
import time
from machine import Pin, PWM
import machine, time

SPEAKER_GPIO = 18

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

WHOLE = 1
HALF = 1/2
QUARTER = 1/4
EIGHTH = 1/8
SIXTEENTH = 1/16
speaker = PWM(Pin(SPEAKER_GPIO))



def playNote(note,length):
    PWM = int(((2**16)-1)/8)
    speaker.freq(note)
    speaker.duty_u16(PWM)
    time.sleep(length)
    speaker.duty_u16(0)
    time.sleep(0.2)
def HappyBirthday():
    playNote(G3,EIGHTH+SIXTEENTH)
    playNote(G3,SIXTEENTH)
    playNote(A3,QUARTER)
    playNote(G3,QUARTER)
    playNote(C4,QUARTER)
    playNote(B3,HALF)
    playNote(G3,EIGHTH+SIXTEENTH)
    playNote(G3,SIXTEENTH)
    playNote(A3,QUARTER)
    playNote(G3,QUARTER)
    playNote(D4,QUARTER)
    playNote(C4,HALF)
    playNote(G3,EIGHTH+SIXTEENTH)
    playNote(G3,SIXTEENTH)
    playNote(G4,QUARTER)
    playNote(E4,QUARTER)
    playNote(C4,QUARTER)
    playNote(B3,QUARTER)
    playNote(A3,HALF)
    playNote(F4,EIGHTH+SIXTEENTH)
    playNote(F4,SIXTEENTH)
    playNote(E4,QUARTER)
    playNote(C4,QUARTER)
    playNote(D4,QUARTER)
    playNote(C4,1)
    
HappyBirthday()

