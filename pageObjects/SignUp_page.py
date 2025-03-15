from selenium.webdriver.common.by import By


class signUp_page_class:

    signup_page_userID="username"
    signup_page_passwordID="password"
    signup_page_emailID="email"
    signup_page_phoneID="phone"
    signup_page_click_button_ID="createUserButton"

    def __init__(self, driver):
        self.driver = driver

    def enter_signUp_username(self,username):
        self.driver.find_element(By.ID,self.signup_page_userID).send_keys(username)

    def enter_signUp_password(self,password):
        self.driver.find_element(By.ID, self.signup_page_passwordID).send_keys(password)

    def enter_signUp_email(self,emailid):
        self.driver.find_element(By.ID, self.signup_page_emailID).send_keys(emailid)

    def enter_signUp_phone(self,phoneno):
        self.driver.find_element(By.ID, self.signup_page_phoneID).send_keys(phoneno)

    def SignUp_button_click(self):
        self.driver.find_element(By.ID, self.signup_page_click_button_ID).click()



