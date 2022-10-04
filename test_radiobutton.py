import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):
    def setup(self):
        service_obj = Service("D:\Documents\chrome driver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_obj)
        self.driver.get("https://shop.thetestingworld.com/")

    def tearDown(self):
        self.driver.quit()

    def testName(self):
        self.driver.find_element(By.NAME,"search").send_keys("Iphone")
        self.driver.find_element(By.XPATH,"//div[@id='search']/span/button").click()



if __name__=="__main__":
    unittest.main()