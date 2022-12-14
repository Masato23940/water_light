import time
from ADCDevice import *

class Potentionmeter:
  def __init__(self):
    self.Vref = 3.3
    self.adc = ADCDevice()
    self.setup_adc()
  
  def setup_adc(self):
    if(self.adc.detectI2C(0x48)):
      self.adc = PCF8591()
    elif(self.adc.detectI2C(0x4b)):
      self.adc = ADS7830()
    else:
      print("No correct I2C address found, \n"
      "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
      "Program Exit. \n");
      exit(-1)

  def read_voltage(self):
    value = self.adc.analogRead(0) # read the ADC value of channel 0
    voltage = value / 255.0 * self.Vref # calculate the voltage value
    print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
    time.sleep(0.1)
    return voltage

  def destroy(self):
    self.adc.close()

if __name__ == "__main__":
  potentionmeter = Potentionmeter()
  print('system start')
  try:
      while True:
          potentionmeter.read_voltage()
          
  except KeyboardInterrupt:
      potentionmeter.destroy()
    

    

