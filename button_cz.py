#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
# Set #23 as LED pin
LedPinRed = 23
LedPinYellow = 17
LedPinGreen = 27
# Set #18 as button pin
ButtonPin = 18

# Set Led status to True(OFF)
Led_status = True

# Define a function to print message at the beginning
def print_message():
	print ("========================================")
	print ("|          Button control LED          |")
	print ("|      LEDRed connect to GPIO23        |")
	print ("|      LEDYellow connect to GPIO17     |")
	print ("|      LEDGreen connect to GPIO27      |")
	print ("|        Button connect to GPIO18      |")
	print ("|                                      |")
	print ("|   Press button to turn on/off LED.   |")
	print ("|                                      |")
	print ("========================================\n")
	print 'Program is running...'


# Define a setup function for some setup
def setup():
	# Set the GPIO modes to BCM Numbering
	GPIO.setmode(GPIO.BCM)
	# Set LedPin's mode to output, 
	# and initial level to high (3.3v)
	GPIO.setup(LedPinRed, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(LedPinYellow, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(LedPinGreen, GPIO.OUT, initial=GPIO.HIGH)
	# Set BtnPin's mode to input, 
	# and pull up to high (3.3V)
	GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	# Set up a falling detect on BtnPin, 
	# and callback function to swLed
	# GPIO.add_event_detect(ButtonPin, GPIO.FALLING, callback=swLed)
	

# Define a callback function for button callback
def swLed(ev=None):
	print("put the botton")

	GPIO.output(LedPinGreen, GPIO.LOW)
	GPIO.output(LedPinYellow, GPIO.HIGH)
	time.sleep(4)
	GPIO.output(LedPinGreen, GPIO.HIGH)
	GPIO.output(LedPinYellow, GPIO.LOW)
	time.sleep(2)
	GPIO.output(LedPinYellow, GPIO.HIGH)
	GPIO.output(LedPinRed, GPIO.LOW)
	GPIO.output(LedPinYellow, GPIO.HIGH)
	time.sleep(5)
	GPIO.output(LedPinRed, GPIO.HIGH)

		
	

# Define a main function for main process
def main():
	# Print messages
	print_message()
	while True:
		# Don't do anything.
		GPIO.output(LedPinYellow, GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(LedPinYellow, GPIO.HIGH)
		time.sleep(0.5)
		if(GPIO.input(ButtonPin)==GPIO.LOW):
			GPIO.output(LedPinYellow, GPIO.LOW)
			time.sleep(0.5)
			GPIO.output(LedPinYellow, GPIO.HIGH)
			time.sleep(0.5)
			swLed()
		

# Define a destroy function for clean up everything after
# the script finished 
def destroy():
	# Turn off LED
	GPIO.output(LedPinGreen, GPIO.HIGH)
	GPIO.output(LedPinYellow, GPIO.HIGH)
	GPIO.output(LedPinRed, GPIO.HIGH)
	# Release resource
	GPIO.cleanup()

# If run this script directly, do:
if __name__ == '__main__':
	setup()
	try:
		main()
	# When 'Ctrl+C' is pressed, the child program 
	# destroy() will be  executed.
	except KeyboardInterrupt:
		destroy()

