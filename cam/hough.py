import cv2

#hough transformation for finding circlles
def transformation(filename):
    # Loads an image
    src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        return -1
    
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)
    return circles

#get cordinates from circles
def cordinates(circles, filename):
    circle = circles[0][0]
    src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        return -1
    
    center = (circle[0], circle[1])
    color = (src[int(circle[1]), int(circle[0]+10)])

    color_string = None
    if color[0] < 15:
        color_string = "yellow"
    elif color[1] < 100:
        color_string = "red"
    else:
        color_string = "green"
    
    cal1_px = (229, 130)
    cal2_px = (962, 622)
    x_px_total = cal2_px[1] - cal1_px[1]
    y_px_total = cal2_px[0] - cal1_px[0]
    x_mm_total = 207
    y_mm_total = 305
    
    pos_px_x = x_px_total - (circle[1] - cal1_px[1])
    pos_px_y = y_px_total - (circle[0] - cal1_px[0])
    
    pos_perc_x = pos_px_x / x_px_total
    pos_perc_y = pos_px_y / y_px_total
    
    pos_mm_x = x_mm_total * pos_perc_x
    pos_mm_y = y_mm_total * pos_perc_y
    
    return int(pos_mm_x), int(pos_mm_y), color_string

#save image with marker at selected ball
def save_location_image(circles, filename, location_filename):
    circle = circles[0][0]
    src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        return -1
    
    center = (int(circle[0]), int(circle[1]))
    radius = int(circle[2])
    img = cv2.circle(src, center, radius, (255, 0, 255), 3)
    cv2.imwrite(location_filename, img)