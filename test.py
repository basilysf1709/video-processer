# Tested a lot of things here and I did not want to delete

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

    if not cap.isOpened():
        print("Error openeing Video File")

    # Defining the Codec
    # This is the important part, Codec is basically a compression technology to compress and decode video files
    fourcc = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')
    size = (int(cap.get(3)), int(cap.get(4)))
    fps = find_frames_per_second(input_filename)

    out = cv2.VideoWriter(output_filename, fourcc, fps, size)

    while True:
        # This is to resize the frame [Betters way of doing it. This is not goood!!]
        cv2.namedWindow('Frame1', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Frame1', 600, 600)
        cv2.namedWindow('Frame2', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Frame2', 600, 600)
        cv2.namedWindow('Frame3', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Frame3', 600, 600)

        ret, frame = cap.read()
        if ret == True: 
            out.write(frame)
            # Color Grading goes on here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            filtered_frame = cv2.applyColorMap(gray, cv2.COLORMAP_BONE)
            blended_frame = cv2.addWeighted(frame, 0.3, filtered_frame, 0.7, 40)
            # to sharpen the frame
            laplacian = cv2.Laplacian(frame, cv2.CV_8U)
            sharpened_frame = cv2.add(frame, laplacian)
            # To increase the contrast of the frame
            contrast_frame = cv2.normalize(sharpened_frame, None, 0, 255, cv2.NORM_MINMAX)
            # To show the frame 
            cv2.imshow('Frame1', frame)
            cv2.imshow('Frame2', contrast_frame)
            cv2.imshow('Frame3', blended_frame)
            # Break if "Q" is pressed on the keyboard
            if cv2.waitKey(1) & 0xFF == ord('q'): break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

color_grade("assets/clip2.mp4", "output/final.mp4")