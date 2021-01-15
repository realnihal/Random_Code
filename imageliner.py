# this program converts an image to a pencil sketch

import cv2

img_location = 'image_location'
filename = 'image_name'

img = cv2.imread(img_location+filename)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_gray_img = 255 - gray_img

blurred_img = cv2.GaussianBlur(inverted_gray_img, (21, 21), 0)

inverted_blurred = 255 - blurred_img

pencil_sketch_img = cv2.divide(gray_img, inverted_blurred, scale=256.0)

cv2.imshow('Original Image', img)
cv2.imshow('Inverting Image', pencil_sketch_img)
cv2.waitKey(0)
