from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

usr='gf3ifzw4n32h@gmail.com'
pwd='ce878ce872064b03'
  
options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
driver = webdriver.Chrome(options=options,  executable_path=CM().install())
driver.set_window_size(1680, 900)
driver.get('https://www.tiktok.com/login/phone-or-email/email')
print ("Opened tiktok")
sleep(1)
ActionChains(driver).key_down(Keys.CONTROL).send_keys(
        '-').key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys(
        '-').key_up(Keys.CONTROL).perform()
username_box = driver.find_element_by_name('email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)
  
password_box = driver.find_element_by_name('password')
password_box.send_keys(pwd)
print ("Password entered")
sleep(5)
login_box = driver.find_element_by_tag_name('button')
login_box.click()
  
print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")