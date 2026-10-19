# HW5solenoid.py
# Purpose: Cycle solenoid on for 20 minutes, off 10 minutes, using GP19 to activate a transistor
# Method: Off, Energize, Denergize states defined and used to allow toggling of cycles with
# the press of a button.
# Author: Gabriel Ferrer Llave

from machine import Pin
from HW5_solenoideventmanager import Event, Manager # imports user module HW5_solenoideventmanager
import time

# Define Pin Constants
GP19 = const(19)
GP20 = const(20)

# Define States as constant values
STATE_OFF = const(0)
STATE_CYCLE_ON = const(1)
STATE_CYCLE_OFF = const(2)

# Define Solenoid on/off cycle durations
SOLENOID_ON = const(5000)
SOLENOID_OFF = const(2500)

# Enable/Disable Debug Mode, as well as debug statuses as a list
DEBUG = True

STATE_STATUS = ['STATE_OFF','STATE_CYCLE_ON','STATE_CYCLE_OFF']

# Define pin for solenoid transistor as a Pin Object
solenoid = Pin(GP19,Pin.OUT)

# Define function for printing error messages
def error(e_msg):
    raise Exception(e_msg)

"""
event_processor defines an event processor for the program.
event_processor compares current event to current state, and
makes decisions based on that information. It will then return the
new state based on those actions.

If current state/event combination
does not match recognized combinations, event_processor returns an error message.

"""
def event_processor(state, event):
    if state == STATE_OFF:
        if event == Event.PRESSED:
            solenoid.on()
            manager.timer_set(SOLENOID_ON, periodic = False)
            return STATE_CYCLE_ON
        else:
            error('Unexpected event in state STATE_OFF')
    elif state == STATE_CYCLE_ON:
        if event == Event.PRESSED:
            solenoid.off()
            manager.timer_cancel()
            return STATE_OFF
        elif event == Event.TIMER:
            solenoid.off()
            manager.timer_set(SOLENOID_OFF, periodic = False)
            return STATE_CYCLE_OFF
        else:
            error('Unexpected event in state STATE_CYCLE_ON')
    elif state == STATE_CYCLE_OFF:
        if event == Event.PRESSED:
            solenoid.off()
            manager.timer_cancel()
            return STATE_OFF
        elif event == Event.TIMER:
            solenoid.on()
            manager.timer_set(SOLENOID_ON, periodic = False)
            return STATE_CYCLE_ON
        else:
            error('Unexpected event in state STATE_CYCLE_OFF')
    else:
        error('ERROR: Unrecognized state')
    
# Initial Conditions. Ensures solenoid and states are set to OFF positions
solenoid.off()
state = STATE_OFF
    
# Main Code

# prints states if Debug mode is on
if DEBUG: print(STATE_STATUS[state])

# Defines Manager object (see HW_solenoideventmanager.py)
manager = Manager(GP20)
    
while True:
    event = manager.next()
    # Below code returns the new state using event_processor,
    # Feeds it to the Debug mode printer, and then defines
    # It as the state variable to be fed back into
    # event_processor if a new event occurs.
    if event != Event.NONE:
        if DEBUG: print(Event.status(event), end = "")
        state_new = event_processor(state,event)
        if DEBUG: print("->"+STATE_STATUS[state_new])
        state = state_new
        
            
        


