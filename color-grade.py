import cv2
import numpy as np
import math

# Function to find the frames per second of a video file
def find_frames_per_second(filename):
    video = cv2.VideoCapture(filename)
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    return math.ceil(fps)


def color_grade(input_filename, output_filename):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(input_filename)

    # Check if camera opened successfully
    if (cap.isOpened() == False): 
        print("Unable to read video feed")

    # Defining the Codec
    # This is the important part, Codec is basically a compression technology to compress and decode video files
    fourcc = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')
    size = (int(cap.get(3)), int(cap.get(4)))
    fps = find_frames_per_second(input_filename)

    out = cv2.VideoWriter(output_filename, fourcc, fps, size)
    while True:
        ret, frame = cap.read()
        out.write(frame)

        if ret == True: 
            out.write(frame)
            cv2.imshow('frame',frame)

            # Break if "Q" is pressed on the keyboard
            if cv2.waitKey(1) & 0xFF == ord('q'): break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

color_grade("assets/clip2.mp4", "output/final.mp4")