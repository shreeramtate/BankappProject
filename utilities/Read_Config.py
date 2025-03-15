import configparser

config= configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig_class:
    @staticmethod
    def app_username():
        username = config.get("Login Data","username")
        return username

    @staticmethod
    def app_password():
        password = config.get("Login Data","password")
        return password

    @staticmethod
    def base_page_url():
        base_url = config.get("Application Urls","base_url")
        return base_url

    @staticmethod
    def login_page_url():
        login_url = config.get("Application Urls","login_url")
        return login_url

    @staticmethod
    def signup_page_url():
        signup_url = config.get("Application Urls","signup_url")
        return signup_url
