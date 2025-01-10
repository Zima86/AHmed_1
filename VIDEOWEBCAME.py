import cv2
from matplotlib import pyplot as plt
import time



def takephoto():
    ret, fram = cap.read()  # get a fram from a caputre device
    print(fram)
    plt.imshow(fram)
    plt.show()

def devicerelease(cap):
    cap.release()

while True:
    cap = cv2.VideoCapture(0)
    ret, fram = cap.read()  # get a fram from a caputre device
    print(fram)
    plt.imshow(fram)
    plt.show()
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

