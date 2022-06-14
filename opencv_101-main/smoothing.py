import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('cats', img)


# averaging
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# gaussian blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# median blur

medianb = cv.medianBlur(img, 7)
cv.imshow('Median Blur', medianb)

# bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)