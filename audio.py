from moviepy.editor import *

# To add audio to the file
quote1 = AudioFileClip("quotes/quote1.mp3")
clip = VideoFileClip("output/colorgraded.mp4")
videoclip = clip.set_audio(quote1)
videoclip.write_videofile("output/final_with_audio.mp4")