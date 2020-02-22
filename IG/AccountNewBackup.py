from selenium import webdriver
from getpass import getpass
import time
import random

#login advanced

#usr = raw_input("Enter your username: ")
#pwd = getpass("Enter your password: ")

#login simpled

#usr = 'richardepsilva@gmail.com'
#pwd = 'gabrielserra'

#wordlist for make accounts generator

#WDfullname = 'henrique da silva'
WDemail = 'henriquesilveira@gmail.com'
WDpassword = 'gabrielserra'

#Generator Full names for making accounts and infos viewer

Filename='/root/Desktop/programming/Python-resultados/firstnames.txt'
File=open(Filename,'r').readlines()
WDfullname=random.choice(File)[:-1]
WDfullname=WDfullname+' '
WDfullname=WDfullname+random.choice(File)[:-1]
print ("Full Name: " + WDfullname)
print ("Email: " + WDemail)
print ("Password: " + WDpassword)

#page for login direct

driver = webdriver.Firefox() #no change
#driver.get('https://www.instagram.com/accounts/login/')

#page for Sign Up

driver.get('https://www.instagram.com/accounts/emailsignup/')

time.sleep(2)

#account creator

#email
username_box = driver.find_element_by_name('emailOrPhone')
username_box.send_keys(WDemail)

#nome completo
username_box = driver.find_element_by_name('fullName')
username_box.send_keys(WDfullname)

#password
username_box = driver.find_element_by_name('password')
username_box.send_keys(WDpassword)

time.sleep(2)

#generator nick
nick_btn = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     '][@type='button']")
nick_btn.click()

time.sleep(1)

#click on button sign up
signup_btn = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     '][@type='submit']")
signup_btn.click()

#Login simple
#username_box = driver.find_element_by_name('username')
#username_box.send_keys(usr)

#password_box = driver.find_element_by_name('password')
#password_box.send_keys(pwd)

time.sleep(1)

#button for login default
#login_btn = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     '][@type='submit']")
#login_btn.click()

time.sleep(4)

#Account for follow
#driver.get('https://instagram.com/gabrielsukinsyn')

time.sleep(1)

#follow my account ig
#follow_btn = driver.find_element_by_xpath("//button[@class='BY3EC  sqdOP  L3NKy   y3zKF     '][@type='button']")
#follow_btn.click()

#Timer for close Firefox driver / set time in time.sleep()
#time.sleep(5)
#driver.quit()
