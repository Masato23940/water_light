import time
from controller.show_soilMoisture_5V import CSMS12
from controller.turn_on_bar_led import BarLED

class SeviceWaterLight
def __init__(self):
    self.bar_led = BarLED()

def serve(self):
    sensor = CSMS12()
    sensor.moisturePercentage()