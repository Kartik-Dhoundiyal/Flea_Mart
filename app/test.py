from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create a new browser window
driver = webdriver.Chrome()

# Visit the home page of the Django app
driver.get("http://127.0.0.1:8000/")

uzu = "kadbubf12"


time.sleep(2)
signup = driver.find_element(By.XPATH, '/html/body/nav/div/a[3]')
signup.click()

time.sleep(2)
username = driver.find_element(By.XPATH, '//*[@id="id_username"]')
username.send_keys(uzu)

email = driver.find_element(By.XPATH, '//*[@id="id_email"]')
email.send_keys("garvy312@gmail.com")

password = driver.find_element(By.XPATH, '//*[@id="id_password1"]')
password.send_keys('MSIlaptop@1')

repassword = driver.find_element(By.XPATH, '//*[@id="id_password2"]')
repassword.send_keys('MSIlaptop@1')

time.sleep(2)
submit = driver.find_element(By.XPATH, '/html/body/div/div/form/button')
submit.click()

login = driver.find_element(By.XPATH, '//*[@id="id_username"]')
login.send_keys(uzu)
passwordd = driver.find_element(By.XPATH, '//*[@id="id_password"]')
passwordd.send_keys("MSIlaptop@1")
time.sleep(2)
print("Test Successfully")