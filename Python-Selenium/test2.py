#!usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get("https://www.instagram.com/accounts/login/")
elem = browser.find_element_by_name("username")
elem.send_keys('Laptops' + Keys.RETURN)
time.sleep(4)
browser.quit()
