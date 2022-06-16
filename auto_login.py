from conect_db import data
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM

usr = data
path = "--user-data-dir=Cockei/" + usr + " Data"
print(path);
print('=====================================================================================================')
print('Heyy, you have to login manully on tiktok, so the bot will wait you 1 minute for loging in manually!')
print('=====================================================================================================')
time.sleep(2)

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# avoiding detection
options.add_argument('--disable-blink-features=AutomationControlled')

# Default User Profile
options.add_argument("--profile-directory=Default")
options.add_argument(path)

driver = webdriver.Chrome(options=options,  executable_path=CM().install())
driver.set_window_size(1680, 900)
driver.get('https://www.tiktok.com/login')
print ("Opened tiktok")

time.sleep(5)
driver.get('https://www.tiktok.com/upload?lang=en')
time.sleep(10)

# for video in videos:
#     print(video)