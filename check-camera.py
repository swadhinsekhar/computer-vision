import cv2

# Try /dev/video3 first
#cap = cv2.VideoCapture('/dev/video3')
# If it doesn't work, you can switch to /dev/video2
cap = cv2.VideoCapture('/dev/video2', cv2.CAP_V4L2)

if not cap.isOpened():
    print("Error: Could not open video device.")
