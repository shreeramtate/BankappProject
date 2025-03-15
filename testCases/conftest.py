import pytest
from selenium import webdriver
from utilities.Read_Config import ReadConfig_class

@pytest.fixture(scope="class")
def setup(request):
    global driver

    browser_value = request.config.getoption("--browser")
    if browser_value == "chrome":
        print("launching chrome browser")
        driver = webdriver.Chrome()
    elif browser_value == "firefox":
        print("launching Firefox browser")
        driver = webdriver.Firefox()
    elif browser_value == "edge":
        print("launching Edge browser")
        driver = webdriver.Edge()
    elif browser_value == "headless":
        print("launching Headless browser")
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Edge(options=options)

    driver.maximize_window()
    driver.implicitly_wait(15)
    request.cls.driver = driver
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", default="edge")


# username = ReadConfig_class.app_username()
# password = ReadConfig_class.app_password()
# base_url = ReadConfig_class.base_page_url()
# login_url = ReadConfig_class.login_page_url()
# sign_up_url = ReadConfig_class.signup_page_url()
