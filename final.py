# AUTOMATION ASSIGNMENT
# GIFFARI AL HAFIDZ
# https://itera-qa.azurewebsites.net/home/automation

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service()
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation/")
driver.maximize_window()
time.sleep(3)

# Textarea
driver.find_element(By.XPATH,"//*[@id='name']").send_keys("Testing")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='phone']").send_keys("+6289xxxxxx")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("testing@test.com")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("Testing")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='address']").send_keys("Testing")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/button").click()

# Checkbox and Radio Button
time.sleep(2)
radiob = driver.find_element(By.ID,'male')
radiob.click()

time.sleep(2)
driver.find_element(By.ID,'monday').click()
time.sleep(2)
driver.find_element(By.ID,'wednesday').click()
time.sleep(2)
driver.find_element(By.ID,'friday').click()
time.sleep(2)
driver.find_element(By.ID,'saturday').click()

# Dropdown
time.sleep(2)
dd = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/select/option[3]')
dd.click()

# Checkbox and Radio Button Xpath
time.sleep(2)
radio = driver.find_element(By.XPATH,'//label[@for="2years"]')
radio.click()

time.sleep(2)
cbox = driver.find_element(By.XPATH,'//label[@for="selenium"]')
cbox.click()

# File input
# The files must be in systems
# Hover mouse cursor to upload form to see it works or not
time.sleep(2)
driver.find_element(By.ID,'inputGroupFile02').send_keys("D:/A-Test/0.py")

time.sleep(2)
driver.close()