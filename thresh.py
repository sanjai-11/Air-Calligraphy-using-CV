import cv2 as cv
import numpy as np

pic = cv.imread('photos/sanicon.jpg')
img = cv.resize(pic, (500,500))
cv.imshow('original',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#---simple-thresholding---
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

#---Adaptive-Threshold---
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 13 , 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)