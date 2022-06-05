import cv2
import torch
import pyautogui
from PIL import Image
import time
import keyboard
import numpy as np
from mss import mss
import win32api, win32con
import pynput
import pywinauto
import mouse
"""
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'yolov5-master\best.pt')
#image = Image.open("yolov5-master\img10.png")
image = pyautogui.screenshot()
results = model(image)
img = numpy.asarray(results.render())
#cv2.imwrite('color_img.jpg', img)
print(results.pandas().xyxy[0])
print(results.xyxy[0])
results.render()
for img in results.imgs:
    cv2.imshow("name", img)
    cv2.waitKey()
    print()

"""

 

#object_methods = [method_name for method_name in dir(results)
#                  if callable(getattr(results, method_name))]
#print(object_methods)
#results.show()



def main(model):
    mon = {'left': 800, 'top': 270, 'width': 240, 'height': 540}
    #cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    #cv2.resizeWindow("Live", 480, 270)
    with mss() as sct:
        while True:
    # press 'q' to exit
            screenShot = sct.grab(mon)
            img = Image.frombytes(
                'RGB', 
                (screenShot.width, screenShot.height), 
                screenShot.rgb, 
            )
            results = model(img)
            
            #print(results.xyxy[0])
            if(len(results.pandas().xyxy[0]['xmin'].values)):
                x_top = results.pandas().xyxy[0]['xmin'].values[0]
                y_top = results.pandas().xyxy[0]['ymin'].values[0]
                x_bot = results.pandas().xyxy[0]['xmax'].values[0]
                y_bot = results.pandas().xyxy[0]['ymax'].values[0]
                width = x_bot - x_top
                height = y_bot - y_top
                head_x = x_top + width/2
                head_y = y_top + height*0.1
                print(head_x)
               
                if(abs(160 - head_x) < 10 and abs(270-head_y) < 10):
                    print("USAO")
                    mouse.click()
                    time.sleep(0.15)
            #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(head_x), int(head_y), 0, 0)
            #print(str(head_x) + " " + str(head_y))
            #print(results.xyxyn[0][:, :-1].numpy())
                #results.render()
               # img = results.imgs[0]
                #img = cv2.circle(img, (int(head_x),int(head_y)), radius=5, color=(0, 0, 255), thickness=1)
            #img = cv2.circle(img, (int(x_bot),int(y_bot)), radius=5, color=(0, 0, 255), thickness=1)
            #cv2.imshow('test', np.array(img))
            if cv2.waitKey(33) & 0xFF in (
                ord('q'), 
                27, 
            ):
                break
            #frame = np.array(img)
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
        #cv2.imshow("Live", frame)
if __name__ == '__main__':
    CUDA = torch.cuda.is_available()
    print(CUDA)
    #print(torch.zeros(1).cuda())
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'yolov5-master\best.pt')
    if CUDA:
        model.cuda()
    
    main(model)
 