import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QProgressBar
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt
from gpiozero import Button


class ElectricCarDashboard(QWidget):


    def __init__(self):
        super().__init__()

        #Stuff to by controlled by GPIO
        self.AMS_Fault = False
        self.ECU_Fault = True
        self.IMD_Fault = False

        self.Speed = 0
        self.Voltage = 0
        self.BreakPercent = 50
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
        self.update_speed(self.Speed)


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
        self.update_AMS_indicator()
        self.update_IMD_indicator()
        self.update_ECU_indicator()


        # Throttle and Break Bars
        self.bars_layout = QHBoxLayout()


        self.break_layout = QVBoxLayout()
        self.break_bar = QProgressBar(self)
        self.break_bar.setGeometry(200, 80, 250, 20)
        self.break_bar.setValue(100)
        self.break_bar.setOrientation(Qt.Vertical)
        #self.break_bar.setAlignment(Qt.AlignCenter)

        self.break_label = QLabel('Breaks')
        #self.break_label.setAlignment(Qt.AlignCenter)
        self.break_layout.addWidget(self.break_label)
        self.break_layout.addWidget(self.break_bar)


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
        self.update_Breaks(self.BreakPercent)

        self.bars_layout.addLayout(self.break_layout)
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
        self.setGeometry(100, 100, 600, 600)
        self.show()

    def update_speed(self, value):
        #ADD CODE LATER TO INTERFACE WITH GPIO PINS
        self.speed_label.setText(f'Speed: {value} Mph')

    def update_Voltage(self, value):
        #ADD CODE LATER TO INTERFACE WITH GPIO PINS
        self.voltage_label.setText(f'Battery Level: {value}V')

    def update_AMS_indicator(self):
        #ADD CODE LATER TO INTERFACE WITH GPIO PINS
        color = 'green' if self.AMS_Fault else 'red'
        style = f'background-color: {color}; border: 1px solid black;'

        self.AMS_indicator.setFixedWidth(self.indicator_box_size)
        self.AMS_indicator.setFixedHeight(self.indicator_box_size)
        self.AMS_indicator.setStyleSheet(style)

    def update_IMD_indicator(self):
        #ADD CODE LATER TO INTERFACE WITH GPIO PINS
        color = 'green' if self.IMD_Fault else 'red'
        style = f'background-color: {color}; border: 1px solid black;'

        self.IMD_indicator.setFixedWidth(self.indicator_box_size)
        self.IMD_indicator.setFixedHeight(self.indicator_box_size)
        self.IMD_indicator.setStyleSheet(style)

    def update_ECU_indicator(self):
        #ADD CODE LATER TO INTERFACE WITH GPIO PINS
        color = 'green' if self.ECU_Fault else 'red'
        style = f'background-color: {color}; border: 1px solid black;'

        self.ECU_indicator.setFixedWidth(self.indicator_box_size)
        self.ECU_indicator.setFixedHeight(self.indicator_box_size)
        self.ECU_indicator.setStyleSheet(style)

    def update_Breaks(self, value):
        #ADD CODE LATER TO INTERFACE WITH GPIO PINS
        self.break_bar.setValue(value)

    def update_Throttle(self, value):
        #ADD CODE LATER TO INTERFACE WITH GPIO PINS
        self.throttle_bar.setValue(value)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    electric_car_dashboard = ElectricCarDashboard()
    sys.exit(app.exec_())
