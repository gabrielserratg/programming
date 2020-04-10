import win32com.client
x = win32com.client.Dispatch("AppRobotic.API")
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
# navigate to Instagram
driver = webdriver.Firefox()
driver.get('https://www.instagram.com') 
# sleep 1 second
x.Wait(1000)
 
# attach to the 'login' button on homepage
login_link = browser.find_element_by_xpath(
'//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
# navigate to login page
login_link.click()
 
# wait for the username field to appear and type in username
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
x.Type("AppRobotic")
