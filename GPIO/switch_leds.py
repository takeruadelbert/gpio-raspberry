#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:55:39 2018

@author: takeru
"""

from gpiozero import Button, LEDBoard
from signal import pause

class SwitchLeds :
    def __init__(self) :
        self.button = Button(14)
        self.led = LEDBoard(2,3,4)
        self.counter = 0
    
    def get_all_leds(self):
        for led in self.led :
            print(led)
    
    def repeatly_turning_on_led(self):
        self.led[self.counter].on()
        message = "LED GPIO-" + str(self.counter) + " is on."
        print(message)
        for x in range(0, len(self.led)) :
            if x != self.counter :
                self.led[x].off()
                message = "LED GPIO-" + str(x) + " is off."
                print(message)
        if self.counter < 2 :
            self.counter += 1
        else :
            self.counter = 0
    
    def testing(self):
        self.button.when_pressed = self.repeatly_turning_on_led
        pause()

if __name__ == "__main__" :
    btn = SwitchLeds()
    btn.testing()