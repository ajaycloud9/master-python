from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

class HomePage():

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT,"Shop")

    def shopItems(self):
        print(*HomePage.shop)
        return self.driver.find_element(*HomePage.shop)
