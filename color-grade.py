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
    width = int(cap.get(3))
    height = int(cap.get(4))
    size = (width, height)
    fps = find_frames_per_second(input_filename)

    out = cv2.VideoWriter(output_filename, fourcc, fps, size)

    while True:
        # This is to resize the frame [Betters way of doing it. This is not goood!!]
        cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Frame', 600, 600)

        ret, frame = cap.read()
        if ret == True:
            # Add a color grade
            blue, green, red = cv2.split(frame)
            blue = np.clip(blue * 0.55, 0, 255).astype(np.uint8)  # Increase the blue channel
            green = np.clip(green * 0.55, 0, 255).astype(np.uint8)  # Decrease the green channel
            red = np.clip(red * 0.55, 0, 255).astype(np.uint8)  # Increase the red channel
            frame = cv2.merge((blue, green, red))

            cv2.imshow('Frame', frame)
            out.write(frame)
            # Break if "Q" is pressed on the keyboard
            if cv2.waitKey(1) & 0xFF == ord('q'): break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

color_grade("assets/clip2.mp4", "output/final.mp4")