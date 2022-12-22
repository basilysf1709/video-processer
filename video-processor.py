from moviepy.editor import *

# function to remove audio of a clip
def removeAudio(clip):
    try:
        edit_clip = clip.without_audio()
        return edit_clip
    except Exception as e:
        print("Error Occured")
        return 

# function to combine different clips
def combineClips(list_of_clips, final_clip_number):
    try:
        combined = concatenate_videoclips(list_of_clips)
        combined.write_videofile("output/final{}.mp4".format(final_clip_number))
    except Exception as e:
        print("Error occured")

clip1 = VideoFileClip("assets/clip1.mp4")
clip2 = VideoFileClip("assets/clip2.mp4")
clip3 = VideoFileClip("assets/clip3.mp4")
clip4 = VideoFileClip("assets/clip4.mp4")

clips = [clip1, clip2, clip3, clip4]

for i in range(len(clips)):
    clips[i] = removeAudio(clips[i])
combineClips(clips, 1)
