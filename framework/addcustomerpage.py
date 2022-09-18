import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomer:
    """
    Add customer Page details- Email, Password,first_name,Last_name, gender, DOB, company name, Admin content box
    """
    TXT_EMAIL = (By.XPATH, "//input[@id='Email']")
    TXT_PASSWORD = (By.XPATH, "//input[@id='Password']")
    TXT_FIRST_NAME = (By.XPATH, "//input[@id='FirstName']")
    TXT_LAST_NAME = (By.XPATH, "//input[@id='LastName']")
    MALE_GENDER = (By.XPATH, "//*[@id='Gender_Male']")
    FEMALE_GENDER = (By.XPATH, "//*[@id='Gender_Female']")
    TXT_DOB = (By.XPATH, "//input[@id='DateOfBirth']")
    LINK_CUSTOMERS_MENU = (By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a")
    lINK_CUSTOMERS_MENU_ITEM = (By.XPATH, "//a[@href='/Admin/Customer/List']")
    BTN_ADD_NEW = (By.XPATH, "//a[@class='btn btn-primary']")
    MGR_OF_VENDOR = (By.XPATH, "//*[@id='VendorId']")
    TXT_COMPANY_NAME = (By.XPATH, "//input[@id='Company']")
    TXT_ADMIN_CONTENT = (By.XPATH, "//textarea[@id='AdminComment']")
    BTN_SAVE = (By.XPATH, "//button[@name='save']")

    def __init__(self, driver):
        self.driver = driver

    def clickonCustomersmenu(self):
        """
        method to click on customer menu bar
        :return: none
        """
        self.driver.find_element(*self.LINK_CUSTOMERS_MENU).click()

    def clickoncustomersmenuitem(self):
        """
        method to click on customer menu items
        :return: none
        """
        self.driver.find_element(*self.lINK_CUSTOMERS_MENU_ITEM).click()

    def clickonaddnew(self):
        """
        method to add new customer details
        :return: none
        """
        self.driver.find_element(*self.BTN_ADD_NEW).click()

    def setemail(self, email):
        """
        method to add email address
        :param email: Email id of the customer
        :return:none
        """
        self.driver.find_element(*self.TXT_EMAIL).send_keys(email)

    def setpassword(self, password):
        """
        method to set a  password to customer
        :param password: login password
        :return:none
        """
        self.driver.find_element(*self.TXT_PASSWORD).send_keys(password)

    def setmanagerofvendor(self, value):
        drp = Select(self.driver.find_element(*self.MGR_OF_VENDOR))
        drp.select_by_visible_text(value)

    def setgender(self, gender):
        """
        method to add gender
        :param gender: customer gender
        :return: none
        """
        if gender == 'Male':
            self.driver.find_element(*self.MALE_GENDER).click()
        elif gender == 'Female':
            self.driver.find_element(*self.FEMALE_GENDER).click()
        else:
            self.driver.find_element(*self.MALE_GENDER).click()

    def setfirstname(self, fname):
        """
        method to add first name of the customer
        :param fname: first name of customer
        :return: none
        """
        self.driver.find_element(*self.TXT_FIRST_NAME).send_keys(fname)

    def setlastname(self, lname):
        """
        method to add last name of the customer
        :param lname: customer last name
        :return: none
        """
        self.driver.find_element(*self.TXT_LAST_NAME).send_keys(lname)

    def setdob(self, dob):
        """
        method to add Date of birth of  customer
        :param dob: Customer Date of birth
        :return:none
        """
        self.driver.find_element(*self.TXT_DOB).send_keys(dob)

    def setcompanyname(self, comname):
        """
        method to add company name
        :param comname: company name of the customer
        :return:none
        """
        self.driver.find_element(*self.TXT_COMPANY_NAME).send_keys(comname)

    def setadmincontent(self, content):
        """
        method to add comments by admin in the final comments
        :param content: admin comments
        :return:none
        """
        self.driver.find_element(*self.TXT_ADMIN_CONTENT).send_keys(content)

    def clickonsave(self):
        """
        method to save the form details.
        :return: none
        """
        self.driver.find_element(*self.BTN_SAVE).click()
