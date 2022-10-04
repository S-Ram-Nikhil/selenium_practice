from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

service_obj=Service("D:\Documents\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

website_URL = "https://www.google.co.in/"
driver.get(website_URL)
driver.maximize_window()

# After how many seconds you want to refresh the webpage
# Few website count view if you stay there
# for a particular time
# you have to figure that out
refreshrate = int(20)

# This would keep running until you stop the compiler.
while True:
    time.sleep(refreshrate)
    driver.refresh()