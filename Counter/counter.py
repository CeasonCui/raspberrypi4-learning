#!/usr/bin/env python3
import RPi.GPIO as GPIO
import Keypad       #import module Keypad

from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

from time import sleep

ROWS = 4        # number of rows of the Keypad
COLS = 4        #number of columns of the Keypad
keys =  [   '1','2','3','+',    #key code
            '4','5','6','-',
            '7','8','9','x',
            'C','0','=','/'     ]
rowsPins = [12,16,22,32]        #connect to the row pinouts of the keypad
colsPins = [19,15,13,11]        #connect to the column pinouts of the keypad

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

lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

def loop():
    keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)    #creat Keypad object
    keypad.setDebounceTime(50)      #set the debounce time
    mcp.output(3,1)
    lcd.begin(16,2)
    key_list=[]
    while(True):
        key = keypad.getKey()       #obtain the state of keys
        
        if(key != keypad.NULL and key !='C'):     #if there is key pressed, print its key code.
            print ("You Pressed Key : %c "%(key))
            key_list.append(key)
            lcd.setCursor(0,0)  # set cursor position
            lcd.message(key_list)   # display the time
        elif (key == 'C'):
            print ("You Pressed Key : %c "%(key))
            lcd.clear()
            key_list = []
        i = 0
        A_sum = 0.00
        B_sum = 0.00
        sum = 0.00
        func = 0
        if (key == '='):
            while(True):
                A_sum = A_sum*10 + int(key_list[i])
                i+=1
                if(key_list[i]=='+' or key_list[i]=='-' or key_list[i]=='x' or key_list[i]=='/'):
                    break
            print('A_sum:',A_sum)

            if (key_list[i]=='+'):
                func = 1
            elif (key_list[i]=='-'):
                func = 2
            elif (key_list[i]=='x'):
                func = 3
            elif (key_list[i]=='/'):
                func = 4
                        
            i+=1        
            
            while(True):
                B_sum = B_sum*10 + int(key_list[i])
                i+=1
                if(key_list[i]=='=' and func != 0):     
                    if(func == 1):
                        sum = A_sum + B_sum
                    elif(func == 2):
                        sum = A_sum - B_sum
                    elif(func == 3):
                        sum = A_sum * B_sum
                    elif(func == 4):
                        sum = A_sum / B_sum
                    lcd.message(str(sum))
                    break
            print('B_sum:',B_sum)
            print('sum:',sum)

        # if(key == '+'):
        #     key_A = key_list[:-1]
        #     # print(len(key_A))
        #     i=0
        #     A_sum = 0
        #     while (i<len(key_A)):
        #         A_sum = A_sum*10+int(key_A[i])
        #         i+=1
            


        sleep(0.1)
        
            
if __name__ == '__main__':     #Program start from here
    print ("Program is starting ... ")
    try:
        loop()
    except KeyboardInterrupt:  #When 'Ctrl+C' is pressed, exit the program. 
        GPIO.cleanup()
