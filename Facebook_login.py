from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user_name = "suryadevararmnikhil@gmail.com"
password = "YOUR PASSWORD"

service_obj=Service("D:\Documents\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)


driver.get("https://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(5)

element = driver.find_element(By.ID,"email")
element.send_keys(user_name)
element = driver.find_element(By.ID,"pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
driver.quit()