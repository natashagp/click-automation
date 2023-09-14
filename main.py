import time

# Selenium Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Set location of Chrome Driver
s = Service('location_of_chrome_driver_in_your_computer')

# Set some selenium chrome options
chromeOptions = Options()
driver = webdriver.Chrome()


def initialize_browser():
    count = 0
    # Set Url of Website
    driver.get("url_of_website")
    print("starting_Driver")
    while count < 2:
        print(f"clicking_button {count + 1}")
        # Set Class name of element to click
        click_button = driver.find_element(by=By.CLASS_NAME, value="name_of_class_to_find_element")
        click_button.click()
        time.sleep(10)
        driver.refresh()
        time.sleep(10)
        count += 1


if __name__ == '__main__':
    initialize_browser()
    print("app closed")

