te: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################
from SEN040134 import SEN040134_Tracking as Tracking_Sensor
#########################################################################
# Date: 2018/10/02
# file name: car.py
# Purpose: this code has been generated for the 4 wheels drive body
# this code is used for the student only
#########################################################################


# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO

# =======================================================================
# import ALL method in the SEN040134 Tracking Module
# =======================================================================
from SEN040134 import SEN040134_Tracking as Tracking_Sensor

# =======================================================================
# import ALL method in the TCS34725 RGB Module
# =======================================================================
from TCS34725 import TCS34725_RGB as RGB_Sensor

# =======================================================================
# import ALL method in the SR02 Ultrasonic Module
# =======================================================================
from SR02 import SR02_Supersonic as Supersonic_Sensor

# =======================================================================
# import ALL method in the PCA9685 Module
# =======================================================================
from PCA9685 import PCA9685 as PWM_Controller

# =======================================================================
# import ALL method in the rear/front Motor Module
# =======================================================================
import rear_wheels
import front_wheels

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        Tracker = Tracking_Sensor.SEN040134_Tracking([16, 18, 22, 40, 32])
        accelerator = rear_wheels.Rear_Wheels(db='config')
        accelerator.ready()
        steering = front_wheels.Front_Wheels(db='config')
        steering.ready()
        accelerator.forward_with_speed(20)
        while(True):
            print(" read digital : ", Tracker.read_digital())
            time.sleep(0.2)
            if((Tracker.read_digital() == [1,1,1,0,0])):
                steering.turn_left(75)
                time.sleep(0.2)                                
            elif(Tracker.read_digital() == [1,0,0,0,0]):
                steering.turn_left(55)
                time.sleep(0.2)                
            elif((Tracker.read_digital() == [1,1,0,0,0])):
                steering.turn_left(60)
                time.sleep(0.2)                                
            elif((Tracker.read_digital() == [0,1,0,0,0])):
                steering.turn_left(80)
                time.sleep(0.2)                
            elif((Tracker.read_digital() == [0,1,1,0,0])):
                steering.turn_left(85)                
                time.sleep(0.2)
            elif((Tracker.read_digital() == [0,0,1,0,0]) or (Tracker.read_digital() == [0,1,0,1,0]) or (Tracker.read_digital() == [0,1,1,1,0])):
                steering.turn(90)
                time.sleep(0.2)
            elif((Tracker.read_digital() == [0,0,1,1,0])):
                steering.turn_right(95)
                time.sleep(0.2)
            elif((Tracker.read_digital() == [0,0,0,1,0])):
                steering.turn_right(100)
                time.sleep(0.2)
            elif((Tracker.read_digital() == [0,0,0,1,1])):
                steering.turn_right(120)
                time.sleep(0.2)                
            elif((Tracker.read_digital() == [0,0,0,0,1])):
                steering.turn_right(125)
                time.sleep(0.2)
            elif((Tracker.read_digital() == [0,0,1,1,1])):
                steering.turn_right(110)
                time.sleep(0.2)
            elif((Tracker.read_digital() == [0,0,0,0,0])):
                while(True):
                    print(Tracker.is_in_line)
                    time.sleep(0.2)
                    accelerator.backward_with_speed(20) # 라인벗어났을시 뒤로간다.
                    if(Tracker.is_in_line == True):
                        break;
                accelerator.stop()
                time.sleep(0.2)
                accelerator.forward_with_speed(20) # 다시 앞으로 가면서실
            else:
                steering.turn(90)
                time.sleep(0.2)
                


                
        
        # implement the assignment code here
        pass


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
