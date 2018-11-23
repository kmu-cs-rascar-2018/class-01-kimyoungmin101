#########################################################################
# Date: 2018/10/02
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
        count = 0
        Tracker = Tracking_Sensor.SEN040134_Tracking([16, 18, 22, 40, 32])
        accelerator = rear_wheels.Rear_Wheels(db='config')
        distance_detector = Supersonic_Sensor.Supersonic_Sensor(35)
        distance = distance_detector.get_distance()        
        accelerator.ready()
        steering = front_wheels.Front_Wheels(db='config')
        steering.ready()
        accelerator.forward_with_speed(30)
        while(True):
            print(count)
            distance = distance_detector.get_distance()
            time.sleep(0.01)
            if((distance < 15) and (distance > 5) and (distance != 6) and (distance != 7)):
                print("distance", distance)
                accelerator.stop()
                time.sleep(0.1)
                steering.turn(90)
                time.sleep(0.1)
                accelerator.backward_with_speed(30)
                time.sleep(2)
                steering.turn_left(35)
                time.sleep(0.1)
                accelerator.forward_with_speed(30)
                time.sleep(1.5)
                steering.turn(90)
                time.sleep(1)                
                steering.turn_right(135)
                time.sleep(3)
                steering.turn_right(135)
                while(True):
                    if(Tracker.is_in_line() == True):
                        steering.turn(90)
                        time.sleep(0.1)
                        accelerator.stop()
                        time.sleep(0.1)
                        accelerator.forward_with_speed(30)
                        time.sleep(1)
                        break;
            if(Tracker.read_digital() == [1,0,0,0,0]):
                steering.turn_left(35)
                time.sleep(0.1)
                accelerator.forward_with_speed(30)
                time.sleep(0.5)
            elif((Tracker.read_digital() == [1,1,0,0,0])):
                steering.turn_left(60)
                time.sleep(0.1)
            elif((Tracker.read_digital() == [0,1,0,0,0])):
                steering.turn_left(50)
                time.sleep(0.1)                
            elif((Tracker.read_digital() == [1,1,1,0,0])):
                steering.turn_left(75)
                time.sleep(0.1)                
            elif((Tracker.read_digital() == [0,1,1,0,0])):
                steering.turn_left(80)
                time.sleep(0.1)
            elif((Tracker.read_digital() == [1,1,1,1,0])):
                steering.turn_left(70)
                time.sleep(0.1)
            elif((Tracker.read_digital() == [1,0,0,1,0])):
                steering.turn_left(80)
                time.sleep(0.1)
            elif((Tracker.read_digital() == [0,0,1,0,0]) or (Tracker.read_digital() == [0,1,0,1,0]) or (Tracker.read_digital() == [0,1,1,1,0])):
                steering.turn(90)
                time.sleep(0.1)
            elif((Tracker.read_digital() == [0,0,0,0,1])):
                steering.turn_right(135)
                time.sleep(0.1)
            elif((Tracker.read_digital() == [0,0,0,1,1])):
                steering.turn_right(120)
                time.sleep(0.1)
            elif((Tracker.read_digital() == [0,0,1,1,1])):
                steering.turn_right(110)
                time.sleep(0.1)
            elif((Tracker.read_digital() == [0,1,1,1,1])):
                steering.turn_right(110)
                time.sleep(0.1)                
            elif((Tracker.read_digital() == [0,0,1,1,0])):
                steering.turn_right(115)
                time.sleep(0.1)
            elif((Tracker.read_digital() == [0,0,0,1,0])):
                steering.turn_right(125)
                time.sleep(0.1)
            elif((Tracker.read_digital() == [0,1,0,0,1])):
                steering.turn_right(100)
                time.sleep(0.1)    
            elif((Tracker.read_digital() == [0,0,0,0,0])):
                accelerator.stop()
                time.sleep(0.1)
                steering.turn(90)
                while(True):
                    print("Tracker.is_in_line : ", Tracker.is_in_line())
                    time.sleep(0.1)
                    accelerator.backward_with_speed(30)
                    if(Tracker.is_in_line() == True):
                        accelerator.stop()
                        time.sleep(0.1)
                        accelerator.forward_with_speed(20)
                        break;
            elif((Tracker.read_digital() == [1,1,1,1,1])):
                count = count+1
                if(count >= 3):
                    break;
                accelerator.forward_with_speed(30)
                time.sleep(1)
            else:
                steering.turn(90)
                time.sleep(0.1)
        accelerator.stop()
        accelerator.power_down()        


                
        
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