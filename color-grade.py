import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture("assets/clip2.mp4")

# Check if camera opened successfully
if (cap.isOpened() == False): 
    print("Unable to read video feed")

# Defining the Codec
# This is the important part, Codec is basically a compression technology to compress and decode video files
fourcc = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')
out = cv2.VideoWriter('output/final2.mp4', fourcc, 20.0, (int(cap.get(3)),int(cap.get(4))) )
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