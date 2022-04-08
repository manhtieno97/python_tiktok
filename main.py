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

usr='gf3ifzw4n32h@gmail.com'
pwd='ce878ce872064b03'

path_folder = "/home/mingnm2/python/document/video/"
name_file = "tiktok" + time.strftime("%Y%m%d-%H%M%S")
type_file = ".mp4"
link = "https://www.youtube.com/watch?v=xWOoBJUqlbI"

# download(link, path_folder, name_file + type_file)
# path = path_folder + name_file + type_file

segments = [(0, 180),
            (180, 360),(360,540)]
# videos = cut_video(path, segments, path_folder, name_file, type_file)


print('=====================================================================================================')
print('Heyy, you have to login manully on tiktok, so the bot will wait you 1 minute for loging in manually!')
print('=====================================================================================================')
time.sleep(4)

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# avoiding detection
options.add_argument('--disable-blink-features=AutomationControlled')

# Default User Profile
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=C:/Users/Admin/AppData/Local/Google/Chrome/User Data")

driver = webdriver.Chrome(options=options,  executable_path=CM().install())
driver.set_window_size(1680, 900)
driver.get('https://www.tiktok.com/login')
print ("Opened tiktok")
time.sleep(4)
try:
        buttun_login = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[2]')
        buttun_login.click()
        time.sleep(4)

        buttun_login_lat = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[1]/a')
        buttun_login_lat.click()
        time.sleep(4)
        username_box = driver.find_element_by_name('email')
        username_box.send_keys(usr)
        print ("Email Id entered")
        time.sleep(4)
  
        password_box = driver.find_element_by_name('password')
        password_box.send_keys(pwd)
        print ("Password entered")
        time.sleep(4)
        login_box = driver.find_element_by_tag_name('button')
        login_box.click()
except:
        print ("Done")
time.sleep(5)
driver.get('https://www.tiktok.com/upload?lang=en')
time.sleep(10)

# for video in videos:
#     print(video)
upload("/home/mingnm2/python/document/video/tiktok20220406-0823360.mp4", driver)