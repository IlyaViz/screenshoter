import pyautogui as pg
import os
import keyboard
import cv2
import numpy
import sys
import threading
import time

def get_screenshot(autosave=False):
    COUNT = 0

    def show_current_area_of_screenshot():
        time.sleep(1)
        while True:
            all_screen_np = numpy.array(img)
            all_screen_np = cv2.cvtColor(all_screen_np, cv2.COLOR_BGR2RGB)
            cv2.imshow('go?', all_screen_np)
            cv2.waitKey(1)
    threading.Thread(target=show_current_area_of_screenshot).start()
    
    first_point = (0,0)
    second_point = (1,1)
    while True:
        if keyboard.is_pressed('['):
            temp = pg.position()
            if temp[0] < second_point[0] and temp[1] < second_point[1]:
                first_point = temp

        if keyboard.is_pressed(']'):
            temp = pg.position()
            if temp[0] > first_point[0] and temp[1] > first_point[1]:
                second_point = temp
        
        img = pg.screenshot(region=[first_point[0], first_point[1],
                                second_point[0]-first_point[0],
                                second_point[1]-first_point[1]])
        
        if keyboard.is_pressed('/'):
            if autosave:
                filename = str(COUNT)
                COUNT += 1
            else:
                filename = input('Filename\n')

            print(f'Trying to save to {PATH}{filename}.png')
            try:
                img.save(PATH + filename + '.png')
            except:
                print('error while saving')
            time.sleep(1)

def main():
    global PATH
    PATH = input("Path to directory e.g\n")
    PATH = PATH if PATH[-1] in ['/', '\\'] else PATH + '/'
    autosave = input("autosave? <y>, <n>")
    autosave = True if autosave == 'y' else False
    get_screenshot(autosave)
 
if __name__ == '__main__':
    main()