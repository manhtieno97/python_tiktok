import moviepy.editor as mp


def cut_video(path_video, segments, folder_save, name, type_file):
    video = mp.VideoFileClip(path_video)
    duration = video.duration
    video_respon = []
    number = duration/(segments*60)
    for x in range(0, (round(number)+1)):
        start_seconds = x*60*segments
        print(start_seconds)
        end_seconds = (x+1)*60*segments
        if(end_seconds > duration):
            end_seconds = duration
        sub_video = video.subclip(start_seconds, end_seconds)
        sub_video.write_videofile(folder_save + name + str(start_seconds) + type_file)
        video_respon.append(folder_save + name + str(start_seconds) + type_file)
    return video_respon