import threading
import time
import os
import cv2

#import other scripts
from . import hough

#files
image = "./cam/image.jpg"
location_image = "./cam/location_image.jpg"

#for stopping balls detections
def stop(values):
    values.movementclear = False
    values.ball.x = 0
    values.ball.y = 0
    values.ball.color = None

#main function of script
def Main(values, sql):
    while True:
        #print(values.robot.movementclear, values.robot.cameraarea)
        if values.robot.movementclear and not values.ball.color and not values.robot.cameraarea:
            #capture picture
            os.system(f"libcamera-jpeg -o {image} -n -t 1 --width 1014 --height 760 > /dev/null 2>&1")
            
            if not values.robot.cameraarea:
                #get circles through hought transformation
                circles = hough.transformation(image)
                
                if circles is not None:
                        x, y, color = hough.cordinates(circles, image)
                        if color == None:
                            stop(values)
                        hough.save_location_image(circles, image, location_image)
                        print(x, y , color)
                        values.ball.x = x
                        values.ball.y = y
                        values.ball.color = color
                    
                else:
                    stop(values)
    
#main thread of script
class Thread(threading.Thread):
    def __init__(self, values, sql):
        threading.Thread.__init__(self)
        self.values = values
        self.sql = sql
    def run(self):
        Main(self.values, self.sql)