from selenium import webdriver
from getpass import getpass

usr = 'gabriel@gmail.com'
pwd = 'gabriel'

driver = webdriver.Firefox()
driver.get('https://www.instagram.com/accounts/login/')

username_box = driver.find_element_by_xpath("//input[@name=\"username\"]")\
.send_keys(usr)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id('u_0_2')
login_btn.submit()
