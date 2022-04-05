import string
from download_youtube import download
from cut_video import cut_video
from upload import upload,check_exists_by_xpath
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM

path_folder = "/home/mingnm2/python/document/video/"
name_file = "tiktok" + time.strftime("%Y%m%d-%H%M%S")
type_file = ".mp4"
link = "https://www.youtube.com/watch?v=xWOoBJUqlbI"

download(link, path_folder, name_file + type_file)
path = path_folder + name_file + type_file

segments = [(0, 180),
            (180, 360),(360,540)]
videos = cut_video(path, segments, path_folder, name_file, type_file)

for video in videos:
    print(video)
    print('=====================================================================================================')
    print('Heyy, you have to login manully on tiktok, so the bot will wait you 1 minute for loging in manually!')
    print('=====================================================================================================')
    time.sleep(8)
    print('Running bot now, get ready and login manually...')
    time.sleep(4)

    options = webdriver.ChromeOptions()
    bot = webdriver.Chrome(options=options,  executable_path=CM().install())
    bot.set_window_size(1680, 900)

    bot.get('https://www.tiktok.com/login')
    ActionChains(bot).key_down(Keys.CONTROL).send_keys(
        '-').key_up(Keys.CONTROL).perform()
    ActionChains(bot).key_down(Keys.CONTROL).send_keys(
        '-').key_up(Keys.CONTROL).perform()
    print('Waiting 50s for manual login...')
    time.sleep(50)
    bot.get('https://www.tiktok.com/upload/?lang=en')
    time.sleep(3)
    upload(video, bot)