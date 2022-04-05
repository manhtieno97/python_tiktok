import moviepy.editor as mp

video = mp.VideoFileClip("/home/mingnm2/python/document/video/test.mp4")

duration = video.duration
print(duration)
