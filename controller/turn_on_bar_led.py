import RPi.GPIO as GPIO
import time

ledPins = [7, 11, 13, 15, 12, 16, 18, 22, 24, 10]
#ledPins = [11]


class BarLED:
    def __init__(self, max_val = 100):
        self.GPIO = GPIO
        self.GPIO.setmode(GPIO.BOARD) # use Physical GPIO Numbering
        self.GPIO.setup(ledPins, GPIO.OUT) # set all ledPins to OUTPUT mode
        self.GPIO.output(ledPins, GPIO.HIGH) # make all ledPins output HIGH level, turn off all led
        self.isActivated = False
        self.max_value = max_val

    def turn_on_led(self, value):
        self.isActivated = True
        value_per_LED = self.max_value/len(ledPins)
        turn_on_led_num = round( value/value_per_LED )
        turn_off_led_num = len(ledPins)-turn_on_led_num
        for i in range(turn_on_led_num):
            GPIO.output(ledPins[i], GPIO.LOW)
        if turn_on_led_num != len(ledPins):
            for l in range(turn_on_led_num, len(ledPins)):
                GPIO.output(ledPins[l], GPIO.HIGH)

    def turn_off_led(self):
        self.GPIO.cleanup() # Release all GPIO

if __name__ == '__main__': # Program entrance
    print('Program is starting...')
    bar_led = BarLED()
    try:
        for num in range(0,110,10):
            bar_led.turn_on_led(num)
            time.sleep(1)
        bar_led.turn_off_led()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        bar_led.turn_off_led()