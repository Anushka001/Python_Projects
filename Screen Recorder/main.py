import cv2
from PIL import ImageGrab
import numpy as np
from numpy.core.arrayprint import array2string
from win32api import GetSystemMetrics
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

file_name = f"Recording/Video_{str(time.strftime('%d-%m-%y %H-%M-%S'))}.mp4"
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
capture_vid = cv2.VideoWriter(file_name, fourcc,20.0,(width, height))

while True:
    img_frame = ImageGrab.grab(bbox=(0,0,width,height))
    arr_img = np.array(img_frame)
    color_img = cv2.cvtColor(arr_img, cv2.COLOR_BGR2RGB)

    capture_vid.write(color_img)
    cv2.imshow('Screen Recorder', color_img)
    if cv2.waitKey(1) == ord('e'):
        break
