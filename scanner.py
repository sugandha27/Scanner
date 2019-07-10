import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('/root/Desktop/test.jpg')
print(img.shape)
plt.imshow(img)
plt.show()

#considering the image size , it is necessary to crop the image according to number of rows and columns
