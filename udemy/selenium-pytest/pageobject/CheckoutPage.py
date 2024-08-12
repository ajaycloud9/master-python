from selenium.webdriver.common.by import By


class CheckOutPage():

    def __init__(self, driver):
        self.driver = driver

    item = (By.XPATH,"//a[text() = 'Blackberry']/following::button[1]")

    def get_card_title(self):
        print(*CheckOutPage.item)
        return self.driver.find_element(*CheckOutPage.item)
