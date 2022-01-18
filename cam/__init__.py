from re import T
import threading
import time
import os
import cv2

#import other scripts
from . import hough

#files
image = "./cam/image.jpg"
location_image = "./assets/location_image.jpg"

#for stopping balls detections
def stop(values):
    values.robot.movementclear = False
    values.UI.sorting_done = True
    values.ball.x = 0
    values.ball.y = 0
    values.ball.color = None
    values.UI.ball.x = 0
    values.UI.ball.y = 0
    values.UI.ball.color = None

#main function of script
def Main(values, sql):
    while True:
        #print(values.robot.movementclear, values.robot.cameraarea)
        if values.robot.movementclear and not values.ball.color and not values.robot.cameraarea:
            #capture picture
            os.system(f"libcamera-jpeg -o {image} -n -t 1 --width 1014 --height 760 > /dev/null 2>&1")
            
            if not values.robot.cameraarea:
                #get circles through hought transformation
                circles, total = hough.transformation(image)
                
                #get coardinates of circle
                if circles is not None:#set ball values
                    values.ball.total = total + values.ball.done
                    c, r, g, y = hough.balls_to_collect(circles, image, values)
                    values.ball.to_collect = c + values.ball.done
                    values.colors.red.total = r + values.colors.red.sorted
                    values.colors.green.total = g + values.colors.green.sorted
                    values.colors.yellow.total = y + values.colors.yellow.sorted
                    
                    x, y, color = hough.cordinates(circles, image, values)
                    if color == None:
                        stop(values)
                    hough.save_location_image(circles, image, location_image)
                    values.ball.x = x
                    values.ball.y = y
                    values.ball.color = color
                    values.UI.ball.x = x
                    values.UI.ball.y = y
                    values.UI.ball.color = color
                    
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