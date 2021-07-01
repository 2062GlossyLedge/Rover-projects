# This prorgam makes a servo and ultrasonic sensor work together simultaneously to check for obstacles.
# This program leaves a blueprint for what the motors should do.
from gpiozero import AngularServo
from gpiozero import DistanceSensor
from time import sleep

s = AngularServo(18, min_angle=-90, max_angle=90)
#Ultrasonic sensor reads distance for the whole program
sensor = DistanceSensor(echo=27, trigger=17)

s.mid()
obstacle = 10
object_distance = sensor.distance * 100
print(object_distance)

#move forward from rest 

def when_object_in_front():
    while True:
        if object_distance <= obstacle:
            s.max()
            sleep(4)
            #reverse, turn left, move forward
            continue
            #a1 will only look for obstacles by turning left 
            #if object_distance <= obstacle:
                #s.min()
                #sleep(4)
                #reverse 
                #continue
        elif object_distance > obstacle:
            #Drive forward 
            continue
            
            
    

when_object_in_front()
