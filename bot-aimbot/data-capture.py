from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import cv2 as cv2


def main():
    f = open("brojac.txt", "r")
    i = int(f.readline())
    f.close()
    while True:
    # press 'q' to exit
        if keyboard.is_pressed("q"):
            f = open("brojac.txt", "w")
            f.write(str(i))
            f.close()
            print("q pressed, ending loop")
            break        
        elif keyboard.is_pressed("f"):
            input_img = pyautogui.screenshot()
            input_img.save("valorant/" + str(i) + ".png")
            print("uslikao")
            i += 1
def inf_loop():
    while True:
        time.sleep(0.1)
        input_img = pyautogui.screenshot()       
if __name__ == '__main__':
    main()