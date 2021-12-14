import sys
import cv2 as cv
import numpy as np
def main(argv):
    
    default_file = 'neu.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    
    gray = cv.medianBlur(gray, 5)
    
    
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)
    
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            color = (src[i[1], i[0]+10])
            # circle center
            #cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 3)

            color_string = None
            if color[0] < 15:
                color_string = "yellow"
            elif color[1] < 100:
                color_string = "red"
            else:
                color_string = "green"

            print(f"pos: {i}")
            print(f"color: {color_string}")  
            print(f"color: {color}")
            
            
            cal1_px = (229, 130)
            cal2_px = (962, 622)
            x_px_total = cal2_px[0] - cal1_px[0]
            y_px_total = cal2_px[1] - cal1_px[1]
            x_mm_total = 305
            y_mm_total = 207
            
            pos_px_x = x_px_total - (i[0] - cal1_px[0])
            pos_px_y = y_px_total - (i[1] - cal1_px[1])
            
            pos_perc_x = pos_px_x / x_px_total
            pos_perc_y = pos_px_y / y_px_total
            
            pos_mm_x = x_mm_total * pos_perc_x
            pos_mm_y = y_mm_total * pos_perc_y
            
            print(f"position: {pos_mm_x} {pos_mm_y}")

            cv.imshow("detected circles", src)
            cv.waitKey(0)
    
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])