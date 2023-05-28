import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def emptyFunction():
    pass
def main():
    img = np.zeros((512,512,3) , np.uint8)
    windowName = "open color plette"
    cv.namedWindow(windowName)
    cv.createTrackbar('Blue',windowName , 0,255,emptyFunction)
    cv.createTrackbar('Green', windowName, 0, 255, emptyFunction)
    cv.createTrackbar('Red', windowName, 0, 255, emptyFunction)
    while(True):
        cv.imshow(windowName, img)
        if cv.waitKey(1) == 27:
            break
        blue = cv.getTrackbarPos("Blue", windowName)
        green = cv.getTrackbarPos("Green", windowName)
        red = cv.getTrackbarPos("Red", windowName)
        img[:] = [blue,green,red]
        print(blue, green , red)
    cv.destroyAllWindows()
if __name__=="__main__":
    main()



