#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


pinA = 3
pinB = 5
pinC = 15
pinD = 8
pinE = 10
pinF = 11
pinG = 12
pinDP = 13

pinButton = 18
pinLed = 22
sum = 0

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pinA, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(pinB, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(pinC, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(pinD, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(pinE, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(pinF, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(pinG, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(pinDP, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(pinLed, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(pinButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	# GPIO.add_event_detect(pinButton, GPIO.FALLING,callback=swAdd)
	print 'gpio init completed!'

def swAdd(ev=None):
	global sum
	GPIO.output(pinLed, GPIO.LOW)

	if sum<9:
		sum += 1
	elif sum == 9:
		sum = 0

	if sum == 0:
		display_0()
	elif sum == 1:
		display_1()
	elif sum == 2:
		display_2()
	elif sum == 3:
		display_3()	
	elif sum == 4:
		display_4()
	elif sum == 5:
		display_5()
	elif sum == 6:
		display_6()
	elif sum == 7:
		display_7()
	elif sum == 8:
		display_8()
	elif sum == 9:
		display_9()
	
	time.sleep(0.2)
	GPIO.output(pinLed, GPIO.HIGH)
	
	
def display_0():
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.HIGH)
	GPIO.output(pinE, GPIO.HIGH)
	GPIO.output(pinF, GPIO.HIGH)
	GPIO.output(pinG, GPIO.LOW)
	GPIO.output(pinDP, GPIO.LOW)
	print 'display number 0'

def display_1():
	GPIO.output(pinA, GPIO.LOW)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.LOW)
	GPIO.output(pinE, GPIO.LOW)
	GPIO.output(pinF, GPIO.LOW)
	GPIO.output(pinG, GPIO.LOW)
	GPIO.output(pinDP, GPIO.LOW)
	print 'display number 1'
	
	
def display_2():
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.LOW)
	GPIO.output(pinD, GPIO.HIGH)
	GPIO.output(pinE, GPIO.HIGH)
	GPIO.output(pinF, GPIO.LOW)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinDP, GPIO.LOW)
	print 'display number 2'
	
def display_3():
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.HIGH)
	GPIO.output(pinE, GPIO.LOW)
	GPIO.output(pinF, GPIO.LOW)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinDP, GPIO.LOW)
	print 'display number 3'	
	
def display_4():
	GPIO.output(pinA, GPIO.LOW)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.LOW)
	GPIO.output(pinE, GPIO.LOW)
	GPIO.output(pinF, GPIO.HIGH)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinDP, GPIO.LOW)
	print 'display number 4'	
	
def display_5():
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinB, GPIO.LOW)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.HIGH)
	GPIO.output(pinE, GPIO.LOW)
	GPIO.output(pinF, GPIO.HIGH)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinDP, GPIO.LOW)
	print 'display number 5'	
	
def display_6():
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinB, GPIO.LOW)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.HIGH)
	GPIO.output(pinE, GPIO.HIGH)
	GPIO.output(pinF, GPIO.HIGH)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinDP, GPIO.LOW)
	print 'display number 6'


def display_7():
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.LOW)
	GPIO.output(pinE, GPIO.LOW)
	GPIO.output(pinF, GPIO.LOW)
	GPIO.output(pinG, GPIO.LOW)
	GPIO.output(pinDP, GPIO.LOW)
	print 'display number 7'	
	
def display_8():
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.HIGH)
	GPIO.output(pinE, GPIO.HIGH)
	GPIO.output(pinF, GPIO.HIGH)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinDP, GPIO.LOW)
	print 'display number 8'	
	
	
def display_9():
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.HIGH)
	GPIO.output(pinE, GPIO.LOW)
	GPIO.output(pinF, GPIO.HIGH)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinDP, GPIO.LOW)
	print 'display number 9'
	
def display_dp():
	GPIO.output(pinA, GPIO.LOW)
	GPIO.output(pinB, GPIO.LOW)
	GPIO.output(pinC, GPIO.LOW)
	GPIO.output(pinD, GPIO.LOW)
	GPIO.output(pinE, GPIO.LOW)
	GPIO.output(pinF, GPIO.LOW)
	GPIO.output(pinG, GPIO.LOW)
	GPIO.output(pinDP, GPIO.HIGH)
	print 'display dp'

def clear():
	GPIO.output(pinA, GPIO.LOW)
	GPIO.output(pinB, GPIO.LOW)
	GPIO.output(pinC, GPIO.LOW)
	GPIO.output(pinD, GPIO.LOW)
	GPIO.output(pinE, GPIO.LOW)
	GPIO.output(pinF, GPIO.LOW)
	GPIO.output(pinG, GPIO.LOW)
	GPIO.output(pinDP, GPIO.LOW)
	print 'clear'

def loop():
	while True:
		if GPIO.input(pinButton) == GPIO.LOW:
			time.sleep(0.02)
			if GPIO.input(pinButton)==GPIO.LOW:
				while GPIO.input(pinButton)==GPIO.LOW:
					pass
				swAdd()
	
if __name__ == '__main__':
	try:
		init()
		loop()
	except KeyboardInterrupt:
		GPIO.output(pinLed,GPIO.HIGH)
		GPIO.cleanup()
		print 'Key Board Interrupt!'
		
	
