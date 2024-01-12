import cv2 as cv
import numpy as np

pic = cv.imread('photos/Hills.jpg')
img = cv.resize(pic, (600,400))
cv.imshow('original', img)

blank = np.zeros((300,300), dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('weird shape', weird_shape)

#masked = cv.bitwise_and(img, img, mask=mask)
#cv.imshow('MaskedImage', masked)


cv.waitKey(0)