import requests, sys
from gpiozero import LEDBoard
from signal import pause
from time import sleep

class TestAPI :
    def __init__(self, ip_address) :
        self.ip_address = ip_address
        self.led = LEDBoard(2,3)
        self.delay = 3 # in seconds
    
    def get_api_response(self, url):
        try:
            response = requests.get(self.ip_address + url)
            response.raise_for_status()
            data_json = response.json()
            return data_json
        except requests.exceptions.HTTPError as err:
            print(err)
            sys.exit(1)
    
    def api_list_employee(self, url) :
        data_json = self.get_api_response(url)
        if data_json['status'] == 206 :
            data_employee = data_json['data']
            for emp_id, emp_name in data_employee.items() :
                print("SSN : " + str(emp_id))
                print("Name : " + emp_name + "\n")
        else :
            return "No Data"
                
    def api_check_employee(self, url_check_employee) :
        try :
            response = requests.get(self.ip_address + url_check_employee)
            response.raise_for_status()
            data_json = response.json()
            print(data_json['message'])
            if data_json['status'] == 205 :
                color = "green"
            else :
                color = "red"
            self.turn_on_led(color)
        except requests.exceptions.HTTPError as err :
            print(err)
            self.turn_on_led("red")
            sys.exit(1)
    
    def turn_on_led(self, color):
        if color == "green" :
            self.led[1].on()
        else :
            self.led[0].on()
        sleep(self.delay)
        self.turn_off_all_led()
    
    def turn_off_all_led(self):
        self.led[0].off()
        self.led[1].off()

if __name__ == "__main__" :
    ip_address = "http://192.168.1.201"
    #url = "/vms/api/get-employees"
    #emp_ssn = "485112533"
    api = TestAPI(ip_address)
    while True :
        #emp_ssn = input("Employee SSN : ")
        #barcode = input("Barcode : ")
        barcode = str(input("Scan Barcode : "))
        if barcode != "" :
            #url_check_emp = "/vms/api/check-employee?ssn=" + str(emp_ssn)
            url_check_validity = "/vms/api/check-validity?barcode=" + str(barcode)
            api.api_check_employee(url_check_validity)
        else :            
            print("Invalid Barcode!")
            api.turn_on_led("red")
        print("\n")