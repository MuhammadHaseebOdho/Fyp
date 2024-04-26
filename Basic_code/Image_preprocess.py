import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the drone image
drone_image = cv2.imread('E:\FYP\code\images\img1.jpg')

# Preprocessing: Convert to grayscale and enhance contrast if needed
gray_image = cv2.cvtColor(drone_image, cv2.COLOR_BGR2GRAY)

# Segmentation: Apply thresholding to isolate the solar plate
_, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

# Find contours of the solar plate
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through contours and find the contour with maximum area (assuming it's the solar plate)
max_contour = max(contours, key=cv2.contourArea)

# Create a mask for the solar plate
mask = np.zeros_like(gray_image)
cv2.drawContours(mask, [max_contour], -1, (255), thickness=cv2.FILLED)

# Apply the mask to extract the solar plate region
solar_plate_image = cv2.bitwise_and(gray_image, mask)

# Feature Extraction: Get thermal values from the solar plate region
thermal_values = solar_plate_image[mask > 0]

# Now you have the thermal values of the solar plate in the 'thermal_values' array

# Optional: Display the result
# cv2.imshow('Solar Plate', solar_plate_image)
print(thermal_values)
thermal_list_of_panels = np.array(thermal_values)
plt.imshow(solar_plate_image)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
