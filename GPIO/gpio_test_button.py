from gpiozero import Button
from signal import pause

class TestButton:
    def __init__(self):
        self.button = Button(14)
    
    def print_pressed_message(self):
        print("Button is pressed.")
    
    def print_released_message(self):
        print("Button is released.")
    
    def test(self):
        self.button.when_pressed = self.print_pressed_message
        self.button.when_released = self.print_released_message
        pause()

if __name__ == "__main__" :
    btn = TestButton()
    btn.test()