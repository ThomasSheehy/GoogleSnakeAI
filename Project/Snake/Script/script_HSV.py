import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os

def keys_to_output(keys):
    '''
    [D, S, A, W]
    '''
    output = [0, 0, 0, 0]
    
    if 'D' in keys:
        output [0] = 1

    elif 'S' in keys:
        output [1] = 1

    elif 'A' in keys:
        output [2] = 1

    else:
        output [3] = 1

    return output


file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print("File exists, loading previous data.")
    training_data = list(np.load(file_name))
else:
    print("File does not exist, starting fresh.")
    training_data = []


def main():
    
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    last_time = time.time()

    paused = False
    while(True):
        screen =  grab_screen(region=(0, 50, 600, 700))
        last_time = time.time()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
        screen = cv2.resize(screen,(80, 60))
        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen, output])
        print('Loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        if len(training_data) % 1000 == 0:
            print(len(training_data))
            np.save(file_name, training_data)

main()
