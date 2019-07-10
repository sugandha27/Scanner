import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('/root/Desktop/test.jpg')
crop_img=img[800:4000,500:3000,2]
crop_img=cv2.resize(crop_img,(100,100))
plt.imshow(crop_img)
plt.axis("off")
plt.show()



