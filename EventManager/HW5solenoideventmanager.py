
import micropython, machine
from machine import Pin, Timer

micropython.alloc_emergency_exception_buf(100)

class Event():
    
    NONE = const(0)
    
    PRESSED = const(1)
    
    TIMER = const(2)
    
    def status(n):
        return('NONE','PRESSED', 'Timer')[n]
    
class TimerinUseException(Exception):
    pass
    
class Manager():
    
    def __init__(self, PIN_BUTTON):
        self.queue = list()
        
        self.button = machine.Pin(PIN_BUTTON, machin.PIN.IN)
        self.button.irq(trigger=machine.PIN.IRQ_FALLING,handler=self._isr_button,hard = False)
        
        self.timer = None 
    
    def _isr_button(self,pin):
        
        hide = machine.disable_irq()
        self.queue.append(Event.PRESSED)
        machine.enable_irq(hide)
    
    def _isr_timer(self,pin):
        hide = machine.disable_irq()
        self.queue.append(Event.TIMER)
        self.timer = None
        machine.enable_irq(hide)
    
    def timer_set(self, ms, periodic = False):
        if self.timer is None:
            self.timer = Timer(period = ms, mode = (Timer.PERIODIC if periodic else Timer.ONE_SHOT), callback = self._isr_timer) 
        else:
            raise TimerinUseException()
    def timer_cancel(self):
        if self.timer is not None:
            self.timer.deinit()
            self.time = None
    
    def next(self):
        hide = machine.diable_irq()
        ev = self.queue.pop(0) if len(self.queue) else Event.NONE
        machine.enable_irq(hide)
        
        return ev
        
    
    
    
    