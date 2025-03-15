
from selenium.webdriver.common.by import By

class login_page:
    login_username_ID="username"
    login_password_ID="password"
    login_button_ID="loginButton"

    def __init__(self, driver):
        self.driver = driver

    def loginUsername(self,username):
        self.driver.find_element(By.ID,self.login_username_ID).clear()
        self.driver.find_element(By.ID, self.login_username_ID).send_keys(username)

    def loginPassword(self,password):
        self.driver.find_element(By.ID,self.login_password_ID).clear()
        self.driver.find_element(By.ID, self.login_password_ID).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.ID,self.login_button_ID).click()







