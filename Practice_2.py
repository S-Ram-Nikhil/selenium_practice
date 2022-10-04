from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org")
print(driver.title)
# Welcome to Python.org
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
# 'https://www.python.org/search/?q=getting+started+with+python&submit='
driver.close()
driver.switch_to_window('window_name')
print(driver.window_handles)
driver.switch_to_default_content()

# explicit wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
element = WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.ID, "id-of-new-element"))
)
finally:
driver.quit()

driver.implicitly_wait(5)
element = driver.find_element_by_id("id-of-new-element")

# unit test
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ChromeSearch(unittest.TestCase):

def setUp(self):
self.driver = webdriver.Chrome('./chromedriver')

def test_search_in_python_org(self):
driver = self.driver
driver.get("https://www.python.org")
self.assertIn("Python", driver.title)
elem = driver.find_element_by_name("q")
elem.send_keys("getting started with python")
elem.send_keys(Keys.RETURN)
assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == driver.current_url

def tearDown(self):
self.driver.close()

if __name__ == "__main__":
unittest.main()










