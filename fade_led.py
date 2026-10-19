import time
from machine import Pin, PWM

PIN_LED = const(0)

PWM_FREQ = const(1000)

MAX_POWER_OF_2 = const(16)

led_pwm = PWM(Pin(0))   # LED on GP0
led_pwm.freq(PWM_FREQ)

while True:
	for duty_exp in range(1, MAX_POWER_OF_2):
		duty = (2**duty_exp) - 1
		#print(duty)
		led_pwm.duty_u16(duty)
		time.sleep(0.1)