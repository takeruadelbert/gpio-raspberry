from gpiozero import TrafficLights, Button
from time import sleep
from signal import pause

class TrafficLight:
    def __init__(self):
        self.traffic_light = TrafficLights(2,3,4)
        self.button = Button(14)
        
    def print_pressed_button_message(self):
        print("Button is pressed.")
    
    def print_released_button_message(self):
        print("Button is released.")
    
    def simulation(self):
        status = self.button.is_pressed
        while status == True :
            cont_status = self.button.is_pressed
            if cont_status == False :
                break;
            self.traffic_light.green.on()
            sleep(3)
            if cont_status == False :
                break;
            self.print_pressed_button_message()
            self.traffic_light.green.off()
            self.traffic_light.amber.on()
            sleep(1)
            if cont_status == False :
                break;
            self.traffic_light.amber.off()
            self.traffic_light.red.on()
            sleep(3)
            if cont_status == False :
                break;
            self.traffic_light.amber.on()
            sleep(1)
            if cont_status == False :
                break;
            self.traffic_light.green.on()
            self.traffic_light.amber.off()
            self.traffic_light.red.off()
    
    def turn_off_all_light(self):
        print(self.button.is_pressed)
        self.print_released_button_message()
        self.traffic_light.green.off()
        self.traffic_light.amber.off()
        self.traffic_light.red.off()
    
    def testing(self):
        self.button.when_pressed = self.simulation
        self.button.when_released = self.turn_off_all_light
        pause()

if __name__ == "__main__" :
    light = TrafficLight()
    light.testing()