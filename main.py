import cv2
import numpy as np

# Upload image
image = cv2.imread('image1.jpg')

# Check if the image has been uploaded correctly
if image is None:
    print("Error loading image")
    exit()

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create the negative image
negative_image = cv2.bitwise_not(image)

# Convert the grayscale image to BGR to concatenate it with the others
gray_image_bgr = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

# Concatenate the three images horizontally
combined_image = np.hstack((image, gray_image_bgr, negative_image))

# Save the combined image
# cv2.imwrite('modified_image.jpg', combined_image)

# Display the combined image
cv2.imshow('Modified image', gray_image_bgr)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
