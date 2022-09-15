import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service_obj=Service("D:\Documents\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)  # Creating the driver object

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.XPATH,"//input[@value='Confirm']").click()
time.sleep(2)
#
alert= driver.switch_to.alert
print(alert.text)
alert.dismiss()

driver.quit()

