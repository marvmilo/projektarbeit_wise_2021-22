from re import A
import cv2
import numpy as np
import marvmiloTools as mmt
import os

#hough transformation for finding circlles
def transformation(filename):
    # Loads an image
    src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        return -1
    
    src = src[147:624, 190:881]
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 16,
                               param1=50, param2=12,
                               minRadius=28, maxRadius=30)
    #print(circles)
    try:
        total = len(circles[0])
    except TypeError:
        total = 0
    
    return circles, total

#getting amount of balls to collect
def balls_to_collect(circles, filename, values):
    amount_dict = {"red": 0, "green": 0, "yellow": 0}
    
    for circle in circles[0]:
        src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)
        # Check if image is loaded fine
        if src is None:
            print ('Error opening image!')
            return -1
        
        src = src[147:624, 190:881]
        
        x, y, r = circle.astype(np.int32)
        roi = src[y - r: y + r, x - r: x + r]
        
        # generate mask
        width, height = roi.shape[:2]
        mask = np.zeros((width, height, 3), roi.dtype)
        mask = cv2.circle(mask, (int(width / 2), int(height / 2)), r, (255, 255, 255), -1)
        dst = cv2.bitwise_and(roi, mask)
        
        # filter black color and fetch color values
        data = []
        for i in range(3):
            channel = dst[:, :, i]
            indices = np.where(channel != 0)[0]
            color = np.mean(channel[indices])
            data.append(int(color))

        # opencv images are in bgr format
        b,g,r = data
        
        if r > 100 and g > 100:
            color_string = "yellow"
        elif g > 100:
            color_string = "green"
        elif r > 100:
            color_string = "red"
        else:
            color_string = None
        
        if color_string and values.colors[color_string].container_num:
            amount_dict[color_string] += 1
            
    return sum(amount_dict.values()), amount_dict["red"], amount_dict["green"], amount_dict["yellow"]
        

#get cordinates from circles
def cordinates(circles, filename, values):
    for c, circle in enumerate(circles[0]):
        src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)
        # Check if image is loaded fine
        if src is None:
            print ('Error opening image!')
            return -1
        
        src = src[147:624, 190:881]
        # color = (src[int(circle[1]), int(circle[0]+10)])

        # color_string = None
        # print(color)
        # if color[0] < 30:
        #     color_string = "yellow"
        # elif color[1] < 130:
        #     color_string = "red"
        # else:
        #     color_string = "green"
        # print(color_string)
        
        x, y, r = circle.astype(np.int32)
        roi = src[y - r: y + r, x - r: x + r]
        
        # generate mask
        width, height = roi.shape[:2]
        mask = np.zeros((width, height, 3), roi.dtype)
        mask = cv2.circle(mask, (int(width / 2), int(height / 2)), r, (255, 255, 255), -1)
        dst = cv2.bitwise_and(roi, mask)
        
        # filter black color and fetch color values
        data = []
        for i in range(3):
            channel = dst[:, :, i]
            indices = np.where(channel != 0)[0]
            color = np.mean(channel[indices])
            data.append(int(color))

        # opencv images are in bgr format
        b,g,r = data
        
        if r > 100 and g > 100:
            color_string = "yellow"
        elif g > 100:
            color_string = "green"
        elif r > 100:
            color_string = "red"
        else:
            color_string = None
        
        #print(src.shape)
        x_mm_total = 202
        y_mm_total = 289
        x_px_total = src.shape[0] #477
        y_px_total = src.shape[1] #691
        pos_px_x = x_px_total - circle[1]
        pos_px_y = y_px_total - circle[0]
    
        #print(circle)
        pos_mm_x = x_mm_total * (pos_px_x / x_px_total)
        pos_mm_y = y_mm_total * (pos_px_y / y_px_total)
        
        if color_string and values.colors[color_string].container_num:
            return int(pos_mm_x), int(pos_mm_y), color_string, c
    return None, None, None, 0

#save image with marker at selected ball
def save_location_image(circles, filename, ball_to_select_index):
    img = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)
    # Check if image is loaded fine
    if img is None:
        print ('Error opening image!')
        return -1
    
    img = img[147:624, 190:881]
    
    for i, circle in enumerate(circles[0]):
        if i == ball_to_select_index:
            #print(circle)
            color = (255, 120, 75)
        else:
            color = (178, 178, 178)
        center = (int(circle[0]), int(circle[1]))
        radius = int(circle[2])
        img = cv2.circle(img, center, radius, color, 3)
    
    #create random image name to prevent caching   
    image_path = f"./assets/locationimage_{mmt.random_ID(32)}.png"
    for image in [p for p in os.listdir("./assets") if p.startswith("locationimage")]:
        os.remove(f"./assets/{image}")
    cv2.imwrite(image_path, img)