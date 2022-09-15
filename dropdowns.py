import click as click
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service

service_obj=Service("D:\Documents\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)  # Creating the driver object
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ram")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys(("ram@gmail.com"))
driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys(("pass@123"))
driver.find_element(By.XPATH,"//input[@id='exampleCheck1']").click()

# 'select' element
dropdown= Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
driver.find_element(By.XPATH,"//*[@id='inlineRadio2']").click()

driver.find_element(By.XPATH,"//input[@type='date']").send_keys("18----2022")

driver.quit()

# click((By.XPATH, "//input[@value='Submit']"))
# driver.find_element((By.XPATH,"//input[@type='submit']")).click()
# driver.find_element(By.XPATH, "//div[2]/button").click()