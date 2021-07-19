import RPi.GPIO as GPIO
from time import sleep
x = 100
x2 = 50
#en changes speed of motor
enA = 25
enB = 16
enC = 26
enD = 22
#bottom right motor - motor1
in1 = 24
in2 = 23
#top right motor - motor 2
in3 = 20
in4 = 21
#top left motor - motor 3
in1_2 = 19
in2_2 = 13
#bottom left motor - motor 4
in3_2 = 17
in4_2 = 27

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
#motor 3
GPIO.setup(in1_2,GPIO.OUT)
GPIO.setup(in2_2,GPIO.OUT)
GPIO.setup(enC,GPIO.OUT)
p3 = GPIO.PWM(enC,1000)
p3.start(25)
#motor 4
GPIO.setup(in3_2,GPIO.OUT)
GPIO.setup(in4_2,GPIO.OUT)
GPIO.setup(enD,GPIO.OUT)
p4 = GPIO.PWM(enD,1000)
p4.start(25)

def forward():
    print("going forwards")
    p1.ChangeDutyCycle(x)
    p2.ChangeDutyCycle(x)
    p3.ChangeDutyCycle(x)
    p4.ChangeDutyCycle(x)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in1_2,GPIO.LOW)
    GPIO.output(in2_2,GPIO.HIGH)
    GPIO.output(in3_2,GPIO.LOW)
    GPIO.output(in4_2,GPIO.HIGH)

def backward():
    print("going backwards")
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in1_2,GPIO.HIGH)
    GPIO.output(in2_2,GPIO.LOW)
    GPIO.output(in3_2,GPIO.HIGH)
    GPIO.output(in4_2,GPIO.LOW)

def stop():
    print("stopping")
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in1_2,GPIO.LOW)
    GPIO.output(in2_2,GPIO.LOW)
    GPIO.output(in3_2,GPIO.LOW)
    GPIO.output(in4_2,GPIO.LOW)

def turn_left():
    print("turning left")
    p3.ChangeDutyCycle(x2)
    p4.ChangeDutyCycle(x2)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in1_2,GPIO.HIGH)
    GPIO.output(in2_2,GPIO.LOW)
    GPIO.output(in3_2,GPIO.HIGH)
    GPIO.output(in4_2,GPIO.LOW)

def turn_right():
    print("turning right")
    p1.ChangeDutyCycle(x2)
    p2.ChangeDutyCycle(x2)
    p3.ChangeDutyCycle(x)
    p4.ChangeDutyCycle(x)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in1_2,GPIO.LOW)
    GPIO.output(in2_2,GPIO.HIGH)
    GPIO.output(in3_2,GPIO.LOW)
    GPIO.output(in4_2,GPIO.HIGH)


while(1):

    command = input("Enter 's' to start the rover: ")

    if command == 's':
        forward()
        sleep(3)
        backward()
        sleep(3)
        stop()
        sleep(3)
        turn_left()
        sleep(7)
        turn_right()
        sleep(7)
        stop()
    else:
        print("You entered the wrong command. Try again")
