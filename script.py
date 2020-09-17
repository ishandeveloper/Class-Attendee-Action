from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pause
import os
import sys
from datetime import datetime
from pyvirtualdisplay import Display

gmeet_username = sys.argv[1]
gmeet_password = sys.argv[2]

url_meet = sys.argv[3]

print(gmeet_username + gmeet_password + url_meet)

display = Display(visible=0, size=(800, 800))
display.start()
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("window-size=800,800")
options.add_experimental_option("prefs", {
options.add_argument('--no-sandbox')
options.add_argument("--headless")
    "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.notifications": 2
})
browser = webdriver.Chrome(options=options)
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))
browser.maximize_window()
browser.implicitly_wait(20)
username = browser.find_element_by_id('identifierId')
username.send_keys(gmeet_username)
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(5)

password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
password.send_keys(gmeet_password)

signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()
time.sleep(3)
browser.get(url_meet)
time.sleep(6)
element = browser.find_element_by_class_name('CwaK9')
browser.execute_script("arguments[0].click();", element)
browser.find_element_by_xpath(
    "//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()
time.sleep(3600)  #My Class Is One Hour Long
