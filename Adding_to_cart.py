import click as click
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service

service_obj=Service("D:\Documents\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)  # Creating the driver object

cart_button=(By.XPATH,"//a[@class='cart-icon']")
PROMO_CODE= (By.XPATH,"//*[@class='promoCode']")

# driver= webdriver.Chrome(executable_path="D:\Documents\chrome driver\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
# time.sleep(10)
# driver.minimize_window()

def click(locater):
    driver.find_element(*locater).click()

# search_bar=(By.XPATH,"//input[@type='search']")
# locater=driver.find_element((*search_bar))
# print(type(locater))


driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")

products= driver.find_elements(By.XPATH,"//div[@class='product']")
for product in products:
    product.find_element(By.XPATH, "div[3]/button").click()

driver.find_element(By.XPATH,"//a[@class='cart-icon']").click()


click((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']"))
driver.find_element(By.XPATH,"//*[@class='promoCode']").send_keys("rahulshettyacademy")

click((By.XPATH,"//*[@class='promoBtn']"))
promo_info= driver.find_element(By.XPATH,"//*[@class='promoInfo']")
print(promo_info.text)

click((By.XPATH,"//*[contains(text(),'Place Order')]"))
select= Select(driver.find_element(By.XPATH,"//select"))
select.select_by_value("India")
click((By.XPATH,"//input[@type='checkbox']"))
click((By.XPATH,"//*[contains(text(),'Proceed')]"))


success= driver.find_element(By.XPATH,"//*[@class='wrapperTwo']").text
print(success)
driver.quit()



