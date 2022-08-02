import RPi.GPIO as GPIO
import time

ledPins = [40, 38, 36, 32, 37, 35, 33, 31, 29 28]

class BarLED:
    def __init__(self):
        self.GPIO = GPIO
        self.GPIO.setmode(GPIO.BOARD) # use Physical GPIO Numbering
        self.GPIO.setup(ledPins, GPIO.OUT) # set all ledPins to OUTPUT mode
        self.GPIO.output(ledPins, GPIO.HIGH) # make all ledPins output HIGH level, turn off all led
        self.isActivated = False
        self.max_value = 100

    def turn_on_led(self, value):
        self.isActivated = True
        value_per_LED = self.max_value/len(ledPins)
        turn_on_led_num = round( value/value_per_LED )
        turn_off_led_num = len(ledPins)-turn_on_led_num
        for i = 1:turn_on_led_num
            GPIO.output(ledPins[i-1], GPIO.LOW)
        if turn_on_led_num =! len(ledPins)
            for l = turn_on_led_num+1:len(ledPins)
                GPIO.output(ledPins[i-1], GPIO.HIGH)

    def turn_off_led():
        GPIO.cleanup() # Release all GPIO

if __name__ == '__main__': # Program entrance
print ('Program is starting...')
bar_led = BarLED()
try:
    for i = 1:10:100
        bar_led.turn_on_led(i)
        time.sleep(1)
    bar_led.turn_off_led()
except KeyboardInterrupt: # Press ctrl-c to end the program.
    bar_led.turn_off_led()