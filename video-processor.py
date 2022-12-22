from moviepy.editor import *


clip = VideoFileClip("assets/clip1.mp4")
edit_clip = clip.without_audio()
edit_clip.write_videofile("output/final1.mp4")