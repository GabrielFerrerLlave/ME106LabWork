# HW5_solenoideventmanager.py
# Purpose: Manages events fed by originator program(HW5solenoid.py).
# Method: Defines Waiting, Button Press, and Cycling actions as events and
# manipulates them into performing actions, as well as returning the event
# status to be used for the state machine program
import micropython, machine
from machine import Pin, Timer

# Allows for micropython to provide errors for
# interruptions
micropython.alloc_emergency_exception_buf(100)

"""
Define Event Class. NONE corresponds to there being no event
when the event manager checks what has occurred. AKA
no button presses, no timers timing out, and no
state changing required.

PRESSED refers to when the button variable is pressed

TIMER refers to when a timer expires

"""
class Event():
    
    NONE = const(0)
    
    PRESSED = const(1)
    
    TIMER = const(2)
    
    def status(n):
        return('NONE','PRESSED', 'Timer')[n]
    

# Define error function to skip input if timer
# attempted to be set when on already exists

class TimerinUseException(Exception):
    pass

# Defines Manager class. This is used to perform actions based on
# a given event
class Manager():
    # Initialization Function
    def __init__(self, PIN_BUTTON):
        self.queue = list()
        # Defines Pin object. Since we are dealing with Pico Pins,
        # Assume Pins are already pulled up
        self.button = machine.Pin(PIN_BUTTON, machine.Pin.IN)
        # Activate interrupt request. Originator program is interrupted if
        # the Pin's voltage is detected to be falling. The handler is the
        # actual function that occurs when an interrupt is requested.
        self.button.irq(trigger=machine.Pin.IRQ_FALLING,handler=self._isr_button,hard = False)
        
        # Ensures that no timer is occurring on initialization
        self.timer = None 
    # Adds PRESSED event to queue
    def _isr_button(self,pin):
        # Disables interrupt requester to avoid
        # critical section errors
        hide = machine.disable_irq()
        # Adds PRESSED event to event queue
        self.queue.append(Event.PRESSED)
        #re-enables interrupt requester
        machine.enable_irq(hide)
    # Adds TIMER event to queue, and preps for timer reset
    def _isr_timer(self,pin):
        # Disables interrupt requester
        hide = machine.disable_irq()
        # Adds TIMER event to event queue
        self.queue.append(Event.TIMER)
        # Sets timer to 0 so it can be reset
        self.timer = None
        # Re-enables interrupt requester
        machine.enable_irq(hide)
    # Resets Timer
    def timer_set(self, ms, periodic = False):
        if self.timer is None:
            # Sets timer
            self.timer = Timer(period = ms, mode = (Timer.PERIODIC if periodic else Timer.ONE_SHOT), callback = self._isr_timer) 
        else: #Error message if timer already in use when function called
            raise TimerinUseException()
    # Cancels Timer
    def timer_cancel(self):
        if self.timer is not None:
            self.timer.deinit()
            self.time = None
    # Calls next event and deletes it from queue
    def next(self):
        # Disables interrupt requester
        hide = machine.disable_irq()
        # stores next event in queue and deletes it, unless queue is empty
        # Then, returns None
        ev = self.queue.pop(0) if len(self.queue) else Event.NONE
        # Re-enables interrupt requester
        machine.enable_irq(hide)
        #returns next event
        return ev
        
    
    
    
    