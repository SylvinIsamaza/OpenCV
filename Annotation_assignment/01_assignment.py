import cv2

# Read the image
image = cv2.imread('assignment-001-given.jpg')

# Create a copy of the image for the overlay
overlay = image.copy()


cv2.rectangle(overlay, (898, 100), (1118, 175), (0, 0, 0), -1)  # Filled rectangle


alpha = 0.6  # Transparency factor (adjust as needed)
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
cv2.rectangle(image,(260,180),(990,932),(0,255,0),5)

# Add text on top of the semi-transparent rectangle
cv2.putText(image, "RAH972U", (900, 160), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

# Display and save the result
cv2.imshow('Result', image)
cv2.imwrite('assignment-001-result.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
