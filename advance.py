import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('pink.jpeg', cv2.IMREAD_GRAYSCALE)
image=cv2.resize(image,(300,300))
# Step 1: Apply Gaussian Blur (Smoothing)
# Marr-Hildreth uses a Gaussian filter to smooth the image
sigma = 1.0  # Standard deviation of the Gaussian
gaussian_blurred = cv2.GaussianBlur(image, (5, 5), sigma)

# Step 2: Compute the Laplacian (second derivative)
laplacian = cv2.Laplacian(gaussian_blurred, cv2.CV_64F)

# Step 3: Thresholding (optional but can help to better visualize edges)
thresholded = cv2.threshold(np.abs(laplacian), 15, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("Original image",image)
cv2.imshow("Marr Hildreth",thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()
