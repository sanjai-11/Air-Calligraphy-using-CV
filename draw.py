import cv2 as cv
import numpy as np

#blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank', blank)

pic = cv.imread('photos/sanicon.jpg')
s1 = pic.shape
w,h,d = s1
img = cv.resize(pic,(round(w/2),round(h/2)), interpolation=cv.INTER_CUBIC)
cv.imshow('sanicon',img)

#blank[200:300, 300:400] = 0,0,255
##cv.imshow('Green', blank)

##---rectangle---
#cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
#cv.imshow('Rectangle', blank)

##---circle---
#cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-3)
#cv.imshow('circle', blank)

##---Line---
#cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
#cv.imshow('Line', blank)

#---write---
#cv.putText(blank, 'Hello, my name is sanjai...', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
#cv.imshow('Text', blank)

#---convert-gray---
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#---blur---
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
#cv.imshow('blur',blur)

#---edge_cascading---
#canny = cv.Canny(blur, 125, 175)
#cv.imshow('canny edges',canny)

#---dilating_image---
#dilated = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow('Dilated',dilated)

#---eroding---
#eroded = cv.erode(dilated, (3,3), iterations=3)
#cv.imshow('Erode', eroded)

#---resize---
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resized)

#---crapping---
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)