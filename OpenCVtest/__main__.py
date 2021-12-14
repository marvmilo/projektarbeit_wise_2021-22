import cv2
import imutils

#show im function
def show(img, name = "image"):
    cv2.imshow("image", img)
    cv2.waitKey(0)

#open image
img = cv2.imread("./pictures/demo.jpg", cv2.IMREAD_COLOR)

#resize image
scale_percent = 100
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
show(resized)
print(f"new image size: {resized.shape}")

#crop/blur image
img = resized[100:390, 175:590]
show(img)
gaussian_blurr = cv2.GaussianBlur(img, (5, 5), 0)
show(gaussian_blurr)

#filters
color_filters = {
    "green": {
        "lower": (50, 86, 6),
        "upper": (85, 255, 255)
    },
    "yellow": {
        "lower": (13, 99, 81),
        "upper": (38, 255, 255)
    },
    "red": {
        "lower": (150,86, 6),
        "upper": (250,255,255)
    }
}

#iter over colors
for color in color_filters:
    print("applied new color filter: " + str(color_filters[color]))
    
    while True:            
        #hsv farbraum
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        print("converted picture to hsv")
        show(hsv, "picute hsv colors")
        
        #green mask
        lower = color_filters[color]["lower"]
        upper = color_filters[color]["upper"]
        mask = cv2.inRange(hsv, lower, upper)
        print(f"used {color} mask")
        show(mask, f"{color} mask")

        #cirlce
        try:
            cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            pointer = cv2.circle(img.copy(), center, 5, (208, 224, 64), -1)
        except ValueError:
            print("error detecting balls, skip to next color ...")
            break
        
        #print(radius)
        if radius < 15:
            print("no ball detectet, switching color ...")
            break
        
        print("detected ball at " + str(center))
        show(pointer, f"{color} pointer")
        
        #delete ball from picture and save
        img = cv2.circle(img, center, 25, (0, 0, 0), -1)
        cv2.imwrite("./image.jpg", img)
        
        #reopen it
        img = cv2.imread("./image.jpg", cv2.IMREAD_COLOR)