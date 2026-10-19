import time
from machine import Pin, PWM

BUZZER_DUTY = int((2**16-1)/8)
PIN_PWM = 0
pwm = PWM(Pin(PIN_PWM,Pin.OUT))
pwm.duty_u16(BUZZER_DUTY)

for f in range(100,15000,100):
    pwm.freq(f)
    time.sleep(0.25)
