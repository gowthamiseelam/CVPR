import cv2
import numpy as np
binary_image = np.array((
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 255, 255, 255, 0, 0, 0, 2551],
    [0, 255, 255, 255, 0, 255, 0, 0],
    [0, 255, 255, 255, 0, 255, 0, 0],
    [0, 0, 255, 255, 0, 0, 0, 0],
    [0, 0, 255, 0, 0, 255, 255, 0],
    [0,255, 0, 255, 0, 0, 255, 0],
    [0, 255, 255, 255, 0, 0, 0, 0]), dtype="uint8")
kernel_hit = np.array([[0, 1, 0],
                        [1, 1, 1],
                        [0, 1, 0]], np.uint8)  # Hit detection kernel

kernel_miss = np.array([[1, 0, 1],
                         [0, 1, 0],
                         [1, 0, 1]], np.uint8)  # Miss detection kernel

# Perform erosion for hit detection
hit = cv2.erode(binary_image, kernel_hit)

# Perform erosion for miss detection on the inverted binary image
miss = cv2.erode(cv2.bitwise_not(binary_image), kernel_miss)

# Compute the hit-or-miss transform
hit_miss_result = cv2.bitwise_and(hit, miss)
print(hit,miss,hit_miss_result)

binary_image=cv2.resize(binary_image,(250,250),interpolation=cv2.INTER_NEAREST)
hit=cv2.resize(hit,(250,250),interpolation=cv2.INTER_NEAREST)
miss=cv2.resize(miss,(250,250),interpolation=cv2.INTER_NEAREST)
hit_miss_result=cv2.resize(hit_miss_result,(250,250),interpolation=cv2.INTER_NEAREST)


# Display the images
cv2.imshow('Original Binary Image', binary_image)
cv2.imshow("Hit (Eroded with Kernel 1)", hit)
cv2.imshow("Miss (Eroded with Kernel 2 on Inverted Image)", miss)
cv2.imshow("Hit-or-Miss Result", hit_miss_result)

cv2.waitKey(0)
cv2.destroyAllWindows()