import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

train_data = np.load('training_data.npy')
print(len(train_data))

df = pd.DataFrame(train_data)
##print(df.head())
print(Counter(df[1].apply(str)))

rights = []
downs = []
lefts = []
ups = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1, 0, 0, 0]:
        rights.append([img, choice])

    elif choice == [0, 1, 0, 0]:
        downs.append([img, choice])

    elif choice == [0, 0, 1, 0]:
        lefts.append([img, choice])

    elif choice == [0, 0, 0, 1]:
        ups.append([img, choice])

    else:
        print("No matches")

rights = rights[:len(downs)][:len(lefts)][:len(ups)]
downs = downs[:len(rights)][:len(lefts)][:len(ups)]
lefts = lefts[:len(rights)][:len(downs)][:len(ups)]
ups = ups[:len(rights)][:len(downs)][:len(lefts)]

final_data = rights + downs + lefts + rights

shuffle(final_data)
print(len(final_data))
np.save('training_data_v2.npy', final_data)


for data in train_data:
    img = data[0]
    choice = data[1]
    print(img.shape)
    cv2.imshow('test', img)
    print(choice)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

