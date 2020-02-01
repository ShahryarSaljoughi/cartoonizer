import cv2
import numpy as np


num_down = 2 # number of downsampling steps
num_bilateral = 7 # number of bilateral filtering steps

img_rgb = cv2.imread("cat.jpg")
cv2.imshow("first pic", img_rgb)
img_color = img_rgb
# for _ in range(num_down):
#     img_color = cv2.pyrDown(img_color)

# cv2.imshow("after pyramid down", img_color)

for _ in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)

# cv2.imshow("after bilateral", img_color)

# for _ in range(num_down):
#     img_color = cv2.pyrUp(img_color)

# cv2.imshow("after pyramid up", img_color)

cv2.waitKey(0)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)


img_edge = cv2.adaptiveThreshold(
    img_blur, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    blockSize=9,
    C=2
)

img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
img_cartoon = cv2.bitwise_and(img_color, img_edge)
cv2.imshow("edge ", img_cartoon)
cv2.imwrite("cartoon_cat.jpg", img_cartoon)
cv2.waitKey(0)
