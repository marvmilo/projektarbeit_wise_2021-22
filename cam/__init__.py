import threading
import time
import os

#import other scripts
from . import hough

#files
image = "./cam/image.jpg"
location_image = "./cam/location_image.jpg"

#main function of script
def Main(values, sql):
    while True:
        #capture picture
        os.system(f"libcamera-jpeg -o {image} -t 1 --width 1014 --height 760 > /dev/null 2>&1")
        
        #get circles through hought transformation
        circles = hough.transformation(image)
        
        if circles is not None:
            x, y, color = hough.cordinates(circles, image)
            hough.save_location_image(circles, image, location_image)
            
            values.ball.x = x
            values.ball.y = y
            values.ball.color = color
        else:
            values.movmentclear = False
            values.ball.x = 0
            values.ball.y = 0
            values.ball.color = None
        
        time.sleep(1)
    
#main thread of script
class Thread(threading.Thread):
    def __init__(self, values, sql):
        threading.Thread.__init__(self)
        self.values = values
        self.sql = sql
    def run(self):
        Main(self.values, self.sql)