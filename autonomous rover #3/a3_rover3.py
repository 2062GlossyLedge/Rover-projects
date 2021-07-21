from gpiozero import LineSensor
import RPi.GPIO as GPIO
from time import sleep
x = 50
x1 = 0
x2 = 75
t = 0.25
#Left sensor
sensor1 = LineSensor(26)
#Right sensor
sensor2 = LineSensor(16)
enA = 25
enB = 12
#Left motor - motor1
in1 = 24
in2 = 23
#Right motor - motor2
in3 = 20
in4 = 21

GPIO.setmode(GPIO.BCM)
#motor 1
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
p1 = GPIO.PWM(enA,1000)
p1.start(25)
#motor 2
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
p2 = GPIO.PWM(enB,1000)
p2.start(25)

#Movement commands
def forward():
    print("going forwards")
    p1.ChangeDutyCycle(x)
    p2.ChangeDutyCycle(x)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
def turn_left():
    print("turning left")
    p1.ChangeDutyCycle(x1)
    p2.ChangeDutyCycle(x2)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
def turn_right():
    print("turning right")
    p1.ChangeDutyCycle(x2)
    p2.ChangeDutyCycle(x1)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
def stop():
    print("stopping")
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)


sensor1.when_line = turn_left()
sensor2.when_line = turn_right()
sensor1.when_no_line = forward()
sensor2.when_no_line = forward()


try:
    # Repeat the next indented block forever
    while True:
        sleep(10)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    print("Exiting")
    stop()