from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

usr='gf3ifzw4n32h@gmail.com'
pwd='ce878ce872064b03'
  
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
sleep(2)
try:
        buttun_login = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[2]')
        buttun_login.click()
        sleep(2)

        buttun_login_lat = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[1]/a')
        buttun_login_lat.click()
        sleep(2)
        username_box = driver.find_element_by_name('email')
        username_box.send_keys(usr)
        print ("Email Id entered")
        sleep(5)
  
        password_box = driver.find_element_by_name('password')
        password_box.send_keys(pwd)
        print ("Password entered")
        sleep(5)
        login_box = driver.find_element_by_tag_name('button')
        login_box.click()
except:
        print ("Done")

  
print ("Done")
input('Press anything to quit:')
driver.quit()
print("Finished")