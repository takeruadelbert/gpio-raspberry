from gpiozero import Button, LEDBoard
from signal import pause

class ButtonWithTwoLeds:
    def __init__(self):
        self.button = Button(4)
        self.led = LEDBoard(2,3)
        self.led[0].on()
    
    def print_message_button_pressed(self):
        print("Button is pressed.")
    
    def print_message_button_released(self):
        print("Button is released.")
        
    def turn_on_red(self):
        self.led[0].on()
    
    def turn_off_red(self):
        self.led[0].off()
    
    def turn_on_green(self):
        self.led[1].on()
        self.turn_off_red()
        self.print_message_button_pressed()
    
    def turn_off_green(self):
        self.led[1].off()
        self.turn_on_red()
        self.print_message_button_released()
    
    def testing(self):
        self.button.when_pressed = self.turn_on_green
        self.button.when_released = self.turn_off_green
        pause()

if __name__ == "__main__" :
    btn = ButtonWithTwoLeds()
    btn.testing()