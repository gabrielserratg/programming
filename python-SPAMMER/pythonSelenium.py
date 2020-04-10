#
from selenium import webdriver
import time
import random
print("Excute with Python3")
driver = webdriver.Firefox()

driver.get("https://web.whatsapp.com")

#button click configs

time.sleep(10)

#btnconfig = driver.find_element_by_class_name('')
btnconfig = driver.find_element_by_xpath("//button[@d='M12 7a2 2 0 1 0-.001-4.001A2 2 0 0 0 12 7zm0 2a2 2 0 1 0-.001 3.999A2 2 0 0 0 12 9zm0 6a2 2 0 1 0-.001 3.999A2 2 0 0 0 12 15z'][@type='submit']")
btnconfig.click()

