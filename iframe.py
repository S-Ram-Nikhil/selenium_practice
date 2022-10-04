from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service_obj=Service("D:\Documents\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)  # Creating the driver object
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(5)

driver.switch_to.frame("mce_0_ifr")
text_box= driver.find_element(By.XPATH,"//body[@id='tinymce']")
text_box.clear()
text_box.send_keys(("Start writing here"))
driver.switch_to.default_content()

time.sleep(10)

driver.close()
