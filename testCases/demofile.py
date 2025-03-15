#
# from faker import Faker
# # fake=Faker()
# fake=Faker(["en_IN"])
#
# print("My address is", fake.address())
#
# print("My email id", fake.email())
#
# print("Mobile no", fake.phone_number())



#Not running below code just for reference from chatGpt.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the path to your WebDriver executable
driver = webdriver.Chrome()

# Open MakeMyTrip website
driver.get('https://www.makemytrip.com/')

# Locate and click on the departure date field
departure_date_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'hp-widget__depart'))
)
departure_date_field.click()

# Select the desired date (e.g., 20th February 2025)
desired_date = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-datepicker-group-first']//a[text()='20']"))
)
desired_date.click()

# Close the browser
driver.quit()



