from selenium import webdriver
from getpass import getpass

usr = 'gabrielserratg@gmail.com'
pwd = 'Delorean2019'

driver = webdriver.Firefox()
driver.get('https://www.instagram.com/accounts/login/')

username_box = driver.find_element_by_name('username')
username_box.send_keys(usr)

password_box = driver.find_element_by_name('Password')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id('u_0_2')
login_btn.submit()
