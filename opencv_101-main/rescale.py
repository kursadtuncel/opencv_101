import cv2 as cv

#img = cv.imread('photos/cat_large2.jpg')
#cv.imshow('Cat',img)
from read import capture


def rescaleFrame(frame, scale=0.75):
    #0.75 default value
    #images, videos and live video (rescaleFrame method)
    width = int(frame.shape[1] + scale)
    height = int(frame.shape[0] + scale)

    dimensions = (width,height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)



#reading videos

    capture = cv.VideoCapture('videos/dog.mp4')
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    #interpolation = ara değer bulma, inter area = ara alan

while True:
    isTrue, frame = capture.read()
    #frame-by-frame capture video
    frame_resized = rescaleFrame(frame, scale=.2)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cv.waitKey(0)