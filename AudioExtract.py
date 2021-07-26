import moviepy.editor as mp
my_clip = mp.VideoFileClip(r"abc.mp4")
my_clip.audio.write_audiofile(r"my_result.wav")

#print(my_clip)