from gpiozero import PWMLED, Button
from signal import pause
from time import sleep

class ButtonPressRelease :
    def __init__(self) :
        self.button = Button(2)
        self.led = PWMLED(17)
    
    def continuously_listen(self):
        while True:
            if self.button.is_pressed :
                self.print_message_pressed()
            else :
                self.print_message_released()
                
    def wait_for_being_pressed(self):
        self.button.wait_for_press()
        self.print_message_pressed(False)
        
    def when_pressed_or_released_print_something(self):
         self.button.when_pressed = self.print_message_pressed
         self.button.when_released = self.print_message_released
         pause()
         
    def turn_on_off_led(self):        
        self.button.when_released = self.turn_off_led
        self.button.when_pressed = self.led_pulse
        pause()
        
    def print_message_pressed(self, is_continous = True):
        if is_continous :
            tense = "is"
        else :
            tense = "was"
        print("Button " + tense + " pressed.")
        
    def print_message_released(self):
        print("Button is released.")
        
    def led_pulse(self):
        self.print_message_pressed(True)
        self.led.pulse()
    
    def turn_off_led(self):
        self.print_message_released()
        self.led.off()
        
if __name__ == "__main__" :
    btn = ButtonPressRelease()
    #btn.wait_for_being_pressed()
    #btn.continuously_listen()
    #btn.when_pressed_or_released_print_something()
    btn.turn_on_off_led()