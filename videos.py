#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# David Pascual Hernandez, 2015

import cv2
import sys

try:
    vidFile = cv2.VideoCapture(0)
except:
    print "problem opening input stream"
    sys.exit(1)
if not vidFile.isOpened():
    print "capture stream not open"
    sys.exit(1)

nFrames = int(vidFile.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)) # one good way of namespacing legacy openCV: cv2.cv.*
print "frame number: %s" %nFrames
fps = vidFile.get(cv2.cv.CV_CAP_PROP_FPS)
print "FPS value: %s" %fps

ret, frame = vidFile.read() # read first frame, and the return code of the function.
while ret:  # note that we don't have to use frame number here, we could read from a live written file.
    print "yes"
    cv2.imshow("frameWindow", frame)
    cv2.waitKey(int(1/20*1000)) # time to wait between frames, in mSec
    ret, frame = vidFile.read() # read next frame, get next return code