#!/usr/bin/env python3
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from RPi import GPIO as GPIO

from time import sleep, strftime
from datetime import datetime

pinButton = 36
pinLed = 38
num = 0

def get_cpu_temp():     # get CPU temperature and store it into file "/sys/class/thermal/thermal_zone0/temp"
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format( float(cpu)/1000 ) + ' C'
 
def get_time_now():     # get system time
    return datetime.now().strftime('    %H:%M:%S')

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pinLed, GPIO.OUT, initial=GPIO.HIGH)

def swAdd(ev=None):
    print("put the button")
    global num
    num += 1
    GPIO.output(pinLed, GPIO.LOW)
    sleep(0.2)
    GPIO.output(pinLed, GPIO.HIGH)

def loop():
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns
    while(True):         
        #lcd.clear()
        lcd.setCursor(0,0)  # set cursor position
        # lcd.message( 'CPU: ' + get_cpu_temp()+'\n' )# display CPU temperature
        if GPIO.input(pinButton) == GPIO.LOW:
            sleep(0.02)
            if GPIO.input(pinButton)==GPIO.LOW:
                while GPIO.input(pinButton)==GPIO.LOW:
                    pass
                swAdd()
                lcd.message(str(num))
        sleep(0.1)
        
def destroy():
    lcd.clear()
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
	mcp = PCF8574_GPIO(PCF8574_address)
except:
	try:
		mcp = PCF8574_GPIO(PCF8574A_address)
	except:
		print ('I2C Address Error !')
		exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

if __name__ == '__main__':
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

