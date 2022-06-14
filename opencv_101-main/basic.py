import cv2 as cv

img = cv.imread('photos/lady.jpg')

cv.imshow('Lady', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# edge cascade
canny = cv.Canny(img, 125, 175)
                #buraya blur yazılabilir
cv.imshow('Canny', canny)

# dilating image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

# eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# resize
resized = cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
