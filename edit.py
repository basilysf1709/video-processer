from moviepy.editor import *

# function to trim the clip
def trim_clip(clip, start, end):
    try:
        return clip.subclip(start, end)
    except Exception as e:
        print(e)
        return

# function to resize the clip
def resize_clip(clip):
    try:
        return clip.resize(height=360)
    except Exception as e:
        print(e)
        return

# function to remove audio of a clip
def remove_audio(clip):
    try:
        edit_clip = clip.without_audio()
        return edit_clip
    except Exception as e:
        print(e)
        return 

# function to combine different clips
def combine_clips(list_of_clips, final_clip_number):
    try:
        combined = concatenate_videoclips(list_of_clips)
        combined.write_videofile("output/final{}.mp4".format(final_clip_number))
    except Exception as e:
        print(e)

# function to extract audio from a video
def extract_audio(clip):
    try:
        audio = clip.audio
        return audio
    except Exception as e:
        print(e)
        return

# function to convert video to gif file
def convert_clip_to_gif(clip, filename):
    try:
        return clip.write_gif(filename)
    except Exception as e:
        print(e)
        return



# clip1 = VideoFileClip("assets/clip1.mp4")
# clip2 = VideoFileClip("assets/clip2.mp4")
# clip3 = VideoFileClip("assets/clip3.mp4")
# clip4 = VideoFileClip("assets/clip4.mp4")

# clips = [clip1, clip2, clip3, clip4]

# for i in range(len(clips)):
#     clips[i] = resize_clip(clips[i])
#     clips[i] = remove_audio(clips[i])
# combine_clips(clips, 1)



