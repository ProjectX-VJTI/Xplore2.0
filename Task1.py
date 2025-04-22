import cv2
import numpy as np
image = cv2.imread("Task1.png")
if np.mean(image) == 255:
    print("Image is white")
else:
    print("Image is not white")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
_, binary = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", binary)
white_pixels = cv2.countNonZero(binary)
total_pixels = image.shape[0] * image.shape[1]
non_white_pixels = total_pixels - white_pixels
print(f"Total number of pixels: {total_pixels}")
print(f"Number of white pixels: {white_pixels}")
print(f"Number of non-white pixels: {non_white_pixels}")
non_white_pixel_locations = np.argwhere(binary == 0)
print("Non-white pixel locations (row, column):")
for row, col in non_white_pixel_locations:
    print(f"({row}, {col})")
cv2.waitKey(0)
cv2.destroyAllWindows()
