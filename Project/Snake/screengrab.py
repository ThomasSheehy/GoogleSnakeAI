import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from numpy import ones,vstack
from numpy.linalg import lstsq
from statistics import mean


def roi(img, vertices):
    #, vertices
    mask = np.zeros_like(img)

    cv2.fillPoly(mask, vertices, 255)
    #vertices,
    masked = cv2.bitwise_and(img, mask)
    return masked

def draw_lines(img, lines, color = [0,255,255], thickness = 3):
    for line in lines:
        coords = line[0]
        cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [0, 255, 0], 3)

def process_img (original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img

def process_img (image):
    original_image = image
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    processed_img = cv2.Canny(image, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)
    vertices = np.array([[10,100], [580,100], [580,600], [10,600]])
    processed_img = roi(processed_img, [vertices])
    #, [vertices]

    #edges
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 100, 0, 15)
    m1 = 0
    m2 = 0
    
    try:
        l1, l2, m1, m2 = draw_lines(original_image, lines) 
        cv2.line(original_image, (l1[0], l1[1], l1[2], l1[3]), [0, 255, 0], 30)
        cv2.line(original_image, (l2[0], l2[1], l2[2], l2[3]), [0, 255, 0], 30)
    except Exception as e:
        ##print (str(e))
        pass
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255,0, 0], 3)

            except Exception as e:
                print(str(e))
    except Exception as e:
        pass
    

    return processed_img, original_image, m1, m2


last_time = time.time()
while(True):
    screen =  np.array(ImageGrab.grab(bbox=(0, 50, 600, 700)))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
    #screen = cv2.resize(screen(80, 60))
    print('Loop took {} seconds'.format(time.time() - last_time))
    last_time = time.time()
    new_screen, original_image, m1, m2 = process_img(screen)
    cv2.imshow('window', new_screen)
    cv2.imshow('window2', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))

    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


