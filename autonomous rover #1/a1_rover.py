#Motor control forwards and backwards 
import RPi.GPIO as io
from time import sleep

in1 = 24
in2 = 23
enA = 25

in3 = 20
in4 = 21
enB = 16

io.setmode(io.BCM)

#First motor
io.setup(in3,io.OUT)
io.setup(in4,io.OUT)
io.setup(enB,io.OUT)
io.output(in3,io.LOW)
io.output(in4,io.LOW)
p2_dt = io.PWM(enB,1000)
p2_dt.start(25)
#Second motor
io.setup(in1,io.OUT)
io.setup(in2,io.OUT)
io.setup(enA,io.OUT)
io.output(in1,io.LOW)
io.output(in2,io.LOW)
p_dt= io.PWM(enA,1000)
p_dt.start(25)

while(1):
    command = input("Enter 'r' to make the rover drive: ")

    if command == 'r':
        #forwards
        io.output(in3, io.HIGH)
        io.output(in4, io.LOW)
        p2_dt.ChangeDutyCycle(100)
        io.output(in1, io.HIGH)
        io.output(in2, io.LOW)
        p_dt.ChangeDutyCycle(100)
        sleep(10)
        #stop
        io.output(in3, io.LOW)
        io.output(in4, io.LOW)
        io.output(in1, io.LOW)
        io.output(in2, io.LOW)
        sleep(3)
        #backwards
        io.output(in3, io.LOW)
        io.output(in4, io.HIGH)
        p2_dt.ChangeDutyCycle(100)
        io.output(in1, io.LOW)
        io.output(in2, io.HIGH)
        p2_dt.ChangeDutyCycle(100)
        sleep(10)
        #stop
        io.output(in3, io.LOW)
        io.output(in4, io.LOW)
        io.output(in1, io.LOW)
        io.output(in2, io.LOW)

    elif command == 's':
        io.cleanup()
        break

    else:
        print("You entered an invalid command. Try again")


