import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QProgressBar
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt
import serial
#from gpiozero import Button

import signal
import RPi.GPIO as GPIO

UARTRX_GPIO = 10 

'''
def signal_handler(sig, frame):
    GPIO.cleanup()
    #sys.exit(0)

def uart_input(channel):
    print("Signal Read")
    # read signal
    # return data?
'''

class ElectricCarDashboard(QWidget):


    def __init__(self):
        super().__init__()

        #Stuff to by controlled by GPIO
        self.AMS_Fault = False
        self.ECU_Fault = False
        self.IMD_Fault = False

        self.Speed = 0
        self.Voltage = 0
        self.BrakePercent = 50
        self.ThrottlePercent = 50


        #UI Look Stuff
        self.indicator_box_size = 75
        self.font_details = QFont('Arial', 10)


        self.init_ui()





    def init_ui(self):

        #QApplication.setFont(self.font_details)


        # Speedometer Layout Stuff
        self.SpeedometerLayout = QVBoxLayout()

        self.speed_label = QLabel('Speed: 69 mph')
        self.speed_label.setAlignment(Qt.AlignCenter)

        self.voltage_label = QLabel('Voltage: 69 V')
        self.voltage_label.setAlignment(Qt.AlignCenter)

        self.SpeedometerLayout.addWidget(self.speed_label)
        self.SpeedometerLayout.addWidget(self.voltage_label)


        #Updates Speedometer Data
        self.update_Voltage(self.Speed)
        self.update_Speed(self.Speed)


        # Fault Status Indicator Layout
        self.status_boxes_layout = QVBoxLayout()
        self.AMS_indicator = QLabel()
        self.ECU_indicator = QLabel()
        self.IMD_indicator = QLabel()

        self.AMS_label = QLabel('AMS Fault')
        self.ECU_label = QLabel('ECU Fault')
        self.IMD_label = QLabel('IMD Fault')

        self.status_boxes_layout.addWidget(self.AMS_label)
        self.status_boxes_layout.addWidget(self.AMS_indicator)
        self.status_boxes_layout.addWidget(self.ECU_label)
        self.status_boxes_layout.addWidget(self.ECU_indicator)
        self.status_boxes_layout.addWidget(self.IMD_label)
        self.status_boxes_layout.addWidget(self.IMD_indicator)
        self.status_boxes_layout.setAlignment(Qt.AlignLeft)

        #Updates the indicator
        self.update_AMS_indicator(0)
        self.update_IMD_indicator(0)
        self.update_ECU_indicator(0)


        # Throttle and brake Bars
        self.bars_layout = QHBoxLayout()


        self.brake_layout = QVBoxLayout()
        self.brake_bar = QProgressBar(self)
        self.brake_bar.setGeometry(200, 80, 250, 20)
        self.brake_bar.setValue(100)
        self.brake_bar.setOrientation(Qt.Vertical)
        #self.brake_bar.setAlignment(Qt.AlignCenter)

        self.brake_label = QLabel('Brakes')
        #self.brake_label.setAlignment(Qt.AlignCenter)
        self.brake_layout.addWidget(self.brake_label)
        self.brake_layout.addWidget(self.brake_bar)


        self.throttle_layout = QVBoxLayout()
        self.throttle_bar = QProgressBar(self)
        self.throttle_bar.setGeometry(200, 80, 250, 20)
        self.throttle_bar.setValue(100)
        self.throttle_bar.setOrientation(Qt.Vertical)

        self.throttle_label = QLabel('Throttle')
        #self.throttle_label.setAlignment(Qt.AlignCenter)
        self.throttle_layout.addWidget(self.throttle_label)
        self.throttle_layout.addWidget(self.throttle_bar)

        self.update_Throttle(self.ThrottlePercent)
        self.update_Brakes(self.BrakePercent)

        self.bars_layout.addLayout(self.brake_layout)
        self.bars_layout.addWidget(QLabel())
        self.bars_layout.addLayout(self.throttle_layout)





        # Final Layout
        hbox = QHBoxLayout()
        hbox.addLayout(self.status_boxes_layout)
        hbox.addLayout(self.SpeedometerLayout)
        hbox.addLayout(self.bars_layout)


        self.setLayout(hbox)

        self.setWindowTitle('Dashboard')
        self.setFont(self.font_details)
        self.setStyleSheet("background-color: gray;")
        self.setGeometry(100, 100, 800, 400)
        self.show()

    def update_Speed(self, value):
        #ADD CODE LATER TO PROCESS DATA
        self.speed_label.setText(f'Speed: {value} Mph')

    def update_Voltage(self, value):
        #ADD CODE LATER TO PROCESS DATA
        self.voltage_label.setText(f'Battery Level: {value}V')

    def update_AMS_indicator(self, value):
        #ADD CODE LATER TO PROCESS DATA
        self.AMS_Fault = value
        color = 'green' if self.AMS_Fault else 'red'
        style = f'background-color: {color}; border: 1px solid black;'

        self.AMS_indicator.setFixedWidth(self.indicator_box_size)
        self.AMS_indicator.setFixedHeight(self.indicator_box_size)
        self.AMS_indicator.setStyleSheet(style)

    def update_IMD_indicator(self, value):
        #ADD CODE LATER TO PROCESS DATA
        self.IMD_Fault = value
        color = 'green' if self.IMD_Fault else 'red'
        style = f'background-color: {color}; border: 1px solid black;'

        self.IMD_indicator.setFixedWidth(self.indicator_box_size)
        self.IMD_indicator.setFixedHeight(self.indicator_box_size)
        self.IMD_indicator.setStyleSheet(style)

    def update_ECU_indicator(self, value):
        #ADD CODE LATER TO PROCESS DATA
        self.ECU_Fault = value
        color = 'green' if self.ECU_Fault else 'red'
        style = f'background-color: {color}; border: 1px solid black;'

        self.ECU_indicator.setFixedWidth(self.indicator_box_size)
        self.ECU_indicator.setFixedHeight(self.indicator_box_size)
        self.ECU_indicator.setStyleSheet(style)

    def update_Brakes(self, value):
        #ADD CODE LATER TO PROCESS DATA
        self.brake_bar.setValue(value)

    def update_Throttle(self, value):
        #ADD CODE LATER TO PROCESS DATA
        self.throttle_bar.setValue(value)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    electric_car_dashboard = ElectricCarDashboard()

    functions = [

        ["speed", "update_Speed"],

        ["voltage", "update_Voltage"],

        ["AMS", "update_AMS_indicator"],

        ["IMD", "update_IMD_indicator"],

        ["ECU", "update_ECU_indicator"],

        ["ECU", "update_ECU_indicator"],

        ["brakes", "update_Brakes"],

        ["throttle", "update_Throttle"]

    ]

    # UART code here
    pass
    '''
    # Borrowed from https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/#Python_code_with_RPiGPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(UARTRX_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(UARTRX_GPIO, GPIO.FALLING, 
            callback=uart_input, bouncetime=100)

    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

    '''

    
    ser = serial.Serial('/dev/tty1', 115200, timeout=1) #Probably wrong name, maybe wrong baudrate
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            read_data = line
            print(line)

            function_information = read_data.split(",")

            for function in functions:
                if function[0] == function_information[0]:
                    funk = getattr(electric_car_dashboard, function[1])
                    funk(int(function_information[1]))
                    #locals()[function[1]](int(function_information[1])) # maybe should be globals() ?
    
    


    '''
    ser = serial.Serial(
        # Serial Port to read the data from
        port='/dev/ttyAMA0',
 
        #Rate at which the information is shared to the communication channel
        baudrate = 9600,
   
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
 
       # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
     
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
 
        # Number of serial commands to accept before timing out
        timeout=1
    )
        # Pause the program for 1 second to avoid overworking the serial port
    while 1:
        x=ser.readline()
        read_data = x
    '''

    '''
    read_data = ("throttle,12") #example
    function_information = read_data.split(",")

    for function in functions:
        if function[0] == function_information[0]:
            funk = getattr(electric_car_dashboard, function[1])
            funk(int(function_information[1]))
            #locals()[function[1]](int(function_information[1])) # maybe should be globals() ?
    
    sys.exit(app.exec_())
    '''
    
    
