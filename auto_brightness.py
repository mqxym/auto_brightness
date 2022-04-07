from time import sleep
import cv2
import screen_brightness_control as sbc

threshhold = 40

def change_brightness (level):
    current_brighntess = sbc.get_brightness()[0]
    if current_brighntess == level:
        return
    if (level > current_brighntess):
        for i in range(current_brighntess,level+1):
            sbc.set_brightness(i)
    else:
        for i in range(current_brighntess,level,-1):
           sbc.set_brightness(i)


vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    rval, frame = vc.read()
    average_cam_bright = frame.mean()
    if average_cam_bright < threshhold:
        sbc.set_brightness(20)
    else:
        sbc.set_brightness(100)

vc.release()