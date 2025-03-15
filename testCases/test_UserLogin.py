import random
import string
from faker import Faker

import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.Logger_utility import logger_class
from pageObjects.SignUp_page import signUp_page_class
from pageObjects.LoginClass import login_page
from testCases.conftest import setup
from utilities.Read_Config import ReadConfig_class

@pytest.mark.usefixtures("setup")
class Test_login:

    username = ReadConfig_class.app_username()
    password = ReadConfig_class.app_password()
    base_url = ReadConfig_class.base_page_url()
    login_url = ReadConfig_class.login_page_url()
    sign_up_url = ReadConfig_class.signup_page_url()
    log = logger_class.log_gen_method()

    driver=None

    @pytest.mark.depedency(name="test_url_001")
    def test_url_001(self):
        self.log.info("Testing basic site url")
        self.log.info(f"Entering base page url: {self.base_url} ")
        self.driver.get(self.base_url)
        if self.driver.title == "Bank Application":
            assert True
            self.log.info("Base Url test case is passed")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_url_Pass001.png")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_verify_url_Fail001.png")
            self.log.info("Base Url test case is Failed")
            assert False

    @pytest.mark.dependency(depends=["test_url_001"])
    def test_login_002(self):
        self.log.info("Login Page Url test case")
        self.log.info(f"Login Page url :{self.login_url}")
        self.driver.get(self.login_url)
        lp=login_page(self.driver)
        lp.loginUsername(self.username)
        lp.loginPassword(self.password)
        lp.ClickLogin()

        if self.driver.title == "Dashboard":
            assert True
            self.log.info("Login Page Url test case is passed")
            self.driver.save_screenshot("G:\\CREDENCE\\CT-REVISION DEC 2024\\BANK_APP_PROJECT\\Screenshots\\LoginUrl_pass001.png")
        else:
            self.driver.save_screenshot("G:\\CREDENCE\\CT-REVISION DEC 2024\\BANK_APP_PROJECT\\Screenshots\\LoginUrl_Fail002.png")
            self.log.error("Login Page Url test case is fail")
            assert False


    # @pytest.mark.group1
    @pytest.mark.dependency(depends=["test_url_001"])
    def test_signup_page_003(self):
        faker = Faker('en_IN')
        self.log.info("Testing Sign Up URL")
        self.log.info(f"Checking Sign up URL {self.sign_up_url}")
        self.driver.get(self.sign_up_url)
        sp=signUp_page_class(self.driver)

        username=faker.user_name()
        self.log.info(f"Entering username{username}")
        sp.enter_signUp_username(username)
        self.log.info("Entering Password 'Admin@123'")
        sp.enter_signUp_password("Admin@123")
        email=faker.email()
        self.log.info(f"Entering Password Email address {email}")
        sp.enter_signUp_email(email)
        time.sleep(1)
        # phone_no=faker.phone_number()
        phone_no = faker.phone_number().replace('+', '').strip()
        self.log.info(f"Entering Phone number {phone_no}")
        sp.enter_signUp_phone(phone_no)
        time.sleep(2)
        sp.SignUp_button_click()
        time.sleep(5)
        message = self.driver.find_element(By.ID,"successMessage")
        print(f"Driver Message after User creation is:{message.text}\n")
        self.log.info("Checking User sign up Page title")
        if message.text == "User created successfully":
            assert True
            self.log.info("Sign up title Page successfully verified")
            print("TestCase for User Creation passed successfully")
            self.driver.save_screenshot("G:\\CREDENCE\\CT-REVISION DEC 2024\\BANK_APP_PROJECT\\Screenshots\\test_signup_page_pass.png")
        else:
            print("TestCase for User Creation Failed")
            self.log.info("Sign up title Page not verified")
            self.driver.save_screenshot("G:\\CREDENCE\\CT-REVISION DEC 2024\\BANK_APP_PROJECT\\Screenshots\\test_signup_page_fail.png")
            assert False


    # pytest -v -s --html=Reports/myreport3.html
    # In query for report path '/' slas is correct.
    # pytest -v -s --html=Report/my_report.html -n auto --browser headless


