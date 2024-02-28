
from cv2 import normalize
import moviepy.editor as mpe
import time
from moviepy.video.compositing.transitions import crossfadein, crossfadeout
from moviepy.video.fx.all import fadein, fadeout
# import moviepy as mp
# import cv2
# import numpy as np
# from scipy import stats

# timer code ...
start_time = time.time()

# config ...
mic_information = "MIC INFORMATION"
main_video_path = "you_video.mp4"
normalize_audio = True
generate_video_description = True

main_video = mpe.VideoFileClip(main_video_path)

# # generate video description...
# if generate_video_description:
#     # write audio wav to 16Hz...
#     main_video.audio.write_audiofile("main_video_audio.wav", fps=16000, nbytes=2, buffersize=2000, write_logfile=False, verbose=True, logger='bar')

# normalize main vídeo áudio...
if normalize_audio:
    main_video.audio = main_video.audio.fx(mpe.afx.audio_normalize)

overlays = []
if main_video.duration > 60:
    # mic info (litte info about you and your mic)
    overlay_mic = mpe.TextClip(mic_information.upper(), fontsize=20, color='yellow', ).set_position(("right", "top")).set_duration(5)
    overlays.append(overlay_mic)

    # about me txt (this you must create)
    overlay_about_me = mpe.VideoFileClip("resources/about_me.mp4") 
    overlay_about_me = overlay_about_me.fx(mpe.vfx.mask_color, color=[0, 0, 0], thr=90, s=3)
    overlays.append(overlay_about_me)

    # overlay ...
    overlay1 = mpe.VideoFileClip("resources/ANIMAÇÃO FLASH 1.mp4")
    overlay1 = overlay1.fx(mpe.vfx.mask_color, color=[2, 136, 0], thr=90, s=3)
    overlays.append(overlay1)

if main_video.duration > 600:
    # overlay ...
    overlay2 = mpe.VideoFileClip("resources/ANIMAÇÃO FLASH 2.mp4")
    # .set_start((main_video.duration - 10) / 3)
    overlay2 = overlay2.fx(mpe.vfx.mask_color, color=[2, 136, 0], thr=90, s=3)
    overlays.append(overlay2)

if main_video.duration > 1200:
    # overlay ...
    overlay3 = mpe.VideoFileClip("resources/ANIMAÇÃO FLASH 3.mp4")
    overlay3 = overlay3.fx(mpe.vfx.mask_color, color=[2, 136, 0], thr=90, s=3)
    overlays.append(overlay3)

if main_video.duration > 3600:
    # overlay ...
    overlay4 = mpe.VideoFileClip("resources/ANIMAÇÃO FLASH 1.mp4")
    overlay4 = overlay4.fx(mpe.vfx.mask_color, color=[2, 136, 0], thr=90, s=3)
    overlays.append(overlay4)

# Adjust overlays
    
if overlays:
    overlays[0] = overlays[0].set_start(5) # mic info
    overlays[1] = overlays[1].set_start(5) # about me
    overlays[2] = overlays[2].set_start(overlays[1].duration + 5) # first overlay ...

if len(overlays) > 3:
    overlays[-1] = overlays[-1].set_start(main_video.duration - (overlays[-1].duration + 10)) # last overlay ...


if len(overlays) > 4:
    middle_overlays_count = len(overlays) - 4
    division_factor = middle_overlays_count + 1
    overlay_position = 0
    for i in range(3, len(overlays) - 1):
        overlay_position += 1
        overlays[i] = overlays[i].set_start(((main_video.duration / division_factor) * overlay_position) - (overlays[i].duration / 2)) # other overlays ...

# print all overlays start time ...
for i in range(len(overlays)):
    print("overlay %s start time: %s" % (i, overlays[i].start))

video_with_overlay = mpe.CompositeVideoClip([main_video] + overlays)

# intro and folder image you must create...
video_intro = mpe.VideoFileClip("resources/video_intro.mp4").set_duration(7)
video_folder = mpe.ImageClip("resources/video_folder.png").set_duration(7)

video_with_overlay = video_with_overlay.resize(height=1080, width=1920)
video_intro = video_intro.resize(height=video_with_overlay.h, width=video_with_overlay.w)
video_folder = video_folder.resize(height=video_with_overlay.h, width=video_with_overlay.w)

# Apply fade-in and fade-out to each clip
video_intro = video_intro.fx(fadein, 1).fx(fadeout, 1)
video_folder = video_folder.fx(fadein, 1).fx(fadeout, 1)
video_with_overlay = video_with_overlay.fx(fadein, 1).fx(fadeout, 1)

# Create a list of clips with crossfade
clips = [video_intro, video_folder.crossfadein(1), video_with_overlay.crossfadein(1)]

# Concatenate clips with crossfade
final_video = mpe.concatenate_videoclips(clips, method="compose") # .set_duration(30)

# final_video = mpe.concatenate_videoclips([
#     video_intro,
#     video_folder.crossfadein(1),
#     video_with_overlay.crossfadein(1)
#     ], method='compose', bg_color=None).set_duration(30)

final_video.write_videofile("final_video.mp4", 
                            threads=8, 
                            preset='medium', # ultrafast superfast veryfast faster fast medium slow slower veryslow placebo
                            # remove_temp=True, 
                            # write_logfile=False, 
                            # verbose=True, 
                            # logger='bar'
                            )

print("--- %s ---" % time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))