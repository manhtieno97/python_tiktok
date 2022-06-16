import string

from download_youtube import download
from cut_video import cut_video
import time
from conect_db import select_link_youtube,uppdate_status_link

path_folder = "/home/manhtien/python/tiktok/video/youtube/"
type_file = ".mp4"

link_db = select_link_youtube()
name_file = link_db[1]
link = link_db[0]
download(link, path_folder, name_file + type_file)
path = path_folder + name_file + type_file

# segments = [(0, 180),
#             (180, 360),(360,540),(540,720),(720,900)]
if(link_db[2]):
    segments = link_db[2]
else:
    segments = 5

videos = cut_video(path, segments, path_folder, name_file, type_file)

uppdate_status_link(link_db[3])
