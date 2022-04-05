import moviepy.editor as mp


def cut_video(path_video, segments, folder_save, name, type_file):
    video = mp.VideoFileClip(path_video)
    duration = video.duration
    video_respon = []
    for start_seconds, end_seconds in segments:
        if (duration > start_seconds) : 
        # crop a video clip and add it to list
            try:
                sub_video = video.subclip(start_seconds, end_seconds)
                sub_video.write_videofile(folder_save + name + str(start_seconds) + type_file)
                video_respon.append(folder_save + name + str(start_seconds) + type_file)
            except:
                sub_video = video.subclip(start_seconds, None)
                sub_video.write_videofile(folder_save + name + str(start_seconds) + type_file)
                video_respon.append(folder_save + name + str(start_seconds) + type_file)
    return video_respon