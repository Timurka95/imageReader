import cv2
import pytesseract

image = cv2.imread('test2.jpg')
height, width, _ = image.shape
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('test', thresh)

cv2.waitKey()