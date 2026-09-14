# ============================================================
# OpenCV Image Processing Practicals
# ============================================================


# 1. Write a Python program to read and display an image using OpenCV.

import cv2

image = cv2.imread("/Users/gauravpaul/Desktop/Image/bear.jpeg")

cv2.imshow("Original Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ============================================================
# 2. Write a program to read an image from a specified path
#    using cv2.imread().
# ============================================================

image = cv2.imread("/Users/gauravpaul/Desktop/Image/bear.jpeg")

print("Image read successfully")


# ============================================================
# 3. Write a program to display an image using cv2_imshow().
#
# NOTE:
# cv2_imshow() is specifically for Google Colab.
# For VS Code, cv2.imshow() is used.
# ============================================================

image = cv2.imread("/Users/gauravpaul/Desktop/Image/bear.jpeg")

cv2.imshow("Display Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ============================================================
# 4. Write a program to save an image using cv2.imwrite().
# ============================================================

image = cv2.imread("/Users/gauravpaul/Desktop/Image/bear.jpeg")

cv2.imwrite("saved_image.jpg", image)

print("Image saved successfully")


# ============================================================
# 5. Write a Python program to convert a color image
#    into a grayscale image.
# ============================================================

image = cv2.imread("/Users/gauravpaul/Desktop/Image/bear.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ============================================================
# 6. Write a program to save a grayscale image
#    using cv2.imwrite().
# ============================================================

image = cv2.imread("/Users/gauravpaul/Desktop/Image/bear.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("grayscale.jpg", gray)

print("Grayscale image saved successfully")


# ============================================================
# 7. Write a Python program to convert an image
#    into a NumPy array.
# ============================================================

import numpy as np

image = cv2.imread("/Users/gauravpaul/Desktop/Image/bear.jpeg")

array = np.array(image)

print("Image converted into NumPy array")
print(array)


# ============================================================
# 8. Print the pixel values of an image using NumPy.
# ============================================================

image = cv2.imread("/Users/gauravpaul/Desktop/Image/bear.jpeg")

array = np.array(image)

print("Pixel value at (0, 0):")
print(array[0, 0])


# ============================================================
# 9. Write a Python program to rotate an image
#    by 90 degrees using imutils.
# ============================================================

import imutils

image = cv2.imread("/Users/gauravpaul/Desktop/Image/bear.jpeg")

rotated = imutils.rotate(image, 90)

cv2.imshow("Rotated 90 Degrees", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ============================================================
# 10. Write a Python program to rotate an image
#     by 180 degrees using imutils.
# ============================================================

image = cv2.imread("/Users/gauravpaul/Desktop/Image/bear.jpeg")

rotated = imutils.rotate(image, 180)

cv2.imshow("Rotated 180 Degrees", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ============================================================
# All 10 OpenCV practicals completed.
# ============================================================