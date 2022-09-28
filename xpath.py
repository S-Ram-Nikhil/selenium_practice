
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Syntax-
# Xpath=//tagname[@attribute='value']

# // : Select current node.
# Tagname: Tagname of the particular node.
# @: Select attribute.
# Attribute: Attribute name of the node.
# Value: Value of the attribute.

service_obj = Service("D:\Documents\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("http://demo.guru99.com/test/selenium-xpath.html")

# Basic xpath-
Xpath = //input[@name='uid']
Xpath = //input[@type='text']
Xpath =	//label[@id='message23']
Xpath=	//input[@value='RESET']
Xpath=//*[@class='barone']

# contains -
Xpath=//*[contains(@type,'sub')]
Xpath=//*[contains(@name,'btn')]
Xpath=//*[contains(@id,'message')]



