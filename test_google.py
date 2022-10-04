from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def test_eight_components():
# driver = webdriver.Chrome()
    service_obj=Service("D:\Documents\chrome driver\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://google.com")
    title = driver.title
    driver.maximize_window()
# print(title)
    assert title == "Google"
    driver.implicitly_wait(0.5)
    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")
    search_box.send_keys("Selenium")
    search_button.click()
    search_box = driver.find_element(by=By.NAME, value="q")
    value = search_box.get_attribute("value")
    assert value == "Selenium"
    driver.quit()


