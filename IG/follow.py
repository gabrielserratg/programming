from selenium import webdriver
from getpass import getpass
import time

#usr = raw_input("Enter your username: ")
#pwd = getpass("Enter your password: ")

usr = 'richardepsilva@gmail.com'
pwd = 'gabrielserra'


driver = webdriver.Firefox()
driver.get('https://www.instagram.com/accounts/login/')

time.sleep(2)

username_box = driver.find_element_by_name('username')
username_box.send_keys(usr)

password_box = driver.find_element_by_name('password')
password_box.send_keys(pwd)

time.sleep(1)

login_btn = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     '][@type='submit']")
login_btn.click()

time.sleep(4)

driver.get('https://instagram.com/gabrielsukinsyn')

time.sleep(1)

follow_btn = driver.find_element_by_xpath("//button[@class='BY3EC  sqdOP  L3NKy   y3zKF     '][@type='button']")
follow_btn.click()

#Timer for close Firefox driver / set time in time.sleep()
#time.sleep(5)
#driver.quit()

