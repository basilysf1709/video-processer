import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture("assets/clip2.mp4")

# Check if camera opened successfully
if (cap.isOpened() == False): 
    print("Unable to read video feed")

# Defining the Codec
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output/final.mp4', fourcc, 20.0, (int(cap.get(3)),int(cap.get(4))) )
while True:
    ret, frame = cap.read()
    out.write(frame)
    if ret == True: 
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()