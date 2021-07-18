# Simple test of one line sensor to see if it can distingush a black line from a white paper
from gpiozero import LineSensor
from time import sleep

sensor = LineSensor(4)

def linefound():
    print("found line")

def linelost():
    print("line is lost")
    
#purposely switched roles 
sensor.when_line = linelost
sensor.when_no_line = linefound

