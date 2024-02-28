from moviepy.editor import *
from moviepy.video.compositing.concatenate import concatenate_videoclips

# Load your two video clips
clip1 = VideoFileClip("/Users/marciusbezerra/Dropbox/CodeTotal/CodeTotal/Video Intro.mp4")
clip2 = ImageClip("/Users/marciusbezerra/Downloads/info.png").resize(height=1080, width=1920).set_duration(7)

clips = [clip1, clip2]

slided_clips = [CompositeVideoClip([clip.fx( transfx.slide_out, 1, 'bottom')]) for clip in clips]
final_video = concatenate( slided_clips, padding=-1)

# Write the result to a file
final_video.write_videofile("output.mp4")