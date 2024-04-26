import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# creating windows or canvas
canvas =  np.zeros((300,300,3),dtype="uint8")

# tuble of green color
green =  (0,255,0)
# drawing line
cv.line(canvas,(0,0),(300,300),color=green)

# Red line
red = (255,0,0)
# drawing red line
cv.line(canvas,(300,0),(0,300),color=red)

#showing canvas
plt.imshow(canvas)
plt.show()

