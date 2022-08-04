import sys
sys.path.append('../')
import time
#from controller.show_soilMoisture_5V import CSMS12
from controller.turn_on_bar_led import BarLED
from controller.show_voltage_3p3V import Potentionmeter

class SeviceWaterLight:
  def __init__(self):
    self.isWatering = False
    
  def serve(self):
    potentionmeter = Potentionmeter()
    #sensor.moisturePercentage()
    bar_led = BarLED(3.3)
    start_time = time.time()
    
    while True:
      if time.time() - start_time > 20: # forcibly break 10 sec after pump start
        break
      voltage = potentionmeter.read_voltage()
      bar_led.turn_on_led(voltage)
      
    bar_led.turn_off_led()
    potentionmeter.destroy()

if __name__ == "__main__":
    water_light = SeviceWaterLight()
    water_light.serve()
